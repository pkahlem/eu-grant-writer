# The 18 recipes

Condensed from *The EU Grant Writer's AI Playbook*. Each recipe: when to use it, its confidentiality tier, the method, what to produce, the quality check, and the mistakes that most often sink it. The tier says which kind of material the step needs (see `confidentiality.md`); when in doubt, the stricter tier wins. The book adds a worked example and the full prompt for every recipe, and evaluator-evidence boxes on the recipes where the corpus speaks most directly.

**Contents**
- Phase A · Qualify & set up — 1 Go/no-go · 2 Control tower · 3 Funder's AI rules · 4 Backplan
- Phase B · Intake & safety — 5 Triage information · 6 Vet AI tools
- Phase C · Decode & frame — 7 Decode the template · 8 Question pack · 9 Coordinator compass · 10 Sanitized concept note · 11 Partner inputs
- Phase D · Design & draft — 12 Impact pathway · 13 Work packages · 14 Section drafting · 15 Budget narrative
- Phase E · Review & iterate — 16 Feedback rounds · 17 Mock evaluator review
- Phase F · Finalize & submit — 18 Final submission control
- Universal rules for every output

---

## Phase A · Qualify & set up

### 1. Qualify the bid (go / no-go)
**Use when** a call looks attractive and the idea exists, before partners are contacted or anything is set up. **Tier:** sanitized (public call text + a safe summary of idea and consortium + the user's capacity notes).

Two separate dimensions, kept separate to the end:
- *Call fit and eligibility.* Extract the call's real scope, priorities and success signals; mark where the fit is genuine and where it is forced. Check applicant and consortium eligibility (types, countries, minimum partners). Check each hard constraint — deadline, budget envelope and funding rate, required TRL or readiness level, every mandatory condition (activities, co-funding, letters, ethics gates) — as achievable / at risk / not achievable. Look for a fatal blocker: one unmeetable condition ends the bid regardless of everything else.
- *Capacity to carry the orchestration.* Estimate the real coordination load — chasing and reconciling partner input, signatures, portal, deadline — which scales with consortium size and does not shrink because AI helps write. Compare it honestly with the user's time and other deadlines. Name what would make it carryable: a co-writer, a dedicated coordinator, professional support, a smaller partner set.

**Produce:** call-fit assessment; eligibility check (eligible / not eligible / verify, citing the rule); constraint check; any fatal blocker; orchestration-load estimate separating writing effort from coordination effort; the capacity gap; for each option — **bid**, **no-bid**, **bid-with-professional-support** — the one or two factors weighing for and against it. Lay the options out, brand-free; the decision belongs to the user. Close with what would turn a no-bid or bid-with-support into a clean bid.

**Quality check:** fit is genuine rather than squinted at; eligibility confirmed against official rules; no unresolved fatal blocker; capacity judged apart from writing ability; the decision written down explicitly.

**Common mistakes:** reading the call generously to make the idea fit (evaluators will squint too); judging the call and forgetting the team; treating *AI can write it* as *AI can carry it*; leaving the decision implicit (*we'll probably go for it*); killing a good idea on capacity alone, when the honest answer is bid-with-support.

### 2. Set up the proposal control tower
**Use when** starting any consortium proposal, before drafting. **Tier:** confidential (real partner list, internal WP themes) — or work from roles only to keep it sanitized.

Method: one master proposal file and one version convention; one decision log (scope, budget, WP leadership, final claims); one partner-input tracker; an explicit split between work that may use AI and work that stays offline; one named final approver.

**Produce:** role map; source-of-truth document list; decision-log structure; partner-input tracker structure; AI-supported tasks; offline-only tasks; immediate actions for the writer — a one-page operating note the coordinator can circulate in hour one.

**Common mistakes:** standing the tower up after drafting has begun (the versions have already multiplied); an implicit AI boundary ("use good judgement" is not a data policy); confusing the coordinator with the decision owner; filing admin inside the narrative; "the consortium approves" instead of one named approver.

### 3. Confirm the funder's AI rules
**Use when** at the very start, before any AI-assisted workflow. **Tier:** public.

Method: gather the current call text, applicant guide and portal terms. Establish (a) whether applicant AI use is permitted, (b) which uses are restricted or prohibited, (c) whether AI use must be disclosed or attested, and in what form. Silence means "not confirmed", never "allowed" — assign verification to the research office or funder. Record the result in the decision log; put any required disclosure on the final checklist (Recipe 18). The AI boundary for the proposal is the stricter of the funder's rules and the organisation's data policy.

**Produce:** a dated decision-log entry: permitted? / restricted uses / disclosure required (verbatim wording and placement) / AI boundary — each line with its source (document and section) or "not confirmed" with an owner and a deadline. Quote obligations verbatim; never paraphrase a requirement.

**Common mistakes:** treating silence as permission; checking only the call text and missing the guide or portal terms; recording a required disclosure but never adding it to the checklist; confusing evaluator confidentiality rules (which bind the funder's reviewers) with applicant permissions; relying on last year's conditions.

### 4. Build the submission backplan
**Use when** right after the control tower, before requesting input; rebuild when deadline, consortium or scope change. **Tier:** sanitized (roles and lead times, no partner names).

Method: anchor everything to the portal deadline (date, time, time zone) and express every milestone as "D minus N days". Place the unrecoverable steps first — portal upload, signatures, admin declarations, final coordinator approval. Set content, budget and admin freezes, each before the step that depends on it, with buffer before each freeze for late input and long review rounds. One owner per milestone. Mark the critical path and the points where a one-day slip is unrecoverable. Set an internal target earlier than the portal deadline.

**Produce:** a milestone table (Milestone | Owner | Due as D minus N | Depends on); the three freeze dates; the critical path; unrecoverable points; built-in buffers; the internal target. A typical shape: partner input D−35, content freeze D−21, mock review D−18, budget freeze D−14, admin/signature freeze D−10, final approval D−5, upload and preview D−3, internal submit D−2 — widened wherever signatures or slow partners sit on the critical path.

**Common mistakes:** planning forwards from today; fixed calendar dates that break on reuse; treating the portal deadline as the internal one; assuming partners answer on time; scheduling signatures as if they can be rushed; a milestone with no owner.

---

## Phase B · Intake & safety

### 5. Triage consortium information
**Use when** any input arrives — coordinator notes, partner input, comments, budgets, admin, legal, ethics, drafts. **Tier:** confidential (the sanitizing itself reads raw internal notes); offline-only material is never pasted at all.

| Input | Handling |
|---|---|
| Public call, template, guide, FAQ | AI-ready |
| Public partner profiles and track record | AI-ready, then verify |
| Proposal-facing partner contribution | AI-ready if no confidential detail |
| Internal partner notes or comments | Sanitize first — remove conflict, leverage, private constraints, negotiation language |
| High-level budget logic | Sanitize or aggregate first |
| Raw budget files, salaries, bank or legal data | Offline only |
| Admin forms, signatures, declarations, IDs | Offline only — track, never draft with AI |
| IP, legal agreements, confidential datasets | Offline only — legal or institutional review |

Method: label every input; rewrite sanitize-first material into proposal-facing language ending with an "information still needed" list; log offline items in the tracker; ask whether the AI needs the source or only a safe summary; when unsure, keep it offline and use a placeholder.

**Common mistakes:** labelling the whole folder AI-ready because the deadline is close; sanitizing the words but keeping the meaning (the conflict is still reconstructable); letting AI "summarize" a raw budget file; drafting around a partner's private constraint as if it were a proposal fact; deleting an offline item instead of tracking it.

### 6. Vet the AI tools
**Use when** before any proposal content enters any tool, and again whenever a tool, plan or provider changes. **Tier:** public (vendor documentation only).

Five questions per tool, each answered from a cited source — policy clause, DPA or vendor email, never a salesperson's word:
1. **Training** — does it train on inputs; is that the default; can it be switched off in writing?
2. **Retention** — how long, where, can it be zero?
3. **Subprocessors and jurisdiction** — who else processes the data, and where?
4. **Contract** — is a data-processing agreement available?
5. **Isolation** — account isolation, access controls, no routine human review?

Classify each tool **vetted** (AI-ready content), **restricted** (sanitized or aggregated only) or **blocked** (no proposal content), and match the classification to the triage of Recipe 5. Include embedded features — transcription, translation plugins, "smart" functions in office software. Date the register and schedule a re-check. A not-yet-submitted proposal is competitively sensitive even when it holds no secret data: pasted into a tool that trains on inputs, it is effectively published.

**Produce:** a dated register — one row per tool (plan), five answers with sources, a verdict, the approver, a re-check date. For each verdict option, lay out the decisive clauses; the classification is the user's.

---

## Phase C · Decode & frame

### 7. Decode the funder template
**Use when** right after choosing the call, before drafting and before asking anyone for input. **Tier:** public (call package and blank template only).

Method: map every section, table, limit and hidden requirement; identify who must supply each input; propose an AI-handling label for each input (the user confirms); turn the map into the question pack. Do not draft yet.

**Produce a Proposal Information Map** — per template section: title; purpose; required information; page/word/table limits; linked evaluation criterion; inputs needed from coordinator, WP leaders, partners, finance/admin/compliance; AI-handling label; risk if weak; drafting order. Then a **hidden-requirements checklist** grouped by proposal content, budget, consortium, ethics/compliance, annexes and portal: mandatory tables, limits, KPIs, partner descriptions, budget justification, ethics, data protection, gender, inclusion, sustainability, dissemination/exploitation/communication, annexes, signatures and declarations, naming and formatting rules.

**Quality check:** complete (every section, table and annex mapped); owned (every input names a person or role — "the consortium" is not an owner); classified; honest about gaps (anything the documents do not settle is "verify in the official call documents").

**Common mistakes:** drafting straight after uploading the template; skipping the mandatory tables (objectives, effort, deliverables, milestones, critical risks are scored and need partner data); inventing limits or requirements.

### 8. Generate the question pack
**Use when** right after the template map, before collecting detailed input — one of the highest-value uses of AI in the whole process. **Tier:** sanitized.

Principle: never "please send your input". Ask specific questions tied to named sections, with a deadline and a length.

**Produce** separate sets for coordinator, WP leaders, partners, finance/admin, ethics/legal/compliance. Per question: the question; why it is needed; the section it supports; recommended answer length; deadline or urgency; AI-handling label; essential or optional. Keep it short; prioritise what unlocks the proposal logic, WPs, impact, budget justification, implementation and compliance.

Coordinator questions when an outline exists: the central problem; why urgent now; the solution in one paragraph; 3–5 objectives; what differs from existing approaches; target users; concrete outputs; end-of-project outcomes; essential partners and why; imagined WPs; evidence of need and feasibility; biggest risks; what must not be processed with AI. When no outline exists: the opportunity; why the funder would care; who benefits; existing assets; partners that would make it credible; realistic activities; measurable outcomes; what makes it timely; what would make an evaluator doubt it; the simplest fundable version; the ambitious version.

**Common mistakes:** one long questionnaire for everyone; asking for "input" without naming the section; no AI-handling label; giving the coordinator only logistics; no deadline or length; sending once and never chasing.

### 9. Build the coordinator compass
**Use when** after the question pack, once the coordinator has answered the framing questions. **Tier:** sanitized.

**Produce one page:** one-sentence project promise; problem statement; target users and beneficiaries; proposed solution; 3–5 objectives; likely WP themes; in scope; out of scope; decisions still needed from the coordinator; questions for partners; risks if the direction stays vague. Use the funder's language.

**Quality check:** the coordinator can explain the project in one minute; scope is not too broad; open decisions are visible; the compass is approved before detailed drafting. An empty "decisions still needed" list usually means the hard choices were dodged.

### 10. Prepare the sanitized concept note
**Use when** before project material goes in front of AI again and again. **Tier:** the input is confidential; the output is the reusable sanitized source.

| Field | Include | Leave out |
|---|---|---|
| Problem | Publicly explainable need | Internal weaknesses, private trigger events |
| Innovation | High-level novelty and value | Unpublished proprietary detail |
| Objectives | Coordinator-approved objectives | Unapproved commitments |
| Approach | Method at funder-facing level | Sensitive operational or data detail |
| Consortium | Public strengths, functional roles | Partner conflict, negotiation positions |
| Budget logic | Approved high-level rationale | Salary rates, raw spreadsheets |
| Risks | Proposal-facing risks and mitigations | Reputational vulnerabilities |

Replace every sensitive specific with a marked placeholder (`[BUDGET SPLIT — TBC]`), never with an invented stand-in; end with "information still needed"; get a coordinator glance before it becomes the source every later step reads.

**Common mistakes:** over-sanitizing into vagueness ("an innovative energy solution" protects nothing and helps nothing); leaving the tensions in; filling gaps with invented facts; never updating it; pasting the budget spreadsheet "for context".

### 11. Collect partner inputs
**Use when** after the question pack and an approved compass. **Tier:** confidential (compass, WP structure and partner contacts).

**Produce:** a short partner email; one form per input type — partner profile, WP contribution, impact/dissemination, budget/person-months, risk/ethics/data — every field with a one-line why, the section it feeds, an answer length and an AI-handling label; a separate admin-document checklist (legal entity, signatures, declarations, portal data — never mixed into drafting input); a response tracker per partner and form (received / missing / unclear / approved). Earlier deadlines for slow partners; a worked example in each field for partners new to EU proposals; a way for partners to flag confidential content.

---

## Phase D · Design & draft

### 12. Build the impact pathway
**Use when** after the concept note and compass, once first partner inputs are in, and **before** the work packages are fixed — impact is designed backwards. **Tier:** sanitized.

Method: list target groups and beneficiaries, each with a need and a way of using the results; separate end-of-project **outcomes** (measurable) from longer-term **impacts** (directional, beyond the project's control); map activities → outputs → outcomes → impact per objective and drop any output that leads nowhere; name the key exploitable results with a route to uptake and who takes them up; draft exploitation, dissemination and communication as three distinct plans, every action with an audience, an indicator, a baseline and target, and a timing; state sustainability (what continues and who pays), IPR at proposal level, and the assumptions and barriers with mitigations; assign every outcome to at least one work package.

**Produce:** an impact-logic map (as text or table); the impact plan; an outcome-to-WP list; the indicator set; open questions.

**Common mistakes:** calling an output "impact" (a report, a tool or a workshop is an output); dissemination channels with no audience, indicator or target; merging exploitation, dissemination and communication; outcomes no work package delivers; sustainability with no owner, funding route or timeline.

### 13. Build the work-package architecture
**Use when** concept note, template map, compass and first partner summaries exist. **Tier:** sanitized.

Method: titles and objectives first; review with the coordinator; only then expand approved WPs into tasks, deliverables, milestones, dependencies and owners; check against person-month reality; send gaps back to WP leads.

**Produce, pass 1:** WP list; title; objective; why the WP is necessary; partners involved; key dependencies; what the evaluator should understand; open questions. **Pass 2, per approved WP:** objective; tasks with owners (each task stated as work, with a verb — never a title alone); deliverables with due months; milestones with due months; dependencies; required partner inputs; risks with mitigations and owners; evidence needed.

**Quality check:** every objective maps to a WP and every WP to an objective; every lead has agreed to lead (flag every assumed commitment); effort matches ambition (six tasks and one part-time researcher is a fiction); no WP depends on a deliverable that lands after it is needed; titles carry funder meaning ("WP3 — Technical Work" tells an evaluator nothing).

### 14. Draft from template sections
**Use when** there is enough information for one specific section — draft in controlled passes, without waiting for everything. **Tier:** sanitized context and partner summaries.

Method: one section at a time; work from the section's purpose, limit, criterion, the sanitized content and the missing-information list; integrate into the master by hand; turn gaps into partner questions.

**Produce:** the draft within the limit; assumptions made; missing evidence; claims that need verification; questions for coordinator or partners. Every objective slot gets an indicator, every method slot a named method, every claim a citation or datum — or a placeholder.

**Common mistakes:** drafting the whole proposal in one pass; feeding raw partner emails; trusting fluency; letting the model fill a gap with a plausible number, TRL or commitment; echoing the call keyword-for-keyword.

### 15. Split budget narrative from admin data
**Use when** drafting budget justification, resource rationale or person-month explanations. **Tier:** sanitized — aggregated totals or percentages by category, approved person-month overview; never salaries, rates, margins, invoices or bank data.

**Produce:** a budget justification paragraph; WP-by-WP resource rationale; budget logic that may look weak (this list should never be empty); questions for finance/admin; items requiring manual verification. Add no numbers and infer no salaries or rates; every figure traces to one the user supplied. The narrative is reconciled against the real workbook by the user and finance.

---

## Phase E · Review & iterate

### 16. Run feedback rounds
**Use when** a versioned draft has gone to several reviewers and the comments must be reconciled. **Tier:** sanitized comments (names, budgets, partner-identifying detail removed).

**Produce a triage table:** theme · action (accept / clarify / park / reject / coordinator decision) · reason · proposed rewrite where editorial · owner. Name contradictions between reviewers instead of averaging them; route every strategic or political comment (a TRL claim, a budget reallocation, risk tone) to "coordinator decision"; never let an accepted comment introduce a new fact. Keep a change log and an unresolved-decision list.

### 17. Run a mock evaluator review
See `mock-review.md` for the full procedure. **Tier:** the draft is confidential — apply the confidentiality note in SKILL.md once; when the draft is already pasted, give the note and review in the same reply.

### 18. Final submission control
**Use when** in the last days, once the proposal is essentially written — never while sections are still moving. **Tier:** the frozen master is confidential.

Method: freeze one master version with one owner; run the dashboard; verify forms and admin manually; check the budget narrative against the workbook; remove placeholders; check that no internal language leaked; coordinator approval; submit; archive exactly what was sent.

**Final dashboard checks:** unresolved placeholders; inconsistent terminology; acronym drift; deliverable and milestone inconsistencies (text vs tables vs Gantt); budget references needing verification; partner-role inconsistencies; unsupported claims; overclaims; broken links between objectives, WPs, outcomes and impact; internal notes left in ("[check with legal]"); passages hard for a tired evaluator.

**Manual checklist (a human ticks each):** official call version; portal deadline and format; budget workbook final; admin documents received; signatures and declarations complete; annexes in the correct format; coordinator approval received; AI-use disclosure included if required; portal preview checked; submitted package archived.

**Common mistakes:** polishing and submitting at once; trusting the dashboard's silence (it cannot see the portal, signatures or annex formats); editing after the freeze; submitting in the last hour — portals slow down under load; aim a full day early.

---

## Universal rules for every output

Every task framed for AI carries: a role; the exact task; the safe context; the funder criteria; the constraints (limits, duration, budget envelope); the data boundaries (what not to use, infer or invent); the output format; and verification — assumptions, missing information, manual checks. The book's universal prompt (Appendix B) carries five rules worth applying to every output: do not invent facts; mark assumptions clearly; separate writing issues from strategic decisions; list missing information; identify what the writer must verify by hand.
