# Creative Sales Suite: Product Plan

Internal. This repo stays private while this file lives in it: it contains pricing logic, margins, and kill criteria. Before any public release, this file moves out and paid-tier skills move to the paid download.

Approved direction (Oct 24, 2026): refactor from the v1 non-tech trades pack (archive removed Oct 24, 2026 at the owner's direction) to a B2B sales AI suite for creative services. Beachhead vertical: **packaging**. Binding constraints from the approved proposal: the depth standard and dual-mode tooling spec are ship criteria, not aspirations; no bespoke/done-for-you tier; files only, under 3 hrs/week ongoing.

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

## The problem and the solution, in the customer's words

Problem (one sentence): General AI tools write sales work the way software is sold, so creative studios get drafts that miss how creative work is bought and priced, and they rewrite them or send them and give away free work.

Solution (one sentence): The Creative Sales Suite is a set of instruction files for the AI assistant the buyer already uses, teaching it each selling job the way an experienced creative studio salesperson does it, from the studio's own portfolio, prices, and terms.

This wording governs customer-facing copy. The internal architecture vocabulary (modules, core + vertical, dual-mode, evals) does not appear on the landing page or in the start-here path.

## Non-technical by design (standing rules)

The primary customer is a founder or sales lead who is expert in clients and new to AI tools. Rules that follow from that:

- The first thing a buyer reads is START-HERE.md: five minutes, problem, solution, three steps. The long files are for the AI, never assigned as reading.
- Skills are introduced by the job ("Price a project without guessing"), with the formal skill name second.
- Every SKILL.md opens with a plain-English box: what it does, what to give the assistant, and one starter sentence to copy.
- The default way of working is copy and paste (manual mode). Tool connections (Figma, CRM) are an optional later extra, presented that way in all customer copy, never as the main path.
- The fact sheet is the only homework, it ships with a filled-in fictional sample, and a starter prompt lets the assistant interview the buyer to complete it.
- Claims are softened to what the files can honestly do: the assistant is instructed never to invent and to mark gaps; copy says drafts are checked by the buyer before anything reaches a client.

## Channels

B2B buyers do not browse Etsy. Channels are: LinkedIn outreach to studio founders and biz-dev leads, teardown content (before/after scope reviews and outreach rewrites), the free GitHub repo as the credibility asset, and a Gumroad storefront plus a one-page site (Carrd) for the paid tiers. Coach/consultant partnerships (agency new-business coaches) are a later affiliate channel.

## Build status (Oct 24, 2026)

The full suite is built: all 8 core skills as complete modules (168 files), all 4 vertical layers, setup guides including the Studio team guide, and landing copy. The owner directed a full build over the original 2-skill validation subset, and separately gave a blanket "approve all, stop asking" instruction for in-scope steps. Build order note: the validation outreach plan below still governs selling; the full build simply exists now.

## Quality gate status (honest, updated Oct 24, 2026)

Structural lint passed for all 8 modules (file trees and counts verified programmatically; 8 examples and 6 templates per skill; playbooks in range). For Skills 1 and 5: example arithmetic independently recomputed by two reviewers (Claude and Gemini), errors found and fixed; eval spot-runs completed (research 8/8 on a sampled set including all hostile cases; scope 10/12 with the 2 misses traced to defective test fixtures, which were fixed, and all 8 integrity cases passing). All 8 modules then received a full coworker verification pass. Still outstanding before paid launch, unchanged: (a) full 20-case eval runs per skill on 2+ assistants with the pass bar met, (b) practitioner review at 4/5 or better, (c) tool tests in connected mode on live accounts.

## Validation plan (current phase)

Build order as executed: archive v1 (done; archive later removed), README + this plan (done), all 8 skills to the full depth standard with all 4 vertical layers (done, owner directed the full build on Oct 24), coworker verification (Claude Opus + Gemini) across all modules (done), landing page copy (done). Next phase is outreach and the remaining gate items above.

- Outreach: 25-40 personal LinkedIn messages/week to founders and biz-dev leads at 5-25 person packaging/brand studios, offering a free teardown (their last cold email, or a scope review on a live brief) for 15-20 minutes of feedback.
- Budget: $60-80 (landing page/domain, maybe one month of LinkedIn Premium). $100+ of the $200 cap stays in reserve. No ads.
- **Pass:** 10+ feedback calls AND (5 paid pre-orders at Solo pricing OR 2 studios asking about the Agency License).
- **Kill:** fewer than 3 pre-orders after ~120 outreach messages. Switch the vertical layer once (brand design), or stop.
- Superseded Oct 24, 2026: the owner directed the full build (all skills, all layers) ahead of the pass gate, and it is done. The outreach validation above still governs selling and the paid launch decision.

## The practitioner problem (biggest open risk)

The quality gate requires a working creative-services seller to review the files at 4/5 or better, and the owner has no network in this industry yet. Recruitment path: the validation outreach itself (teardown calls are the audition), plus coach communities. Until a practitioner has reviewed a skill, it is labelled "pre-practitioner review" internally and does not ship as paid. If no practitioner can be recruited during validation, that is itself a kill signal for the paid launch; the free skill can still live as a portfolio asset.

## Explicitly not building

- No SaaS, no app, no CRM of our own, no browser extension.
- No automated sending: skills draft, the human approves and sends. No LinkedIn scraping (no open API; manual mode only, by design).
- No legal advice: contract language in templates is drafting aid, flagged for counsel review.
- No guaranteed-results claims anywhere in copy. No invented case studies, testimonials, or revenue numbers in the skills or the marketing.
