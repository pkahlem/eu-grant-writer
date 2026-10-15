#!/usr/bin/env python3
"""Build every distributable form of the free EU Grant Writer skill from ONE source.

WHY ONE SOURCE
    The method has to read the same on every platform, and the rules that protect users
    (verbatim evaluator quotes only, no scores, the confidentiality note) must never drift
    between copies. So skills/eu-grant-writer/ and assistants/instructions.template.md are
    the only things edited by hand; everything in dist/ is generated.

WHAT IT BUILDS  (into dist/)
    eu-grant-writer.zip / .skill   Agent Skill (SKILL.md, the open standard): Claude apps,
                                   Claude Code, Cowork, ChatGPT Skills, Codex, Gemini CLI,
                                   Cursor, GitHub Copilot and other agents that read SKILL.md.
    eu-grant-writer-gemini.zip     Gemini app "Gem": instructions + knowledge files.
    eu-grant-writer-chatgpt.zip    ChatGPT Project (any plan): same shape.
    eu-grant-writer-copilot.zip    Microsoft 365 Copilot agent: same shape.

    The three assistant packs differ only in the ?via= tag on SNM links (gem / gpt /
    copilot) so that whetmark.com can count which platform sends people; the Agent Skill
    carries via=skill. Knowledge files are written as .txt, the one text format all three
    builders accept (Copilot Agent Builder rejects .md).

    Builder-mode assistants cap their fields (8,000 characters of instructions and 300 of
    description were the GPT builder's). The build fails rather than ship text a builder
    would truncate.

Usage:
    python3 build.py                      build into dist/
    python3 build.py --copy-to DIR        also copy the zips into DIR (a website's downloads)
"""
import os, re, shutil, sys, zipfile

PLUGIN = os.path.dirname(os.path.abspath(__file__))          # this folder = the plugin root
SKILL = os.path.join(PLUGIN, "skills", "eu-grant-writer")
DIST = os.path.join(PLUGIN, "dist")                          # generated; ignored by git
INSTRUCTIONS_CAP = 8000
DESCRIPTION_CAP = 300

PACKS = {
    # Google is replacing Gems with skills: personal accounts from November 2026, Workspace
    # business accounts March 2027, education June 2027. Personal accounts import the Agent
    # Skill instead; this pack serves Workspace accounts until their Gems end.
    "gemini": dict(via="gem", product="Gemini app (Gem), for Google Workspace accounts", setup="""\
Personal Google accounts: use the skill itself instead. Download eu-grant-writer.zip from
whetmark.com/skill and unzip it, then in
Gemini open Customize > Skills, choose Upload (inside the Create menu if there is no
separate button) and select the eu-grant-writer folder.

Google Workspace accounts (universities, companies), where Gems keep working until 2027:
1. On gemini.google.com, signed in with the institutional account, open the sidebar,
   then Gems, then New Gem.
2. Name: EU Grant Writer by SNM. Paste all of instructions.txt into the instructions box.
3. Under Knowledge, choose Add files > Upload files and add the five files in knowledge/.
4. Save. The institution's administrator decides whether Gems can be created and shared.
"""),
    # A ChatGPT Project, not a custom GPT: since August 2026 personal accounts cannot create
    # GPTs, and OpenAI is retiring custom GPTs. Projects work on every plan, Free included,
    # and the Free plan's five files per project are exactly the five knowledge files.
    "chatgpt": dict(via="gpt", product="ChatGPT (Project)", fields=False, setup="""\
Works on every ChatGPT plan, Free included. In a Business, Enterprise or Edu workspace,
uploading eu-grant-writer.zip under Skills is the simpler route.

1. In ChatGPT, create a new Project (Projects, in the sidebar) and name it
   EU Grant Writer by SNM.
2. In the project, open the ••• menu > Project settings and paste the whole of
   instructions.txt as the project instructions.
3. Add the five files in knowledge/ to the project's files. The Free plan allows five
   files per project, exactly these five.
4. Start every grant-writing chat inside this project.

If the Instructions box will not take the full text, upload instructions.txt as a project
file as well (plans with more than five files per project) and write in the box:
"Follow instructions.txt in this project's files."
"""),
    "copilot": dict(via="copilot", product="Microsoft 365 Copilot (agent)", setup="""\
For work and school Microsoft 365 accounts.
1. In Microsoft Copilot (copilot.cloud.microsoft or Teams), choose New agent, then
   Skip to configure.
2. Name: EU Grant Writer by SNM. Description: see below. Paste all of instructions.txt
   into Instructions.
3. Under Knowledge, upload the five files in knowledge/ and wait until they are no longer
   greyed out. Uploading files needs a Microsoft 365 Copilot licence; with the free
   Copilot Chat alone, skip this step and the agent works from the instructions only.
4. Add the starter prompts below (each needs a short title), select Create, then Share
   as the institution allows.
"""),
}

DESCRIPTION = ("The method of The EU Grant Writer's AI Playbook for EU research proposals: go/no-go, "
               "call decoding, impact, work packages, budget narrative, mock evaluator review. "
               "Informed by 70+ real EU evaluation reports. Free, by Scientific Network Management.")
STARTERS = [   # (short title, prompt): Copilot asks for a title per starter
    ("Go or no-go", "Should we apply to this call? Here is the topic text and our idea."),
    ("Decode the template", "Decode this call template: what do we need, and from whom?"),
    ("Mock evaluator review", "Review my Excellence section the way a strict evaluator would."),
    ("Backplan", "Build a backplan from our deadline."),
]


