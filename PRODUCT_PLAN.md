# Creative Sales Suite: Product Plan

Internal. This repo stays private while this file lives in it: it contains pricing logic, margins, and kill criteria. Before any public release, this file moves out and paid-tier skills move to the paid download.

Approved direction (Oct 24, 2026): refactor from the v1 non-tech trades pack (archived in `archive/v1-trades/`) to a B2B sales AI suite for creative services. Beachhead vertical: **packaging**. Binding constraints from the approved proposal: the depth standard and dual-mode tooling spec are ship criteria, not aspirations; no bespoke/done-for-you tier; files only, under 3 hrs/week ongoing.

## Buyer

Sales executives, account executives, founders doing their own selling, and biz-dev leads at creative services firms: packaging studios first, then brand/product design, fashion studios, agencies. The sweet spot is 5-25 person studios where one person sells and bad scoping or a lost pitch is a real financial event.

Why they pay B2B prices: the suite prices against one won project ($15k-100k+) and against margin saved on one badly scoped job, not against a $39 template.

## Product shape

- 8 core skills covering the full sales cycle (research, outreach, discovery, proposal/deck, scope/pricing, objections/procurement, retainer conversion, revive/referral).
- Vertical layers: one context file per industry, loaded with the core skill. Packaging first; brand & product design second; fashion third; agencies as the widest layer last.
- Every paid skill ships as a module meeting the depth standard: SKILL.md, playbook.md (3,000-5,000 words), decision-trees.md (3-5 trees), examples/ (8-12 worked cases incl. failures recovered), templates/ (6-10), edge-cases.md (15-40), tools.md (dual-mode), self-check.md (10-15 checks), evals.md (20+ tests).
- Quality gate before any skill counts as done: structural lint, eval runs on 2+ assistants at 90%+ with zero invented-fact failures, blind stress test on messy inputs, practitioner review at 4/5 or better, tool test in both connected and manual mode with the date recorded.
- Setup guides: one runbook per major tool (Figma first), plus an environment matrix (Claude, ChatGPT, Cursor, Gemini).

## Pricing (one-time, files + update rights)

| Tier | Price | Contents |
|---|---|---|
| Free | $0 | Skill 1 + packaging layer in the public repo (at launch) |
| Solo / Founder | $179 | All 8 core skills, 1 vertical layer |
| Studio | $449 | All layers, team setup guide, proposal + SOW template library, 12 months of updates, up to 5 seats |
| Agency License | $990 | Up to 15 seats, 2 update passes/year |

Net per sale (Gumroad, 10% + $0.50 approx): Solo ~$160.60, Studio ~$403.60, Agency ~$890.50. Exact fees verified at listing time.

No bespoke calibration tier at launch (coworker disagreement resolved against it: it is service work and breaks the 3 hrs/week cap).

## Channels

B2B buyers do not browse Etsy. Channels are: LinkedIn outreach to studio founders and biz-dev leads, teardown content (before/after scope reviews and outreach rewrites), the free GitHub repo as the credibility asset, and a Gumroad storefront plus a one-page site (Carrd) for the paid tiers. Coach/consultant partnerships (agency new-business coaches) are a later affiliate channel.

## Quality gate status (honest, updated Oct 24, 2026)

For Skills 1 and 5 as built: structural lint passed (file trees and counts verified programmatically); example arithmetic independently recomputed by two reviewers (Claude and Gemini), errors found and fixed; consistency pass across README, plan, vertical layer, and skills completed. Still outstanding, and required before either skill is sold as paid: (a) the 20-case eval run on 2+ assistants with the pass bar met, (b) practitioner review at 4/5 or better, (c) tool tests in connected mode on live accounts. Until those three are done the skills are validation builds, not shippable paid product, and the README's table says so.

## Validation plan (current phase)

Build order approved in the proposal: archive v1 (done), rewrite README + this plan (done), build Skills 1 and 5 to the full depth standard with the packaging layer, coworker verification (Claude Opus + Gemini) on both, landing page copy, then outreach.

- Outreach: 25-40 personal LinkedIn messages/week to founders and biz-dev leads at 5-25 person packaging/brand studios, offering a free teardown (their last cold email, or a scope review on a live brief) for 15-20 minutes of feedback.
- Budget: $60-80 (landing page/domain, maybe one month of LinkedIn Premium). $100+ of the $200 cap stays in reserve. No ads.
- **Pass:** 10+ feedback calls AND (5 paid pre-orders at Solo pricing OR 2 studios asking about the Agency License).
- **Kill:** fewer than 3 pre-orders after ~120 outreach messages. Switch the vertical layer once (brand design), or stop.
- Only after the pass gate: build Skills 2, 3, 4, 6, 7, 8 and the second vertical layer.

## The practitioner problem (biggest open risk)

The quality gate requires a working creative-services seller to review the files at 4/5 or better, and the owner has no network in this industry yet. Recruitment path: the validation outreach itself (teardown calls are the audition), plus coach communities. Until a practitioner has reviewed a skill, it is labelled "pre-practitioner review" internally and does not ship as paid. If no practitioner can be recruited during validation, that is itself a kill signal for the paid launch; the free skill can still live as a portfolio asset.

## Explicitly not building

- No SaaS, no app, no CRM of our own, no browser extension.
- No automated sending: skills draft, the human approves and sends. No LinkedIn scraping (no open API; manual mode only, by design).
- No legal advice: contract language in templates is drafting aid, flagged for counsel review.
- No guaranteed-results claims anywhere in copy. No invented case studies, testimonials, or revenue numbers in the skills or the marketing.
