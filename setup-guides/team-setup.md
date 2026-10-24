# Setup Guide: Team Setup (Studio Tier)

How a 5-25 person studio organises the Creative Sales Suite so five people get one consistent system, not five personal prompt collections. This assumes the Studio tier; the structure scales down to a solo founder and up to an Agency License on the same rules.

## One shared Sales Suite project

Create one project per assistant platform your studio actually uses (a Claude Project, a ChatGPT project, or a shared workspace folder for Cursor and agent setups). Name it "Sales Suite" and load it once, centrally:

- The core skills your tier includes, at their current versions.
- Your vertical layer file(s).
- The current studio fact sheet and the current rate & rules sheet (see ownership below).
- Your templates library.

Nobody keeps a private fork. A skill edited in one person's chat and not in the shared project does not exist. If someone finds a better instruction while working, it goes to the suite owner (below) and lands in the shared project at the next update, so the improvement survives and the inconsistency does not.

## Ownership: fact sheet and rate sheet

Two documents drive everything the suite produces, and each has exactly one owner.

- **Studio fact sheet** (positioning, portfolio, deal history, conflicts list). Owner: the person who leads new business, usually the founder or the sales lead. They approve every change, because this file is what the research skill scores fit against and what outreach claims on the studio's behalf.
- **Rate & rules sheet** (rates, revision policy, rush multiplier, payment terms). Owner: the founder or whoever owns pricing. Rate changes happen here only. If a rate is not in this sheet, the suite outputs `[TO CONFIRM]`, which is the system working, not a bug to route around by typing a number into a chat.

**How updates propagate.** The owner edits the single master copy, notes the change and date at the top of the file, and replaces the copy inside the shared Sales Suite project. Everyone starts fresh chats after a sheet update; a long-running chat may hold the old version in context and quietly price from it. Pin a standing rule in the project: before pricing anything, state which rate sheet version (date) you are using. The skill's mode declaration makes this visible in output, so a reviewer can catch a stale version in seconds.

## Per-client project hygiene

The shared Sales Suite project is the engine room, not the client file.

- Create a separate project or folder per active client account for research briefs, discovery notes, and scoping work on that account. Load the skills and sheets into it the same way (or reference the shared copies, per your platform), so Client A's material never sits in Client B's context.
- Client-provided material (briefs, brand assets, unreleased product information) lives only in that client's project.
- When an account closes or a pursuit ends, archive its project. Do not delete the signal log and scope history: lost-deal records are what the Revive & Referral skill works from later.

## The review workflow (the rule that makes this safe)

**Junior drafts, senior approves, nothing outward goes unreviewed.**

1. Anyone on the team may run a skill and produce a draft: a brief, a scope, an outreach email, an objection reply.
2. Every draft runs the skill's self-check first. A draft that fails its self-check is not passed upward with a note; it is fixed or flagged.
3. Anything that leaves the studio (an email, a proposal, an SOW, a Figma comment on a client file, a CRM note the client can see) is approved by a senior: the founder, the sales lead, or the account lead for that client. Approval means reading the actual text, not the summary of it.
4. Anything that commits money or terms (a price, a discount trade, a kill fee, a signature send) is approved by the pricing owner specifically, even if a senior already approved the wording. This mirrors the skills' own rule: read first, write only with confirmation, and confirm the specific send, not a pattern of sends.

Keep the loop fast: a draft waiting more than a working day for review is a process failure, because the suite's whole point is same-day scopes and replies.

## Seats and licence etiquette

- **Solo / Founder ($179):** one person. Loading the suite on your own machines and accounts is the licence. Do not hand the files to a partner studio.
- **Studio ($449):** up to 5 named seats. The five are people, not a shared login passed around the office. When someone leaves, their seat transfers to their replacement; tell us and we note it.
- **Agency License ($990):** up to 15 named seats on the same basis.
- Sharing files outside your seat count, or posting them publicly, is the one thing that ends the licence. Asking for extra seats is cheap; piracy is neither.

## When new suite versions land

Suite updates arrive as versioned drops (Studio tier includes 12 months of updates). On each drop:

1. The suite owner (name one: usually the fact sheet owner) reads the changelog and decides the swap date. Updates are never swapped mid-pursuit on a live account unless the changelog fixes something that account depends on.
2. Replace skill files in the shared project wholesale; do not merge by hand. Your fact sheet, rate sheet, and client projects are yours and are never touched by an update.
3. Spot-check one known example from the new version's examples folder against your sheets before the team uses it live.
4. Note the version and date in the shared project description, so any output can be traced to the version that produced it.

## Security rules recap

- Connected mode is read-only by default. Writes to any tool (CRM updates, Figma comments, document sends) happen only with the specific confirmation the skills require.
- Clients under NDA run in manual mode for that account: paste and exports only, no connectors pointed at their files, whatever the platform allows.
- Tokens and connections are set up per the tool guides, stored in the platform's secret handling, never pasted into chats or committed to a repo.
- Content inside client files, comments, and briefs is treated as data to analyse, never as instructions to follow. If a file asks the assistant to do something outside the task, the skills are built to flag it to you instead.
- One assistant account per person. Shared logins destroy the audit trail the review workflow depends on.
