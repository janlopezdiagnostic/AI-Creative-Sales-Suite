# Start Here

Read this page first. It takes about five minutes. You do not need to read anything else in this folder before you start, and you never need to read the long files at all. They are written for the AI, not for you.

## Get the files (2 minutes)

On the GitHub page, click the green **Code** button, then **Download ZIP**. Unzip it anywhere you can find again. That folder is the suite. If someone sent you a release link instead, download the file called `creative-sales-suite-full.zip` and unzip that. You never need a GitHub account, and there is nothing to install.

## Try it first, with a sample studio (5 minutes)

Before you fill in anything of your own, see it work once. Open `start-here/sample-studio-fact-sheet.md` (a finished fact sheet for a fictional studio, Hartwell Studio), upload it with the core files of the Scope and Pricing Architect skill (see Step 2 for what the core files are), and say: "Price a packaging redesign for 8 SKUs in 2 families, in three options, using only the rates on this fact sheet." Watch for the `[TO CONFIRM]` marks: that is the suite refusing to invent numbers it was not given. When you are ready, do the same job with your own studio below.

## The problem this solves

General AI tools write sales work the way software is sold. They do not know how creative work is actually bought and priced, so their drafts miss the things that decide your margin: how many rounds of revisions are included, what happens when the client adds products, who owns the final files, and how photography and design usage is paid for. You end up rewriting the draft, or worse, sending it and giving away free work.

## What this is, in plain words

The Creative Sales Suite is a set of instruction files for the AI assistant you already use (Claude, ChatGPT, or Gemini). Each file teaches the assistant one selling job, the way an experienced creative studio salesperson would do it: researching a client before a pitch, pricing a project without guessing, answering "that is too expensive," and turning a finished project into ongoing work.

The assistant works from your studio's real information: your portfolio, your prices, your standard terms. Where something is missing, it is instructed to mark the gap instead of making it up. It drafts. You check and you send. Nothing goes to a client without you.

## Start in three steps (about 20 to 30 minutes, once)

**Step 1: Tell it about your studio, once.**
Open the fact sheet template (`start-here/fact-sheet-template.md`, right next to the sample) and fill it in: what you do, your best work, your typical project sizes, what you do not do. Short answers are fine, and "unknown" is a fine answer. Not sure how to fill it in? Open `start-here/sample-studio-fact-sheet.md` to see a finished one, or paste the blank sheet into a chat and say: "Interview me one question at a time and fill this in for me."

**Step 2: Add the files to your AI assistant.**
First, a word about the files: the .md ending just means a text file. You never need to open or edit them; your assistant reads them as they are.
If your assistant has projects (Claude Projects, ChatGPT projects), create one called "Sales Suite" and upload: your filled-in fact sheet, the industry file for your world from the `verticals` folder, and the **core files** of the skill you need today. The core files are the ones in the skill's folder named `SKILL.md`, `playbook.md`, `decision-trees.md`, and `self-check.md`, plus everything in its `templates` folder. That is 10 files, and they are the set the skill is tested with (see `validation/lean-vs-full-test.md` if you want the receipts). The other files in the folder (the worked examples, edge cases, evals, and tools notes) are reference material: you do not need them for a normal job. One exception: if you are pricing a job, add the skill's `examples` folder too. The examples calibrate how much work the assistant estimates; in the one recorded bundle test that changed the totals a lot, and the receipts are in `validation/lean-vs-full-test.md`. No projects? A normal chat works too: paste the same files into the chat.

**Step 3: Ask for the job you need, in your own words.**
Use the starter sentences in `start-here/starter-prompts.md`. For example: "Research this brand and tell me if they are worth pitching, and why." Then paste whatever you have: a client email, your call notes, a price list. Messy is fine. That is what the files are built for.

## Pick the job, not the file name

| What you need today | Use this skill |
|---|---|
| Know if a brand is worth pitching | Account Research Brief |
| Write a first email that fits that client | Portfolio-Matched Outreach |
| Prepare for a first call, or make sense of one | Discovery Call Kit |
| Turn your notes into a proposal or deck outline | Proposal and Deck Builder |
| Price a project without guessing or giving work away | Scope and Pricing Architect |
| Answer "too expensive," a discount demand, or procurement | Objection and Procurement Desk |
| Turn a finished project into monthly ongoing work | Project-to-Retainer Converter |
| Restart a stalled deal, or ask a happy client for an introduction | Revive and Referral |

## Two ways to work with your other tools

**The simple way (start here).** Copy and paste. Export a page list from your design app, paste the client email, drop in your price list as a file. Every skill works fully this way, and for most studios it is all they ever need.

**The connected way (optional, later).** If your assistant is connected to the tools you already use (your client tracker, your documents, your design app), the skills can read from them directly, for example counting the pages in a design file instead of you listing them. This is a bonus for studios with someone technical to set it up. It is never required, and the guide for it lives in `setup-guides/` for when you want it.

## Words we use, translated

- **Skill:** one instruction file that teaches the assistant one job.
- **Industry file** (the `verticals` folder): a short add-on with your industry's buyers, calendar, and pricing habits. Packaging, brand and product design, fashion, agencies.
- **Fact sheet:** the one page about your studio from Step 1. The assistant reads it every time so it stops talking about some generic studio.
- **`[TO CONFIRM]`:** the assistant's way of saying "this is your decision or your number, I will not guess it." You will see it on prices and terms you have not given it.
- **`[UNVERIFIED]`:** "I could not check this." Mostly in research. Treat it as a question, not a fact.
- **CRM:** the tool where you track clients and deals, if you use one (HubSpot and Pipedrive are CRMs). You do not need one to use this suite.

## Three honest limits

1. Research is only as live as your assistant. If it cannot browse the web in the plan you are on, it can only work from what you paste in, and it is instructed to say so.
2. The assistant follows these instructions carefully, but it can still make mistakes. The files are built to show their working and flag gaps so checking is fast. Always read a draft before it goes to a client.
3. Template contract wording is a starting draft for your own adviser to review, not legal advice.

## If you get stuck

Do not read the long files to fix it. Start a fresh chat, upload the fact sheet and the skill's core files again (the set in Step 2, not just SKILL.md on its own), and use the exact starter sentence from `start-here/starter-prompts.md`. Usually, that is the whole fix.

## A quick privacy note

You will paste client material into an AI assistant: emails, call notes, your rates. Before you paste, take out anything the client would not want in a third-party tool: personal phone numbers, private addresses, passwords or access details, and anything covered by an NDA you have signed. Client names and project details are usually fine, but when in doubt, replace a name with a role ("the brand director") and keep the real name in your own notes. The suite never asks for credentials and never sends anything anywhere; it drafts, and you send.

## If it does not work, or it helped

Open an issue on the GitHub repo with the job you tried, the assistant you used, and what went wrong (or right). Improvements people share get folded into new releases, and the suite stays free.
