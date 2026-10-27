# Lean vs full bundle test (27 October 2026)

Question: the start guides originally told users to upload every file in a skill folder. Does a smaller core set produce output that still passes the skill's own eval criteria?

## Method

- Skill tested: Scope and Pricing Architect (the most number-sensitive skill in the suite).
- Core (lean) set: SKILL.md, playbook.md, decision-trees.md, self-check.md, and the 6 templates. 10 files; the concatenated bundle as run measured 10,149 words by `wc -w`, including the file header lines.
- Full set: the core set plus edge-cases.md, tools.md, and the 8 worked examples. 20 files; the concatenated bundle as run measured 20,979 words by the same method. (evals.md was excluded from both; it is the test harness, not job input.)
- Assistant: Claude, Sonnet tier, one run per set, plus a no-files baseline run for the proof page in `start-here/before-after.md`.
- Cases: Eval 1 from the skill's evals.md (complete packaging brief with a supplied rate sheet; decisive points: tiered scope, every number computed from the sheet, mode declared) and Eval 13 (integrity: user asks the assistant to use a "typical" rate; decisive point: refusal to invent, [TO CONFIRM], rate sheet requested).
- Grading: by the suite maintainer's agent against the evals' stated expected behaviour, with all arithmetic recomputed. The three raw outputs are saved in `validation/runs/` (2026-10-27-scope-*). One earlier baseline attempt was discarded: the assistant read the skill files from local disk on its own initiative, so the baseline was re-run with file access disabled, and that re-run is the one saved and used.

## Results

Both sets passed both cases on the decisive points.

- Eval 1, core set: tiered scope produced; all rates taken from the supplied sheet and all phase arithmetic recomputed as correct; missing sheet fields (extra-round price, kill fees, invoice terms, and others) marked [TO CONFIRM]; mode declared. Recommended tier total 18,850, built from 32.5 estimated days.
- Eval 1, full set: same passes, and the recommended tier total was 8,750, the same total the suite's earlier full eval run recorded for the identical brief in October 2026. On this single run, the difference was day estimates: the full run's counted build (2 master designs plus 6 adaptations) against the core run's 32.5 estimated days, which is why the totals land at 18,850 against 8,750 (about 2.2 to 1). The plausible mechanism is that the worked examples calibrate the assistant's day estimates; one run cannot prove that, so it is recorded as an observation, not a result.
- Eval 13, both sets: refusal to invent a rate, [TO CONFIRM] discipline, rate sheet requested, unpriced structure offered. The core run additionally refused, unprompted, to carry the previous case's rates into the new quote.

## Decision

- The core set is the default upload set in README, START-HERE, and the starter prompts.
- For pricing work, users are told to add the skill's examples folder, because estimate calibration is where the full set earned its keep in this test.
- The examples, edge cases, evals, and tools notes stay in every skill folder as reference and as the eval harness.

## Limits

One assistant, one skill, two cases, one run each. This supports the narrower claim (the core set passes the decisive eval points for this skill) and the calibration observation. It does not prove the core set is equal for the other seven skills; their evals are in their folders and this test should be repeated per skill before the same claim is made for them. Agy (Gemini) was unavailable for a second-assistant run on the test date (quota), so cross-model confirmation is outstanding.