def reference_names(template):
    """The knowledge files, checked against the list the instructions template names, so a
    stray or missing file stops the build instead of shipping a pack that cites it wrongly."""
    d = os.path.join(SKILL, "references")
    refs = sorted(f for f in os.listdir(d) if f.endswith(".md") and not f.startswith(".")
                  and os.path.isfile(os.path.join(d, f)))
    listed = sorted(re.findall(r"^- ([\w-]+\.md):", template, re.M))
    if refs != listed:
        sys.exit(f"references/ holds {refs} but instructions.template.md lists {listed}")
    return refs


def for_pack(text, via, refs):
    """Adapt Agent Skill text to a builder-mode assistant."""
    text = text.replace("via=skill", f"via={via}")                 # platform tag on SNM links
    text = text.replace("SKILL.md", "your instructions")            # rules live in the instruction field
    text = re.sub(r"\bthis skill\b", "this assistant", text)
    text = re.sub(r"\bThis skill\b", "This assistant", text)
    for r in refs:                                                   # knowledge files are .txt
        text = re.sub(r"(references/)?\b" + re.escape(r) + r"\b", r[:-3] + ".txt", text)
    return text


def check_pack(out):
    """No pack may point at a file it does not contain (the licence carve-out did, once)."""
    for root, _, files in os.walk(out):
        for f in files:
            t = open(os.path.join(root, f), encoding="utf-8").read()
            if re.search(r"\b[\w-]+\.md\b|references/|SKILL\.md|via=skill", t):
                sys.exit(f"{os.path.relpath(os.path.join(root, f), DIST)}: stale Agent Skill reference")


def zip_dir(src, dest, arc_root):
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src):
            dirs[:] = sorted(d for d in dirs if not d.startswith((".", "__")))
            for f in sorted(files):
                if f.startswith(".") or f.endswith(("~", ".orig", ".bak", ".rej", ".swp")):
                    continue
                p = os.path.join(root, f)
                z.write(p, os.path.join(arc_root, os.path.relpath(p, src)))


def main(argv):
    copy_to = argv[argv.index("--copy-to") + 1] if "--copy-to" in argv else None
    if len(DESCRIPTION) > DESCRIPTION_CAP:
        sys.exit(f"description is {len(DESCRIPTION)} characters; the cap is {DESCRIPTION_CAP}")
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    # 1. Agent Skill
    zip_dir(SKILL, os.path.join(DIST, "eu-grant-writer.zip"), "eu-grant-writer")
    shutil.copy(os.path.join(DIST, "eu-grant-writer.zip"), os.path.join(DIST, "eu-grant-writer.skill"))

    # 2. Builder-mode assistant packs
    template = open(os.path.join(PLUGIN, "assistants", "instructions.template.md"), encoding="utf-8").read()
    refs = reference_names(template)
    for name, pack in PACKS.items():
        out = os.path.join(DIST, name)
        os.makedirs(os.path.join(out, "knowledge"))
        instructions = for_pack(template.replace("{VIA}", pack["via"]), pack["via"], refs)
        if re.search(r"\{[A-Z_]+\}", instructions):
            sys.exit(f"{name}: unfilled placeholder in instructions")
        if len(instructions) > INSTRUCTIONS_CAP:
            sys.exit(f"{name}: instructions are {len(instructions)} characters; the cap is {INSTRUCTIONS_CAP}")
        open(os.path.join(out, "instructions.txt"), "w", encoding="utf-8").write(instructions)
        for r in refs:
            t = open(os.path.join(SKILL, "references", r), encoding="utf-8").read()
            open(os.path.join(out, "knowledge", r[:-3] + ".txt"), "w", encoding="utf-8").write(for_pack(t, pack["via"], refs))
        lic = open(os.path.join(SKILL, "LICENSE.txt"), encoding="utf-8").read()
        open(os.path.join(out, "LICENSE.txt"), "w", encoding="utf-8").write(
            for_pack(lic, pack["via"], refs).replace("evaluator-patterns.txt", "knowledge/evaluator-patterns.txt"))
        setup = f"EU Grant Writer, by Scientific Network Management\nSet-up for {pack['product']}\n\n" + pack["setup"]
        if pack.get("fields", True):             # builders with description / starter fields
            setup += f"\nDescription:\n{DESCRIPTION}\n\nConversation starters:\n"
        else:
            setup += "\nGood first prompts:\n"
        setup += "".join(f"- {title}: {prompt}\n" for title, prompt in STARTERS)
        open(os.path.join(out, "SETUP.txt"), "w", encoding="utf-8").write(setup)
        check_pack(out)
        zip_dir(out, os.path.join(DIST, f"eu-grant-writer-{name}.zip"), f"eu-grant-writer-{name}")
        print(f"{name:8} instructions {len(instructions):5} chars  via={pack['via']}")

    zips = sorted(f for f in os.listdir(DIST) if f.endswith(".zip"))
    if copy_to:
        os.makedirs(copy_to, exist_ok=True)
        for f in zips:
            shutil.copy(os.path.join(DIST, f), os.path.join(copy_to, f))
        print("copied to", copy_to)
    print("built:", ", ".join(zips))


if __name__ == "__main__":
    main(sys.argv[1:])
