# Running a Hierarchy of LLM Agents: Evidence-Backed Operating Practices

**Scope:** CEO orchestrator -> venture managers -> up to 4 workers per venture, plus a shared Research Lab and a Design/Coding Studio.
**Date:** 2026-10-21
**Bottom line:** Quality comes from four things: (1) precise briefs, (2) external verification signals rather than self-assessment, (3) a reusable playbook in git that grows from observed failures, and (4) effort scaled to the task. Agents don't update their weights. "Training" them means writing and pruning the instructions, examples, checklists and notes they load.

---

## 0. Key evidence at a glance

| Finding | Source |
|---|---|
| Multi-agent research (Opus lead + Sonnet subagents) beat a single Opus agent by 90.2% on Anthropic's internal research eval. It also used about 15x the tokens of a chat, versus about 4x for a single agent. | [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) |
| Token usage alone explained about 80% of performance variance on BrowseComp. Tool-call count and model choice explained most of the rest (about 95% combined). | same |
| Vague delegation caused duplicated work: subagents need an objective, an output format, tool and source guidance, and boundaries. | same |
| Effort-scaling rules fixed over-spawning (one early version spawned 50 subagents for simple queries). | same |
| An LLM can't reliably self-correct its reasoning without external feedback, and performance often drops after self-correction. Execution results, tools and search do help. | [Huang et al., ICLR 2024](https://arxiv.org/abs/2310.01798) |
| Iterative self-refinement improves outputs by about 20% absolute on average. Secondary summaries report that most gains come in the first 2-3 rounds. | [Madaan et al., Self-Refine, NeurIPS 2023](https://arxiv.org/abs/2303.17651); [overview](https://www.alphaxiv.org/overview/2303.17651v2) |
| Verbal "lessons learned" memory (no weight updates) raised HumanEval pass@1 to 91%. | [Shinn et al., Reflexion, NeurIPS 2023](https://arxiv.org/abs/2303.11366) |
| Multi-agent failures are mostly design and specification issues: 14 failure modes in 3 categories. The verification category covers premature termination, missing or incomplete verification, and incorrect verification. | [Cemri et al., "Why Do Multi-Agent LLM Systems Fail?", NeurIPS 2025](https://arxiv.org/abs/2503.13657) |
| LLM judges show position, verbosity and self-enhancement bias, yet strong judges agree with humans over 80% of the time, about the rate humans agree with each other. | [Zheng et al., MT-Bench, NeurIPS 2023](https://arxiv.org/abs/2306.05685) |
| LLM evaluators recognize their own outputs and favor them, and self-recognition correlates linearly with self-preference. | [Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076) |
| A reviewer prompted to find gaps will report some even when the work is sound. Chasing every finding leads to over-engineering. | [Claude Code best practices](https://code.claude.com/docs/en/best-practices) |
| Parallel agents acting on implicit, unshared decisions produce inconsistent results. Share context, and keep decision-making and execution together. | [Cognition, "Don't Build Multi-Agents"](https://cognition.com/blog/dont-build-multi-agents) |
| Sampling several agents and taking a majority vote improves accuracy, and the gain is larger on harder tasks. | [Li et al., "More Agents Is All You Need", TMLR 2024](https://arxiv.org/abs/2402.05120) |
| Prefer binary pass/fail judgments with written critiques over 1-5 scores, and calibrate the judge against an expert. | [Hamel Husain via Simon Willison](https://simonwillison.net/2024/Oct/30/llm-as-a-judge) |

---

## 1. How to "train" agents in practice

Agents don't learn between runs. All improvement lives in files they load: system prompts, skills, examples, checklists, style guides and memory notes. Treat these files like code: version them, review them, test them and prune them.

### 1.1 Layers of instruction, from always-loaded to on-demand

| Layer | What goes in it | Loaded when | Guidance |
|---|---|---|---|
| `CLAUDE.md` (root and per-venture) | Org-wide rules, commands, gotchas, definition of done | Every session | Keep it short. For each line ask: "Would removing this cause mistakes?" Bloated files cause agents to ignore rules. ([best practices](https://code.claude.com/docs/en/best-practices)) |
| Agent definitions (`.claude/agents/*.md`) | Role, tools allowlist, model, maxTurns, preloaded skills, memory scope | When the agent is spawned | Give each agent one focused job and least-privilege tools. Reviewers and researchers get read-only tools. ([subagents](https://code.claude.com/docs/en/sub-agents)) |
| Skills (`.claude/skills/<name>/SKILL.md`) | Procedures, templates, worked examples, scripts | Only the name and description load at startup; the body loads when relevant | Keep the body under 500 lines and reference files one level deep. Write the description in third person with trigger terms. Use scripts for deterministic steps. ([skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)) |
| Agent memory (`.claude/agent-memory/<agent>/MEMORY.md`) | Accumulated lessons and project facts | First 200 lines or 25KB load at start | `memory: project` is git-shareable. Tell the agent to read memory before starting and save learnings after. ([subagents](https://code.claude.com/docs/en/sub-agents)) |
| Hooks | Things that must happen with zero exceptions, such as running tests or blocking writes to protected paths | Deterministic | "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic." ([best practices](https://code.claude.com/docs/en/best-practices)) |

### 1.2 Writing instructions that work

- **Right altitude.** Avoid both brittle if/else logic and vague guidance that assumes shared context. Start with a minimal prompt on the strongest model, then add instructions only for failure modes you observe. ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents))
- **Explain why.** "Your response will be read aloud by TTS, so never use ellipses" beats "NEVER use ellipses", because Claude generalizes from the reason. ([prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices))
- **Worked examples are the strongest steering tool.** Use 3-5 relevant, diverse examples wrapped in `<example>` tags. Present each as a problem, the method to apply, and the expected answer. (same)
- **Degrees of freedom.** For fragile operations ("narrow bridge"), give low freedom and exact scripts. For open problems ("open field"), give heuristics. ([skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices))
- **Checklists** that the agent copies into its output and ticks off keep it from skipping validation steps. (same)
- **Use consistent terminology**, give one default rather than many options, and leave out time-sensitive information. (same)
- **Emphasis is scarce.** Mark at most one or two rules as IMPORTANT. If everything is emphasized, nothing is. ([best practices](https://code.claude.com/docs/en/best-practices))

### 1.3 Accumulating playbooks (the "training loop")

This is the Reflexion pattern done by hand, in git:

1. **Evaluation first.** Run the agent on 3+ representative tasks without the new instruction. Record the specific failures and a baseline. ([skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices))
2. **Write the minimal instruction** that fixes the observed failure, never imagined ones.
3. **Use a Claude A / Claude B loop.** One instance (A) edits the skill; a fresh instance (B) uses it on real tasks; you watch B and bring the evidence back to A. (same)
4. **Retrospective note.** At the end of each task, the worker appends a dated lesson to its `MEMORY.md`: what failed, the root cause, and the rule that prevents it. The manager decides whether to promote it to the venture playbook, and the CEO or Research Lab decides whether to promote it to org-wide skills.
5. **Prune.** If an agent already behaves correctly without an instruction, delete the instruction or turn it into a hook. ([best practices](https://code.claude.com/docs/en/best-practices))

Promotion ladder: **worker memory -> venture playbook -> org skill -> hook or script.** Each step up needs evidence that the rule helped on at least two tasks.

---

## 2. Review loops: rubric, rounds, stopping rules, independence

### 2.1 Why review must be external

- Self-critique without an external signal often makes reasoning worse. ([Huang et al.](https://arxiv.org/abs/2310.01798))
- Judges favor their own outputs, longer answers, and answers in certain positions. ([Panickssery](https://arxiv.org/abs/2404.13076), [Zheng](https://arxiv.org/abs/2306.05685))
- Missing or incorrect verification is a top-level failure category in multi-agent systems. ([MAST](https://arxiv.org/abs/2503.13657))

**Rules that follow from this evidence:**

1. **Ground every review in executable evidence wherever possible:** tests, builds, linters, screenshots, link checks, numeric reproductions. "Give Claude a check it can run." Require evidence (command plus output), not claims. ([best practices](https://code.claude.com/docs/en/best-practices))
2. **The reviewer must be a fresh context.** It sees only the artifact, the brief and the rubric, never the worker's reasoning. ([best practices: adversarial review step](https://code.claude.com/docs/en/best-practices))
3. **Use a different model or prompt from the generator** for high-stakes reviews, to reduce self-preference bias.
4. **Score each dimension as binary checks first, then aggregate.** Binary checks with written critiques are more reliable than holistic 1-5 or 1-100 scores. ([Husain](https://simonwillison.net/2024/Oct/30/llm-as-a-judge); [Anthropic evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)) A 0-100 score is fine as a summary, but derive it from weighted checks rather than asking for a gut number.
5. **Give the judge an "Unknown / can't verify" option** to reduce hallucinated grades. ([Anthropic evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents))
6. **Grade outcomes, not paths.** Don't penalize a valid approach you didn't anticipate. (same)

### 2.2 Revision rounds and stopping rules (max 5)

The evidence suggests most gains come in rounds 1-2 and diminish after 2-3. Anthropic also warns that after two failed corrections, context is polluted and a fresh start with a better brief usually beats continuing. ([Self-Refine](https://www.alphaxiv.org/overview/2303.17651v2); [best practices](https://code.claude.com/docs/en/best-practices))

**Stopping rules:**

| Condition | Action |
|---|---|
| Score >= 85, all must-pass gates pass | **Accept.** Log optional nits; don't loop on them. |
| Score 70-84, gates pass | One more targeted revision round, fixing only the named blocking issues. |
| Any must-pass gate fails | Revise, whatever the score. |
| Score improves by less than 5 points between rounds, or the same issue recurs twice | **Stop iterating.** Escalate: re-brief from scratch in a new worker context, change the approach or model, or descope. |
| Round 3 still below 70 | Kill or re-scope. The brief or task is probably broken. ([Anthropic evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): if all trials fail, suspect the task or grader) |
| Round 5 reached | Hard stop. Ship the best version if it passes gates; otherwise escalate to the CEO with a failure note. |

### 2.3 Avoiding rubber-stamping

- **Ask the reviewer to try to refute the work** ("find the strongest reason this is wrong"), not to approve it.
- **Require citations of evidence for every pass**: the test output, line references, or the source URL. A "pass" with no evidence counts as Unknown.
- **Use seeded defects (canaries).** Occasionally hand reviewers work with a known planted bug. If a reviewer misses canaries, recalibrate its prompt or switch its model.
- **Calibrate against humans.** Periodically compare reviewer verdicts with a human or expert verdict until they rarely diverge. ([Anthropic evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); [Husain's critique shadowing](https://simonwillison.net/2024/Oct/30/llm-as-a-judge))
- **Track pass rates.** A reviewer passing over 95% of first drafts is probably rubber-stamping; one passing under 20% is probably miscalibrated or working from a broken brief.

### 2.4 Avoiding over-iteration

- Separate **blocking** findings (correctness and stated requirements) from **optional** ones. Only blocking findings trigger a revision. "Tell the reviewer to flag only gaps that affect correctness or the stated requirements, and treat the rest as optional." ([best practices](https://code.claude.com/docs/en/best-practices))
- Freeze the rubric before work starts. No new criteria mid-loop.
- Watch for reward hacking: workers can game tests (hard-coding, deleting tests). Instruct them that tests are there to verify correctness, not to define the solution, and that removing or editing tests is unacceptable. ([prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [long-running harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents))

### 2.5 Independent verification tiers

| Tier | When | How |
|---|---|---|
| T0: Automated gates | Always | Tests, build, lint, schema validation, link checker, and a spell or format check, run by script or hook |
| T1: Manager review | Every deliverable | Fresh-context rubric review |
| T2: Independent verifier | High-stakes work (money, external publication, production code, irreversible actions) | A separate agent, ideally a different model, that tries to refute the result. For factual claims, verify against sources. For code, use end-to-end tests as a user would (browser automation beat unit tests plus curl in [Anthropic's harness work](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)). |
| T3: Voting | Uncertain judgments with a discrete answer | Run 3-5 independent samples and take the majority. ([More Agents](https://arxiv.org/abs/2402.05120)) |
| T4: Human | Irreversible or customer-facing launches | Spot-check and sign off |

---

## 3. "Only do what's sure to work" vs. controlled experiments

Use two lanes, and make every task declare which lane it's in.

### Lane A: Production (proven methods only)

- Use only playbook procedures that have passed evals or a prior experiment.
- Every output passes T0 and T1 gates. Irreversible actions need T2 or T4.
- No novel tools, models or prompts without a graduated experiment.
- Prefer the simplest pattern that works. "Add complexity only when it demonstrably improves results." ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents))

### Lane B: Experiments (small, cheap, measurable, killable)

Every experiment needs a one-page card **before** it starts:

```
EXPERIMENT CARD
ID / owner / venture:
Hypothesis: If we <change>, then <metric> improves by <X> because <reason>.
Baseline: current value of metric on <N> tasks (measured, not assumed).
Change: exactly one variable (prompt, model, tool, workflow step).
Sample: N >= 10-20 representative tasks (Anthropic started evals with ~20 queries;
        early changes often have large, detectable effects).
Budget cap: <tokens / $ / wall-clock>. Hard stop when hit.
Success criterion: metric >= baseline + X AND no regression on guard metrics.
Kill criteria: (any one) budget hit; metric worse than baseline after N/2 tasks;
               any must-pass gate regression; reviewer flags safety/quality issue.
Blast radius: sandbox / branch / non-customer-facing only.
Decision date:
Result: GRADUATE (merge into playbook) / ITERATE (one more run) / KILL (log why)
```

**Rules:**

- Change one variable at a time. Run the same task set for baseline and treatment.
- Measure consistency as well as peaks. Use pass@k when one success is enough, and pass^k when every run must succeed (75% per trial gives about 42% pass^3). ([Anthropic evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents))
- Include cases where the behavior should not occur, to avoid one-sided optimization. (same)
- Log killed experiments in `lab/experiments/killed/` with the reason. Negative results stop other ventures from re-running them.
- Graduation requires the Research Lab to merge the change into the playbook along with its eval cases.

---

## 4. Time and token efficiency

### 4.1 When to parallelize

Parallelize **independent, read-heavy, breadth-first** work: research across sources, analyzing separate files or markets, generating alternative candidates, and running independent checks. Anthropic's lead agent spins up 3-5 subagents in parallel, each using 3+ tools in parallel, cutting research time by up to 90%. ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system))

Do not parallelize **tightly coupled, write-heavy work with shared implicit decisions**, such as one codebase feature, one design system or one document voice. Parallel writers make conflicting choices. ([Cognition](https://cognition.com/blog/dont-build-multi-agents)) If you must, fix the shared decisions in the brief first (style guide, interfaces, file ownership), and give each writer an isolated git worktree. ([subagents `isolation: worktree`](https://code.claude.com/docs/en/sub-agents))

Anthropic itself notes that multi-agent systems suit high-value, parallelizable work, and that coding is a weaker fit. ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system))

**Effort-scaling rule for managers** (adapted from Anthropic):

| Task type | Workers | Tool calls each |
|---|---|---|
| Simple lookup or fix | 0-1 (do it directly) | 3-10 |
| Comparison or moderate build | 2-3 | 10-15 |
| Broad research or multi-part build | 3-4 | as needed, with a budget cap |

Prompts should also damp over-delegation: "For simple tasks, sequential operations, single-file edits, or tasks where you need to maintain context across steps, work directly rather than delegating." ([prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices))

### 4.2 Model choice per role

Current lineup and list prices per million tokens (input/output), per [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview):

| Model | Price (in/out) | Use for |
|---|---|---|
| Fable 5.1 | $10 / $50 | Rare: hardest reasoning or long-horizon work where evals on Opus fall short |
| Opus 5.5 | $4 / $20 | CEO orchestrator, venture managers, final reviewers and verifiers, complex coding |
| Sonnet 5.5 | $2 / $10 | Most workers: research, drafting, standard coding, design implementation |
| Haiku 5.5 | from $0.10 / $0.50 | Classification, routing, extraction, link checks, formatting, search-heavy subtasks |

Batch API requests are 50% off, and prompt-cache reads cost 5-10% of the input price. Keep shared playbook prefixes stable so they cache.

Supporting evidence: a strong lead with cheaper workers beat a single strong agent ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system)). A model upgrade beat doubling the token budget (same). Anthropic recommends routing cheap work to Haiku via the agent's `model:` field ([subagents](https://code.claude.com/docs/en/sub-agents)). Test skills on every model that will run them, because Haiku may need more guidance than Opus ([skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

### 4.3 Avoiding redundant work

- **Detailed briefs with explicit boundaries** ("you cover X; Worker 2 covers Y; do not cover Z") are the fix Anthropic found for duplicated subagent work. ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system))
- **Check the shared knowledge base first.** Workers search `lab/findings/` and the venture playbook before researching. Findings are stored with date, source and confidence.
- **Pass references, not copies.** Pass file paths and links, and let agents load just-in-time. Return condensed summaries, not transcripts. ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents))
- **Write progress files and commit to git** so a resumed or replacement agent doesn't redo work: `progress.md`, a JSON feature or status list, and descriptive commits. ([long-running harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents))
- **Set budget caps** with `maxTurns` on agents, plus token budgets in briefs.
- **Restart instead of looping.** After two failed corrections, start a fresh context with a better brief. ([best practices](https://code.claude.com/docs/en/best-practices))
- **Don't over-verify.** Newer Opus models verify well on their own. Redundant "double-check everything" instructions add tokens and latency. ([prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)) Put verification in the gates, not in every prompt.

---

## 5. Templates

### 5.1 Worker brief template

```markdown
# BRIEF: <task-id> — <short title>
Venture: <name>    Manager: <agent>    Worker: <agent/model>    Lane: Production | Experiment <EXP-id>

## Objective (one sentence)
<What outcome, for whom, and why it matters.>

## Context you need (read these first; do not re-research)
- <path/to/playbook.md> sections: <...>
- <lab/findings/...> (existing research on this topic)
- Prior attempts / known pitfalls: <...>

## Scope
- IN: <exact deliverables>
- OUT: <explicitly excluded; other workers cover: Worker 2 = X, Worker 3 = Y>
- Fixed decisions (do not change): <interfaces, style guide, tone, stack, file ownership>

## Deliverable & format
- Path: <where to write output>
- Format: <template / schema / sections>; length: <limit>
- Return to manager: <=200-word summary + evidence list (not the full transcript)

## Acceptance criteria (the rubric you'll be scored on)
- Must-pass gates: <tests pass | builds | all claims cited | no TODOs | ...>
- Scored dimensions: see rubric v<N> (attached/linked)

## Verification you must run before submitting
- <command(s) / checks>; paste the command and output as evidence.

## Tools & sources
- Allowed: <tools>; Preferred sources: <primary docs, papers>; Avoid: <SEO farms, ...>

## Budget
- Max tool calls: <N>; max tokens/time: <...>; stop and report if blocked.

## Escalate immediately if
- Requirements conflict, a required input is missing, a test seems wrong, or an action is irreversible.
  (Do not work around broken tests; report them.)

## On completion
- Append one dated lesson to your MEMORY.md (what worked / what to avoid).
```

### 5.2 Manager review rubric (0-100)

The reviewer runs in a fresh context and sees only the brief, the deliverable and the evidence. It scores each check as Pass, Fail or Unknown, citing evidence for every Pass.

```markdown
# REVIEW: <task-id>  round <n>/5  reviewer: <agent/model>  rubric v<N>

## A. Must-pass gates (any FAIL => verdict REVISE regardless of score)
- [ ] G1 Meets the stated objective and every IN-scope deliverable exists
- [ ] G2 Automated checks pass (tests/build/lint/links) — evidence: <output>
- [ ] G3 No fabricated facts: every factual claim traceable to a cited source / code
- [ ] G4 No scope violations (nothing OUT-of-scope changed; fixed decisions respected)
- [ ] G5 No safety/irreversible-action issues

## B. Weighted dimensions (each 0 / 0.5 / 1 × weight; "Unknown" = 0 + note)
| # | Dimension | Weight | Binary checks (all must hold for 1; half for 0.5) | Score | Evidence |
|---|---|---|---|---|---|
| 1 | Correctness / accuracy | 30 | claims verified; edge cases handled; numbers reproduce | | |
| 2 | Completeness vs brief | 20 | every acceptance criterion addressed | | |
| 3 | Evidence & sourcing | 15 | primary/authoritative sources; citations accurate | | |
| 4 | Fitness for use | 15 | the audience can act on it without rework | | |
| 5 | Craft / style-guide conformance | 10 | follows style guide, template, naming | | |
| 6 | Efficiency | 10 | within budget; no redundant work; concise | | |
| | **Total** | **100** | | **__** | |

## C. Findings
- BLOCKING (must fix; tied to a gate or a dimension <0.5): 1) ... 2) ...
- OPTIONAL (do not trigger revision): ...

## D. Verdict
- ACCEPT (>=85, gates pass) | REVISE (gate fail or 70-84) | RE-BRIEF / ESCALATE (<70 at round 3,
  delta <5 vs last round, same blocking issue twice, or round 5)
- Score history: r1 __ r2 __ r3 __ r4 __ r5 __
- Playbook lesson to propose (if any): ...
```

Calibration protocol: every 20 reviews, a human (or a T2 verifier on a stronger model) re-grades 3 at random. Investigate if the disagreement exceeds 10 points or any gate verdict differs. Plant one canary defect per 10 reviews.

### 5.3 Research Lab improvement loop

The Research Lab owns the org's "training". It runs weekly or after every N completed tasks.

```
1. COLLECT   Pull from all ventures: review records (scores, blocking findings), killed/graduated
             experiments, worker MEMORY.md lessons, escalations, budget overruns.
2. CLUSTER   Group failures by MAST-style category: specification (bad brief), inter-agent
             misalignment (duplication, conflicting decisions), verification (premature stop,
             missed/incorrect check). Rank by frequency × cost.
3. HYPOTHESIZE  For the top 1-3 clusters, write an Experiment Card (one variable each):
             e.g., "Adding 3 worked examples to the market-sizing skill raises rubric dim-1
             from 0.6 to 0.8."
4. BUILD EVAL  Turn real failures into 10-20 eval tasks with reference solutions and
             pass/fail graders (include should-not-happen cases). Store in lab/evals/<skill>/.
5. BASELINE  Run current playbook on the eval set (≥3 trials for pass^k where consistency matters).
6. TREAT     Apply the minimal change (prompt line, example, checklist item, script, hook,
             model swap). Re-run the same eval set.
7. DECIDE    Graduate if success criterion met and no guard regression; else iterate once or kill.
8. SHIP      Graduated changes: PR to playbooks/ with eval cases + changelog entry; CEO/manager
             approves. Killed: log in lab/experiments/killed/ with reason.
9. PRUNE     Remove instructions the evals show are no longer needed (behavior holds without them);
             keep CLAUDE.md and SKILL.md lean (<500 lines).
10. REPORT   One-page digest to the CEO: what changed, measured effect, cost, next experiments.
```

### 5.4 Playbook file structure (git repo)

```
org-playbook/
├── CLAUDE.md                        # Org constitution: mission, definition of done, lanes,
│                                    # escalation rules, budget defaults (keep short)
├── .claude/
│   ├── agents/
│   │   ├── ceo.md                   # model: opus; tools: delegate/read; no direct edits
│   │   ├── venture-manager.md       # model: opus; skills: [briefing, reviewing]
│   │   ├── worker-researcher.md     # model: sonnet; read-only + web; memory: project
│   │   ├── worker-builder.md        # model: sonnet; edit+bash; isolation: worktree
│   │   ├── worker-utility.md        # model: haiku; extraction/formatting/link-check
│   │   ├── reviewer.md              # model: opus; read-only tools; fresh context
│   │   └── verifier.md              # different model/prompt from builder; refutation-oriented
│   ├── skills/
│   │   ├── writing-briefs/SKILL.md          # + templates/brief.md
│   │   ├── reviewing-deliverables/SKILL.md  # + rubrics/*.md, canaries/
│   │   ├── running-experiments/SKILL.md     # + templates/experiment-card.md
│   │   ├── researching-markets/SKILL.md     # + examples/, sources.md
│   │   ├── studio-design/SKILL.md           # + style-guide.md, examples/
│   │   └── studio-coding/SKILL.md           # + conventions.md, scripts/verify.sh
│   ├── agent-memory/<agent-name>/MEMORY.md  # per-agent lessons (git-shared, memory: project)
│   └── settings.json                # hooks: run tests on Stop, block writes to protected paths
├── ventures/
│   └── <venture-name>/
│       ├── CLAUDE.md                # venture-specific rules, goals, KPIs
│       ├── playbook.md              # promoted lessons for this venture
│       ├── briefs/<task-id>.md
│       ├── reviews/<task-id>-r<n>.md
│       ├── progress.md              # current state, next steps (for resumption)
│       └── status.json              # task list w/ pass/fail status (agents flip status only)
├── lab/
│   ├── findings/<topic>-<date>.md   # reusable research with sources + confidence
│   ├── evals/<skill>/               # tasks.jsonl, reference solutions, graders
│   ├── experiments/
│   │   ├── active/EXP-###.md
│   │   ├── graduated/
│   │   └── killed/                  # negative results, with reasons
│   └── digests/<yyyy-ww>.md
├── studio/
│   ├── design-system/               # tokens, components, brand voice, examples
│   └── code-standards/              # conventions, templates, CI scripts
├── rubrics/                         # versioned; frozen per task
│   └── default-v1.md
└── CHANGELOG.md                     # every playbook change: what, why, eval evidence
```

---

## 6. Operating rules (one-page summary for CLAUDE.md)

1. Every task has a written brief (template 5.1) with scope boundaries, acceptance criteria and a budget.
2. Scale effort to the task. Do simple things directly, and use at most 4 workers, only for independent subtasks.
3. Parallelize reading and research. Serialize coupled writing, or fix the shared decisions first.
4. Nothing counts as done without evidence from an executable check. Claims without evidence count as Unknown.
5. Reviews happen in a fresh context, against a frozen rubric, with gates first. Only blocking findings trigger revision.
6. Stop the loop when the score is 85 or higher, when it improves by less than 5 points, when the same issue recurs twice, or at round 5. After two failed revisions, re-brief fresh rather than patching.
7. Use a different model or prompt to verify high-stakes work. Use voting for uncertain discrete calls. Humans approve irreversible actions.
8. Production uses proven playbooks only. Anything new goes through an experiment card with kill criteria.
9. Each worker logs one lesson per task. The Research Lab promotes lessons with eval evidence and prunes stale ones.
10. Use Opus for orchestration and review, Sonnet for most work, and Haiku for mechanical subtasks. Keep shared prefixes stable for caching.

---

## Sources

- Anthropic, "How we built our multi-agent research system": https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic, "Building effective agents": https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, "Effective harnesses for long-running agents": https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic, "Equipping agents for the real world with Agent Skills": https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Code docs, Subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code docs, Best practices: https://code.claude.com/docs/en/best-practices
- Claude docs, Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Claude docs, Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude docs, Prompt engineering overview: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Claude docs, Models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024): https://arxiv.org/abs/2310.01798
- Madaan et al., "Self-Refine" (NeurIPS 2023): https://arxiv.org/abs/2303.17651 ; overview: https://www.alphaxiv.org/overview/2303.17651v2
- Shinn et al., "Reflexion" (NeurIPS 2023): https://arxiv.org/abs/2303.11366
- Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (NeurIPS 2025): https://arxiv.org/abs/2503.13657
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023): https://arxiv.org/abs/2306.05685
- Panickssery, Bowman, Feng, "LLM Evaluators Recognize and Favor Their Own Generations" (NeurIPS 2024): https://arxiv.org/abs/2404.13076
- Li et al., "More Agents Is All You Need" (TMLR 2024): https://arxiv.org/abs/2402.05120
- Cognition, "Don't Build Multi-Agents": https://cognition.com/blog/dont-build-multi-agents
- Simon Willison on Hamel Husain, "Using LLM-as-a-Judge" (Critique Shadowing, binary judgments): https://simonwillison.net/2024/Oct/30/llm-as-a-judge

**Notes on evidence strength:** The specific score thresholds (85/70, a delta below 5, a 5-round cap) are recommended operating defaults derived from the cited findings: diminishing returns after 2-3 refinement rounds, and restarting after two failed corrections. They are not measured constants, so tune them in the Research Lab. The "diminishing after 2-3 iterations" figure for Self-Refine comes from secondary summaries, not a direct read of the paper's figures.
