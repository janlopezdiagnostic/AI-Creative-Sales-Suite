# AI Skills for Non-Tech Trades

Reusable AI skills for people who run real-world businesses, not software.

Most AI "skills," prompt packs, and assistant playbooks are built for coders and marketers. Very few are written for the operators who could save the most time with AI, contractors, Airbnb hosts, wedding planners, realtors, teachers, restaurant owners, photographers, and the ones that exist are usually generic prompt lists, not trade playbooks. This repo is that playbook, one skill at a time.

## What is a skill here?

A skill is a folder of plain files that turns a general AI assistant (ChatGPT, Claude, Gemini) into a trade-specific one:

- `SKILL.md` - the standing instructions: the job, the step-by-step workflows, the guardrails, the output format. It starts with a **fact sheet you fill in once** (your business, your rates, your rules), so every output is specific to *your* business instead of generic.
- `examples/` - a realistic messy input and the finished output, so you can see the result before you trust it.

Outputs mark anything the AI did not actually know as `[TO CONFIRM]`. That tag means: check and fill this in before you send anything.

You are not paying for prompts. You are paying for the trade judgment written into the files: the exclusions a contractor forgets, the buffer math a planner does in her head, the platform policy triggers a host has learned the hard way.

## Starter skills (free, lite versions)

| Skill | The job it does | Status |
|---|---|---|
| [Contractor Bid](skills/contractor-bid/) | Rough site notes or a voice memo in, a professional itemized proposal out, with scope exclusions and change-order language | Lite v0.1 |
| [Airbnb Host](skills/airbnb-host/) | Guest messages, review replies, and damage-claim drafts that cite your own house rules and listing facts instead of accidentally admitting fault | Lite v0.1 |
| [Wedding Planner](skills/wedding-planner/) | A client intake in, a minute-by-minute run-of-show with realistic buffers out, plus per-vendor briefs | Lite v0.1 |

More industries are scored in [ideas/BACKLOG.md](ideas/BACKLOG.md).

## How to use a skill (60 seconds)

1. Open the skill's `SKILL.md` (use the "Raw" view on GitHub) and copy the whole file into a notes app or text box you can edit.
2. Fill in the **Setup (once)** lines at the top with your own details (your business, your rates, your rules) *before* you paste anything into the AI. This filled-in version is your personal copy; keep it.
3. Open your AI assistant (ChatGPT, Claude, or Gemini), start a Project, custom GPT, Gem, or a fresh conversation for your trade, and paste your filled-in file as the instructions or first message. Some of these features need a paid plan or a desktop browser.
4. In the next message, run one of the workflows from the file with your real input: a voice memo transcript, a guest message, a client intake.

No code. No install. Works from a phone.

## Free vs. paid

This repo is the free, lite layer: the core skill, one hero example per trade, plain markdown.

The paid **Pro Pack** (planned, $39-59 for the first three trades, Etsy + Gumroad) adds depth over the lite versions in this repo:

- The full prompt library (8-12 per trade, including the awkward ones: full change-order and follow-up sequences, angry clients, edge cases)
- The full guardrail libraries (exclusion clauses by trade, policy citation sets, complete buffer tables), where the lite version carries a starter set
- Ready-to-use formats: printable PDFs, Google Docs / Notion versions, phone shortcuts
- A 2-page visual setup guide and a short walkthrough video
- 1-2 update passes per year when platforms or rules change

See [PRODUCT_PLAN.md](PRODUCT_PLAN.md) for pricing, the under-$200 validation test, and the kill criteria.

## Ground rules baked into every skill

- **Drafting aid, not advice.** Nothing here is legal, tax, medical, or financial advice. Contract and negotiation outputs are drafts to review, not documents to sign blind.
- **No invented facts.** A skill must ask for missing inputs or mark them `[TO CONFIRM]` instead of hallucinating prices, dates, or policy.
- **Human sends it.** Skills draft; the operator reviews and sends. Nothing auto-sends to a client, guest, or platform.

## License

The lite skills in this repo are MIT licensed (see `LICENSE`). Use them, adapt them, share them. The Pro Pack libraries are a separate commercial product.

## Contributing

Run a trade we have not covered? Open an issue with: the recurring job that eats your time, a real (anonymized) example input, and what a good output looks like. The backlog is ranked by pain, willingness to pay, and how well the job demos in 60 seconds.
