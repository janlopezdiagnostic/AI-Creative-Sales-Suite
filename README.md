# Creative Sales Suite

**Ready-made instruction files that teach your AI assistant to sell creative work properly.**

For the people who sell packaging, brand and product design, fashion, and agency work: sales executives, account executives, founders, and business development leads. You add the files to Claude, ChatGPT, or Gemini, and the assistant handles each selling job the way an experienced creative studio salesperson would, using your portfolio, your prices, and your terms.

New here? Read **[START-HERE.md](START-HERE.md)** first. Five minutes, plain English, no technical knowledge needed.

## Get it (2 minutes)

Download the ZIP from the [latest release](https://github.com/janlopezdiagnostic/AI-Creative-Sales-Suite/releases/latest) (`creative-sales-suite-full.zip`), or click the green **Code** button on this page and choose **Download ZIP**. Unzip it. That is the whole installation. No GitHub account, no code, nothing to install. Individual skills are also on the release page as their own smaller ZIPs, including a one-file-per-skill version for Claude users (see "Using these as Claude Skills" below).

**Want proof before you commit?** [See one real before-and-after run](start-here/before-after.md): the same pricing brief, the same AI model, with and without these files. And you can try the suite in 5 minutes with the sample studio in `start-here/`, before filling in anything of your own.

## Why I made this

I work in tech. My wife is a designer, and a lot of my friends work in creative fields.

Most of them barely use AI. Not because they are against it. They just have not found a good place to start, and most AI advice is written for other tech people.

This is a starting place. It covers the everyday parts of selling creative work (researching a client, writing the first email, pricing a project) as simple files you use with Claude, ChatGPT, or Gemini. No technical setup. Nothing new to install.

If you are not technical and you want AI to save you time on work like this, start here. It is free.

## The problem

General AI tools write sales work the way software is sold. They do not know how creative work is actually bought and priced, so their drafts:

- sound like they could be selling anything, to anyone
- miss the things that decide your margin: how many revision rounds are included, what happens when the client adds products or pages, who owns the final files, how photography and design usage is paid for
- quote prices with nothing underneath them, so the first discount demand has nowhere to go but down
- happily invent facts about a client, a case study result, or your own rates

So you rewrite the draft, or worse, you send it and give away free work.

## How this solves it

Each skill in the suite teaches the assistant one selling job, in depth, with the rules a senior salesperson follows without thinking:

- It works from **your** studio fact sheet, portfolio, and rate card, not a generic studio.
- It is instructed to **never invent** a fact, a client result, a price, or a term. Missing pieces are marked `[TO CONFIRM]` (your call to make) or `[UNVERIFIED]` (could not be checked), so you can see exactly what still needs you.
- It **drafts, you decide**. Nothing is emailed, posted, or sent anywhere by the assistant on its own.
- It is allowed to tell you **no**: no case study that fits means no outreach email; a client with no real reason to buy gets a "walk away" recommendation, not a pep talk.

## How it works (three steps)

1. **Tell it about your studio, once.** Fill in a one-page fact sheet (there is a filled-in sample in `start-here/`). About 15 minutes, one time.
2. **Add the files to your AI assistant.** Upload the fact sheet, your industry file, and the **core files** of the skill you need: `SKILL.md`, `playbook.md`, `decision-trees.md`, `self-check.md`, and everything in its `templates` folder (10 files; they are the tested set, see `validation/lean-vs-full-test.md`). The examples, edge cases, evals, and tools notes in the folder are reference, not required reading for the assistant. If you are pricing a job, add the `examples` folder too: in the recorded bundle test (`validation/lean-vs-full-test.md`), the examples kept the assistant's work estimates calibrated. No setup, no code, nothing to install.
3. **Ask for the job you need, in your own words.** "Research this brand." "Price this project." "The client says we are too expensive, help me reply." Starter sentences for every job are in `start-here/starter-prompts.md`.

## Pick the job you need

| What you need today | Skill |
|---|---|
| Know if a brand is worth pitching | Account Research Brief |
| Write a first email that fits that client | Portfolio-Matched Outreach |
| Prepare for a first call, or make sense of one | Discovery Call Kit |
| Turn your notes into a proposal or deck outline | Proposal and Deck Builder |
| Price a project without guessing or giving work away | Scope and Pricing Architect |
| Answer "too expensive," a discount demand, or procurement | Objection and Procurement Desk |
| Turn a finished project into monthly ongoing work | Project-to-Retainer Converter |
| Restart a stalled deal, or ask a happy client for an introduction | Revive and Referral |

Every skill comes with the same backup, all written for the AI rather than for you to study: a detailed playbook, worked examples that start from messy real-world inputs (all fictional, all labelled), ready-to-use templates, answers for unusual situations, a final self-check the assistant runs before it answers you, and test cases the files can be checked against.

**Industry files** (in `verticals/`) add your world's buyers, calendar, and pricing habits. All four are built: **Packaging**, **Brand and Product Design**, **Fashion**, **Agencies**.

## Your other tools: two ways to work

**The simple way is the normal way.** Copy and paste: the client email, your call notes, your price list, an exported list of pages from your design app. Every skill works fully this way.

**The connected way is an optional extra.** If your assistant is connected to the tools you already use (your CRM, your documents, your design app), the skills can read from them directly, for example reading your rate card from your documents or counting artwork files in a design file instead of you listing them. Studios with someone technical can set this up using the guide in `setup-guides/`. It is never required, and the suite never pretends a file can click inside an app by itself.

## Cost

Free. All of it.

All 8 skills, all 4 industry files, the setup guides, and the templates are in this repo, at no cost, with no tiers, no seat limits, and no paid version waiting behind it. If it helps you, the only thing I would ask is that you pass it on to someone else it could help.

## Honest limits

- Research is only as live as your assistant. If it cannot browse the web on your plan, it works from what you paste in, and it is instructed to say so.
- The assistant follows these instructions carefully, but it can still make mistakes. The files show their working and flag gaps so your check is fast. Always read a draft before it reaches a client.
- Template contract wording is a starting draft for your own adviser, not legal advice.

## Using these as Claude Skills (optional)

Each `SKILL.md` now carries the standard Agent Skills frontmatter (`name`, `description`, and `license`), so Claude users on a paid plan can also install a skill as a single ZIP: download `claude-skill-<skill-name>.zip` from the [latest release](https://github.com/janlopezdiagnostic/AI-Creative-Sales-Suite/releases/latest), then in Claude go to Settings, then Features, and upload it. This is a convenience for Claude users only. The plain upload route above works on free plans and on ChatGPT and Gemini too, and stays the normal way to use the suite.

## Feedback, without a GitHub account

If something does not work, or you improved a file, email itsjanlopez@gmail.com with the job you tried and the assistant you used. GitHub issues are open as well, but email is the front door. A short privacy note lives in START-HERE.md: what to take out of client material before you paste it into any AI tool.

## License

The whole suite is under the MIT license (see `LICENSE`). Use it in your studio, adapt it to your rates and your terms, and share it freely. Everything the skills help you produce (briefs, emails, proposals, scopes, replies) is yours.

Attribution is appreciated but not required beyond what the MIT license asks: keep the copyright and license notice in copies. If you improve a skill, consider sharing the improvement back so the next studio benefits too.
