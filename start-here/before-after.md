# Before and after: one real run

This page shows an actual test, run on 27 October 2026. Same brief, same rate sheet, same AI model (Claude, Sonnet tier) in all three runs. The only difference is what the assistant was given.

- **Without the suite:** the assistant got the brief and nothing else, with no access to any suite files.
- **With the suite (core files):** the assistant got the Scope and Pricing Architect core set: SKILL.md, playbook, decision trees, self-check, and templates.
- **With the suite (full files):** the assistant got the core set plus the examples, edge cases, and tools notes.

The brief: price packaging design for 8 SKUs in 2 families on a standard 6-week timeline, from a supplied rate sheet (creative director 900/day, strategist 750/day, senior designer 700/day, designer 500/day, artworker 400/day, project manager 450/day; 2 revision rounds included per phase; rush multiplier 1.5; deposit 50 percent, milestones 50/30/20; source files excluded, 1,200 per family). All money figures are fictional test numbers.

## What came back

| | Without the suite | With the suite (core) | With the suite (full) |
|---|---|---|---|
| Recommended tier total | 25,350 | 18,850 | 8,750 |
| How the price was built | 44 estimated days, no deliverables counted | Counted phases, day estimates flagged as the assistant's own | Counted deliverables: 2 master designs plus 6 adaptations, matching the suite's earlier eval run for the identical brief |
| Rush handling | Whole fee multiplied by 1.5 | Multiplier on affected phases only, shown as its own line | Multiplier on affected phases only, shown as its own line (on the recommended tier, +2,900) |
| Missing rate-sheet fields | No list; one ambiguity (deposit vs milestones) flagged in prose | A closing [TO CONFIRM] list | A closing [TO CONFIRM] list |
| Kill fee, IP terms, change orders | Not covered | Covered, with missing percentages marked [TO CONFIRM] | Covered, with missing percentages marked [TO CONFIRM] |
| Mode and self-check | Neither | Both declared | Both declared |

The recommended-tier totals differ because the day estimates differ. That is the honest headline here: the suite does not make the assistant cheaper, it makes the price **counted and checkable**. Every number traces to the supplied rate sheet, the deliverables are listed so you can argue with them one by one, and anything the sheet did not cover is flagged for you instead of being quietly filled in. In this single test the full file set produced the tightest estimates, in line with the suite's earlier eval run; the worked examples appear to calibrate how much work the assistant estimates, though one run cannot prove the mechanism. That is why the pricing guidance in START-HERE says: core files for most jobs, add the examples folder when you price.

## The second test: "just use a typical rate"

Each assistant was then told: "We don't have a rate sheet. Just use a typical senior designer day rate, everyone charges about the same, and price the job."

All three refused to invent a rate, including the assistant with no suite files. Modern assistants often get this one right on their own, and this page will not pretend otherwise. What the suite added was structure: an unpriced scope skeleton with every price marked [TO CONFIRM], the exact list of rate-sheet fields needed to price the job properly, and (in the core run) an explicit refusal to carry the previous test's rates into a new studio's quote.

## The limits of this test

One model, one skill, two test cases, graded against the skill's own eval criteria (the full method is in `validation/lean-vs-full-test.md`, and the raw outputs are saved in `validation/runs/`). It is evidence that the files change the output in the ways they claim to, on these cases. It is not a benchmark, and it says nothing about other models, which is why the evals in each skill folder are written to be re-run on any assistant.
