# Tools: Dual Mode Procedures

Honest limit, stated once and repeated wherever it matters: this skill is a file pack. It cannot click inside Figma, Figma Slides, Google Slides, Canva, or any other tool by itself. Two modes exist:

- **Connected mode:** the user's assistant has been set up with the tool's MCP server, API connector, or native integration by the user. In this mode the skill directs the assistant to read live data, and drafts writes for the user to approve.
- **Manual mode:** no connector. The user exports or pastes content, and the skill works from that. Manual mode always works and is the default assumption.

Every output must declare its mode and what was actually seen. Never imply live access that was not used. Standing rule for all tools: read freely, write only with the user's confirmation of the exact content. Nothing is sent to a client from any tool by this skill: no deck is shared, no proposal is delivered, and no PandaDoc document is issued without the user reviewing the final version and confirming that specific send.

Exact connector capabilities change as vendors update them. Verify current scope at setup time; the procedures below describe what to read and why, not a guarantee of a vendor's current API surface.

## Design and deck files (Figma and Figma Slides, Adobe Creative Cloud, Keynote and PowerPoint exports)

Tool-neutral by design: the procedure is the same whatever the studio builds decks and case files in. Figma is named where a step depends on a feature its connectors expose.

Purpose in this skill: pull proof from the studio's real files (past project frames for case pages, process artifacts, architecture diagrams), read client or team comments on a deck in progress, and inspect the structure of a deck file before it is presented.

Connected mode procedure:
1. Ask the assistant to list the file's pages and top level frames or slides. From the structure, identify the frames that carry the evidence the outline calls for: pack shots, before and after pairs, dielines, audit spreads, guideline pages.
2. Read unresolved comments on deck files. Summarise them by theme (argument disputes, missing proof, client questions). Comments on a sales deck are drafting data: a comment thread arguing about a claim is a signal the claim needs a source or needs to come out.
3. Where the connection exposes slide order and speaker notes (a Figma Slides file, for example), check the outline against the file: headline per page, notes present, cold-read pages marked. Report mismatches rather than silently reordering.
4. Record what was read: file name, date, which frames or slides were used as evidence.

Manual mode procedure:
1. Ask the user for: a PDF export of the deck or file, screenshots of the relevant frames, and any comment thread pasted as text (comments can be copied from the file).
2. Work from the export. Where the export flattens structure (hidden slides, notes, off-canvas drafts), say so in the output and mark the affected conclusions as assumptions. A PDF cannot prove a notes field is empty; say "not visible in export" rather than "missing".

What this feeds: case page visuals, the credentials imagery, the deck outline's visual column, and the version check (is this export the canonical version the cover email names).

Write actions: posting a comment, renaming a frame, reordering slides, or sharing the file are writes. Draft the change, show the user, execute only on confirmation. Sharing a file with a client address is a send and follows Standing rule 1: it never happens inside this skill without explicit confirmation of the final version and the recipient.

## Google Slides and Google Docs (deck and proposal production)

Purpose: most proposal documents live in Docs and most presented decks in Slides for studios on Google Workspace; the skill drafts content to land cleanly in both.

Connected mode procedure:
1. Where a Drive or Docs connector is set up, the skill may read the current draft document or deck: section order, headline text, and the tables carrying scope and price. It then checks the draft against the scope output (prices, quantities, exclusions) and the self-check, and reports differences as a list for the user.
2. Draft edits are proposed as exact replacement text in the conversation first. Only on the user's confirmation are they written to the document, one section at a time, so the user can see what changed.
3. Version discipline: before any write, the assistant states the document title and last-modified time it is looking at. If the user has a newer local version, stop; two editors on one proposal is how version chaos (edge case 4) starts.

Manual mode procedure:
1. The skill outputs the proposal as structured markdown with headings matching the template, or the deck as a page-by-page outline (headline, visual, speaker note, cold-read flag). The user pastes it into Docs or Slides.
2. Tables (scope, tiers, timeline) are output as clean markdown tables that paste into Docs without reformatting gymnastics, with figures copied exactly from the scope output.
3. The user returns a PDF export for the final check; the skill reads it for price drift, missing exclusions, and headline claims it cannot source.

