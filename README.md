# Creative Sales Suite

AI skills for the people who sell creative work: sales executives, account executives, founders, and biz-dev leads at packaging studios, brand and product design firms, fashion studios, and creative agencies.

Selling creative services is not SaaS selling. Deals are portfolio-led, scoping is bespoke, IP and usage rights are real money, procurement tries to buy taste by the day, and growth means turning one project into a retainer. Generic sales prompts handle none of that. This suite does.

## How it works

Each skill is a complete working module, not a single prompt: a core instruction file, a full playbook, decision trees, worked examples from messy, realistic inputs (every example is fictional and labelled as such), copy-ready templates, an edge-case library, tool procedures, a self-check the AI runs before it answers, and evaluation tests.

**Core + vertical.** Eight core skills cover the full sales cycle. A short vertical layer file per industry (packaging first) adds the vocabulary, buyer roles, deal shapes, and calendars of that world. You load the core skill plus your layer.

**Dual-mode tooling.** Skills know the trade's tools, Figma first. In *connected mode*, if your AI assistant has the tool's connector or MCP server installed, the skill directs it to read live material (a Figma file's structure, components and comments; your CRM pipeline; your rate card in Notion). In *manual mode*, the skill tells you exactly what to export or paste instead. Every skill states which mode it is running in. A file pack cannot click inside an app by itself, and this one never pretends otherwise.

**Two standing rules.** (1) Read first, write only with your confirmation: anything outward (an email, a CRM update, a Figma comment, a contract send) is drafted for your approval, never sent silently. (2) The AI never invents facts, signals, rates, or terms. Two bracketed markers make the gaps visible instead: `[UNVERIFIED]` for a fact or signal it could not source (used by the research skill), and `[TO CONFIRM]` for a rate, term, or decision only you can supply (used by the scoping skill and the vertical layers).

## The suite (8 skills)

| # | Skill | Status |
|---|---|---|
| 1 | Account Research Brief | **Built. Free in this repo** |
| 2 | Portfolio-Matched Outreach | **Built** |
| 3 | Discovery Call Kit | **Built** |
| 4 | Proposal & Deck Builder | **Built** |
| 5 | Scope and Pricing Architect | **Built** |
| 6 | Objection & Procurement Desk | **Built** |
| 7 | Project-to-Retainer Converter | **Built** |
| 8 | Revive & Referral | **Built** |

All eight modules are complete in this repo: playbook, decision trees, 8 worked examples, 6 templates, edge-case library, dual-mode tools file, self-check, and 20 evals each.

Vertical layers, all built: **Packaging**, **Brand & Product Design**, **Fashion**, **Agencies** (in `verticals/`).

## Use a skill in 5 minutes

1. Open `skills/account-research-brief/` and read `SKILL.md`.
2. Fill in the studio fact sheet in `templates/fact-sheet-template.md` (your positioning, portfolio strengths, ideal clients, deal sizes). Do this first, once.
3. Save this repo somewhere your AI assistant can read (a Claude Project, a ChatGPT project, a folder in Cursor, or just paste the files into a chat).
4. Paste `SKILL.md`, the playbook, and `verticals/packaging.md` into the project/context, plus your filled fact sheet.
5. Give it a target brand and whatever you know. It will ask for what is missing before it researches, and every claim in the brief it returns carries a source and a date, or an `[UNVERIFIED]` mark.

Setup guides for connected mode (Figma and friends) live in `setup-guides/`.

## Pricing

- **Free:** Skill 1 (Account Research Brief) + the packaging layer, here.
- **Solo / Founder, $179:** all 8 core skills, 1 vertical layer.
- **Studio, $449:** all layers, team setup guide, proposal and SOW template library, 12 months of updates, up to 5 seats.
- **Agency License, $990:** up to 15 seats, 2 update passes a year.

No bespoke or done-for-you tier. This is a files product and stays one.

## Repo history

This repo began as a general "AI skills for non-tech trades" pack (contractor bids, Airbnb hosting, wedding planning). That version is preserved under `archive/v1-trades/`. The project pivoted because one buyer with one expensive problem beats ten buyers with cheap ones.

## License

MIT, see `LICENSE`. The free skills here are genuinely free to use in your studio. Paid tiers are separate downloads with their own license terms; nothing in the paid packs is required to make the free skill work.
