# Changelog

## v1.1.1, 27 October 2026

- Removed the personal email address from the README, START-HERE, and the website. Feedback runs through GitHub issues only.
- Removed all recruiting and outreach material (the testers-wanted discussion post and the ready-to-send invite and social posts). The suite grows organically or not at all; the validation kit stays, for recording sessions with anyone who finds it and offers.

## v1.1.0, 27 October 2026

- Releases with ZIPs: the full suite, a core and a full ZIP per skill, and a Claude Skills ZIP per skill, all built by `scripts/build_bundles.py`.
- Core upload set defined and tested: SKILL.md, playbook, decision trees, self-check, and templates (10 files). The test, its method, and its limits are recorded in `validation/lean-vs-full-test.md`. Pricing guidance adds the examples folder for estimate calibration.
- Every SKILL.md now carries standard Agent Skills frontmatter (name, description, license), so the skills can also be installed through Claude Skills upload on paid Claude plans.
- START-HERE: a download step, a try-it-first path using the sample studio, a privacy note, and a no-GitHub feedback route. The blank fact sheet template now also lives at `start-here/fact-sheet-template.md`.
- `start-here/before-after.md`: a real with-and-without test run, with its method and limits stated.
- Landing page published as a website (GitHub Pages, from `docs/`), with a social preview image.
- `validation/` folder: a kit for testing the suite with real first-time users (invite, observation checklist, feedback questions, quote consent).

## v1.0.0, 25 October 2026

- The whole suite made free under the MIT license: all 8 skills, all 4 industry files, the setup guides, and the templates. No tiers, no seat limits, no paid version.