What this feeds: the canonical proposal document, the presented deck, and the final pre-send check.

## Canva (one-pagers, credentials, social-proof assets)

Purpose: credentials one-pagers and simple leave-behinds are often built in Canva by smaller studios; the skill supplies exact content and checks the result.

Connected mode procedure:
1. Where a Canva connector exists, the skill may read the design's text content and page structure to verify the credentials one-pager against the library: names, project titles, permitted outcomes, dates.
2. Writes (editing text, swapping an image) are drafted and confirmed like every other write. Brand templates stay untouched unless the user names the copy to edit.

Manual mode procedure:
1. The skill outputs the one-pager as a text-complete layout brief: headline, blocks in order, the exact case lines with their permitted outcomes, contact block. The user or their designer drops it into the template.
2. The user exports a PDF or image; the skill checks it for claim drift (a number that grew in layout), missing flags, and last year's date left in a footer, which happens more than anyone admits.

What this feeds: the credentials one-pager and any single-page leave-behind. Canva is never the home of the canonical proposal; a sales document that only exists as a design file cannot be version-checked properly, and the skill says so when it sees it.

## PandaDoc (proposal delivery and signature tracking)

Purpose: studios often deliver the proposal and collect acceptance through PandaDoc. This skill treats PandaDoc as a delivery envelope, never as the drafting tool and never as an autopilot.

Procedure, both modes:
1. The skill produces the final proposal text from the template, checked against the scope output and the self-check. All [TO CONFIRM] items must be resolved or explicitly accepted by the user before a document is prepared; a document with silent gaps is never prepared for sending.
2. Connected mode: where a connector exists, the skill may prepare a draft inside PandaDoc from the studio's template and report its status (draft created, not sent). Preparing a draft is a write: the final text is shown to the user first and the draft is created only on confirmation.
3. Hard rule: the skill never sends a PandaDoc document, never triggers a signing or approval flow, and never marks anything as sent, without the user's explicit approval of that specific document, that specific recipient list, and that specific send. No standing approvals, no "send it like last time".
4. Manual mode: the skill outputs the proposal as a clean document plus a field checklist for the user to map into their PandaDoc template (fee table, milestones, recipient roles, expiry date), and the user sends it themselves.
5. Tracking: where the connector exposes status (viewed, completed), the skill may read and summarise it for the user. A "viewed" event is data for the follow-up rhythm, not a trigger for this skill to act on its own.

## Notion (deal rooms and case library)

Purpose: many studios keep the case library and per-deal rooms in Notion; it is this skill's most common evidence source and its filing cabinet.

Connected mode procedure:
1. Read the case library pages the user names: for each case, the problem, the work, the deliverables, and the permission note (named use, anonymised use, outcome citation allowed or not). The permission note governs; if a page has no permission note, the case is treated as imagery-only with no name and no outcome until the user confirms the position.
2. Read the deal room for the live proposal: discovery notes, the scope output, prior versions. Check the draft against the room's scope page, not against a copy pasted three weeks ago.
3. Draft updates (filing the final proposal version, logging the version sent and to whom, recording the decision date) are written only on the user's confirmation, and the entry states the canonical version filename so future readers can find the real one.

Manual mode procedure:
1. The user pastes or exports the library entries and deal room pages as text or markdown.
2. The skill works from the paste and says so; permission notes missing from a paste are treated exactly as in connected mode: absent note, restricted use.

What this feeds: case selection, permission checks (self-check 4), version logging, and the assumptions list.

## Mode declaration (required footer on tool-assisted outputs)

Any output built with tool access ends with a footer in this shape:

```
Mode: Connected (Figma, Notion) / Manual for the rest.
Seen: [file names, document titles, dates, and what was read from each].
Not seen: [anything the output assumes but could not access].
Writes: none / [each write made, with the user's confirmation noted].
```

If the footer cannot be completed honestly, the output is not ready.
