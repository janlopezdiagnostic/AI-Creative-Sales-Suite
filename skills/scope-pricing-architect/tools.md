# Tools: Dual Mode Procedures

Honest limit, stated once and repeated wherever it matters: this skill is a file pack. It cannot click inside Figma, Adobe apps, or any other tool by itself. Two modes exist:

- **Connected mode:** the user's assistant has been set up with the tool's MCP server, API connector, or native integration by the user. In this mode the skill directs the assistant to read live data, and drafts writes for the user to approve.
- **Manual mode:** no connector. The user exports or pastes content, and the skill works from that. Manual mode always works and is the default assumption.

Every output must declare its mode and what was actually seen. Never imply live access that was not used. Standing rule for all tools: read freely, write only with the user's confirmation of the exact content. Nothing is sent to a client from any tool by this skill.

Exact connector capabilities change as vendors update them. Verify current scope at setup time; the procedures below describe what to read and why, not a guarantee of a vendor's current API surface.

## Design files (Figma, Adobe Creative Cloud, Affinity, Sketch)

Tool-neutral by design: this procedure is the same whatever the studio designs in. Figma is the worked example below because its connectors are the most common, not because the skill prefers it.

Purpose in this skill: count deliverables and judge complexity from the real files, not the client's summary of them.

Connected mode procedure:
1. Ask the assistant to list the file's pages and top level frames or sections. From the structure, build the deliverables count: design families, SKUs or variants visible, guideline pages.
2. Read component and variable/token usage where the connector exposes it. A file with a real component system implies different adaptation effort from a file of one off frames; note which you found, because it changes the artwork estimate.
3. Read unresolved comments. Summarise them by theme (direction disputes, content gaps, approval blockers). Comment threads are discovery data: unresolved direction disputes at comment level become scope assumptions and revision risks.
4. Record what was read: file name, date, page/frame counts used for the estimate.

Manual mode procedure:
1. Ask the user for: a PDF export of the relevant file or deck, screenshots of the page list or layers panel, and the comment thread pasted as text (comments can be copied out of most design tools).
2. Work from the export. Where the export hides structure (tokens, components), say so and mark the affected estimate lines as assumptions.

What this feeds: the deliverables inventory, the SKU count in the scope, the adaptation estimate, and the risk note on revisions.

Write actions: drafting a comment or a summary into the file is a write. Draft it, show the user, post only on confirmation.

## Adobe InDesign (packaging production complexity)

Purpose: judge production complexity of existing packaging, typically in a takeover, extension, or recovery job.

Manual mode is the expected mode. Ask the user for the InDesign package report (the text summary produced when a document is packaged: fonts, links, colour spaces, page and spread setup) and, where relevant, a PDF of the current pack.
From the report, read: number of placed images and their status, font count and licensing flags, colour build (process versus spot colours), and any missing link or font warnings. Each is a costing fact: spot colours and many linked files mean heavier artwork and proofing effort, which belongs in the scope and the assumptions.
Connected mode: where the user's setup exposes Creative Cloud file or library data through a connector, read asset metadata only, to confirm counts. There is no general substitute for the package report; if it is not provided, mark production complexity as [TO CONFIRM].

## Google Sheets (pricing models)

Purpose: hold the maths where the user can audit it.

Connected mode: where a Sheets connector is set up, the skill may populate a pricing model the user owns: phases as rows, roles and days against rate sheet rates, tier totals. Rules: rates are read from the user's rate sheet file, never typed from memory; any missing rate stops the calculation at that line and shows [TO CONFIRM]; the skill drafts changes and the user approves before the sheet the client may eventually see is touched.
Manual mode: the skill outputs the model as a markdown table with the same structure, and the user pastes it into their own sheet. Show every rate used and its source (rate sheet field), so the user can audit without the connector.
Client facing versions never show internal day maths unless the studio's chosen transparency model says so (see edge case 25).

## PandaDoc and DocuSign (proposals and signature)

Purpose: get the SOW into the studio's signing flow.

Procedure:
1. The skill produces the final SOW text from templates/sow-template.md, with all [TO CONFIRM] items either resolved by the user or removed by the user's decision. A document with unresolved [TO CONFIRM] markers is never prepared for signature.
2. Connected mode: where a connector exists, the skill first shows the user the complete final SOW text and creates the draft inside PandaDoc or DocuSign only after the user confirms that text. It then reports its status (draft created, not sent). Creating the draft is a write to a tool and follows the same confirmation rule as every other write in this suite.
3. Hard rule: the skill never sends a document for signature, and never triggers a signing envelope, without the user's explicit approval of that specific send. No standing approvals, no "send it like last time".
4. Manual mode: output the SOW as a clean document for the user to paste into their template, with a short checklist of fields to map (fee, milestones, dates).

## HubSpot and Pipedrive (deal logging)

Purpose: keep the commercial record where the studio's pipeline lives.

Connected mode: where a CRM connector is set up, the skill may read the deal record (stage, stated budget, contacts, history) as an input to scoping, and draft updates: scope summary, tier prices presented, next step, change order entries. Every drafted update is shown to the user and written only on confirmation.
Manual mode: the skill outputs a copy ready deal note (date, what was scoped, what was sent, next step, follow up date) for the user to paste.
Rules for both modes: log prices actually quoted, not internal estimates; log declined change orders and discount asks with their outcomes, because that history is what makes the next negotiation on this account honest; never log another client's pricing into a deal record.

## Mode declaration (required footer on tool-assisted outputs)

Mode: [Connected / Manual]
Seen: [files, exports, records actually read, with dates]
Not seen: [anything relevant that was unavailable, and what that means for the estimate]
