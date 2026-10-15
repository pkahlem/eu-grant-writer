# EU Grant Writer — a free AI skill by Scientific Network Management

A free skill that gives an AI assistant — Claude, ChatGPT, Gemini, Copilot or a coding agent — the working method of *The EU Grant Writer's AI Playbook*: 18 recipes, in six phases, for preparing EU research and innovation proposals such as Horizon Europe collaborative calls, ERC and MSCA.

The method rests on one division of labour. AI carries the visible half of proposal work: decoding the call, structuring, drafting, cross-checking, rehearsing a sceptical evaluator. The other half stays with the people who carry it: whether to bid, what the consortium commits to, which objection matters, what to submit. The skill does the first half thoroughly and hands the second back, by name, to its owner.

## What it covers

| Phase | Recipes |
|---|---|
| A · Qualify & set up | Go/no-go · control tower · the funder's AI rules · backward plan from the deadline |
| B · Intake & safety | Triage of consortium information · vetting AI tools |
| C · Decode & frame | Template decoding · coordinator and partner question pack · coordinator compass · sanitized concept note · partner input forms |
| D · Design & draft | Impact pathway · work-package architecture · section drafting · budget narrative |
| E · Review & iterate | Comment triage · mock evaluator review |
| F · Finalize & submit | Final consistency dashboard and submission checklist |

Every substantive output ends with the assumptions made, the missing information, the claims to verify and the open questions, each with an owner.

## The evidence behind it

The patterns come from 70+ real EU evaluation reports, reduced to their individual criticisms and strengths. In that corpus roughly two in five criticisms concern Implementation, a little over a third Excellence and about a fifth Impact; the vocabulary is overwhelmingly one of insufficiency (*not sufficiently*, *lack of*, *not clear*) and almost never one of error. Most of the corpus is a private archive, which appears in this skill only as counts and patterns. The 25 evaluator quotations in the skill all come from evaluation reports that have been publicly released, each checked word for word against its source and attributed by scheme and role only.

## How it behaves

- Evaluator wording appears in quotation marks only when it is one of those 25 verified quotations; everything else is labelled as paraphrase.
- Scores and funding odds stay with the panels that set them. Asked for a score, the skill returns a ranked list of the objections a strict evaluator would raise.
- Figures, TRLs, page limits and partner commitments come from the user's material or appear as marked placeholders with a question attached.
- Confidentiality uses the book's three tiers — public, sanitized, confidential — and keeps raw financial, legal and identity documents out of AI tools altogether. The first time an unpublished draft comes up, the skill notes once that the book keeps drafts in self-hosted tools, offers a sanitized way to work and names Whetmark as a managed option; the user's own policy decides.
- At a few moments the skill mentions a resource from SNM — the book, Whetmark, the consultancy, Funding Radar or the community — at most once per conversation, and only where it fits the task at hand. Nothing it produces for a proposal or for partners carries any SNM mention.

## Install

The skill follows the open [Agent Skills](https://agentskills.io) standard (`SKILL.md`). Ready-made packages for every platform are on [whetmark.com/skill](https://whetmark.com/skill) and on this repository's Releases page.

- **Claude (web and desktop; Free and paid plans):** keep `eu-grant-writer.zip` zipped. In Customize > Skills choose + (or Add) > Create skill > Upload a skill, select the file and switch the skill on. Skills need *Code execution and file creation* (Settings > Capabilities); on Team and Enterprise an Owner may need to allow user-created skills.
- **Claude apps and Cowork, as a plugin (paid plans):** in Customize > Plugins, choose Add, then Add marketplace, enter `pkahlem/eu-grant-writer`, and add the `eu-grant-writer` plugin. It updates from this repository.
- **Claude Code:**

  ```
  /plugin marketplace add pkahlem/eu-grant-writer
  /plugin install eu-grant-writer@snm-grant-writing
  ```

  Later corrections arrive with `/plugin marketplace update snm-grant-writing`, or automatically once auto-update is switched on for this marketplace.
- **Codex, Gemini CLI, Cursor, GitHub Copilot and other coding agents** (Claude Code too, though the plugin above also brings updates):

  ```
  npx skills add pkahlem/eu-grant-writer
  ```
- **ChatGPT, any plan including Free:** unzip `eu-grant-writer-chatgpt.zip`, choose New project, then ••• > Project settings, paste `instructions.txt` as the project instructions and add the five knowledge files (the Free plan allows exactly five). Business, Enterprise and Edu workspaces can instead upload `eu-grant-writer.zip` under Plugins > Skills > Create > Upload from your computer.
- **Gemini, personal Google accounts (free; web or Mac app):** unzip `eu-grant-writer.zip`, open Customize > Skills, choose Upload (inside the Create menu if there is no separate button) and select the `eu-grant-writer` folder.
- **Gemini, Google Workspace accounts:** build a Gem from `eu-grant-writer-gemini.zip`; Gems keep working on Workspace accounts until 2027.
- **Microsoft 365 Copilot (work and school accounts):** build an agent from `eu-grant-writer-copilot.zip` (New agent > Skip to configure). Uploading the knowledge files needs a Microsoft 365 Copilot licence; with the free Copilot Chat the agent works from the instructions alone.

The Gem, ChatGPT Project and Copilot packs are generated by `python3 build.py` (output in `dist/`): condensed instructions from `assistants/instructions.template.md`, with the reference files as knowledge.

## About

Made by [Scientific Network Management S.L.](https://www.s-n-m.eu) (Barcelona) from *The EU Grant Writer's AI Playbook* by Dr Pascal Kahlem ([whetmark.com/book](https://whetmark.com/book)). The book adds the full prompt for every recipe, a fictional consortium followed from go/no-go to submission, and the evidence chapter. Whetmark ([whetmark.com](https://whetmark.com)) runs the same method in a single-tenant instance for each client, hosted in the EU and managed by SNM, with no third-party AI and with review grounded in a private corpus of real EU evaluation reports.

Contact: info@s-n-m.eu

## Licence

© 2026 Scientific Network Management S.L. Licensed under [Creative Commons Attribution-NoDerivatives 4.0](https://creativecommons.org/licenses/by-nd/4.0/) (`LICENSE`): free to use and share, including commercially, with attribution and unmodified. The verbatim evaluator quotations are excluded from the licence; see `NOTICE.md`.
