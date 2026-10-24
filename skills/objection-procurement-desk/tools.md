# Tools: Dual Mode Procedures

Honest limit, stated once and repeated wherever it matters: this skill is a file pack. It cannot click inside Gmail, a CRM, or any other tool by itself. Two modes exist:

- **Connected mode:** the user's assistant has been set up with the tool's MCP server, API connector, or native integration by the user. In this mode the skill directs the assistant to read live data, and drafts writes for the user to approve.
- **Manual mode:** no connector. The user exports or pastes content, and the skill works from that. Manual mode always works and is the default assumption.

Every output must declare its mode and what was actually seen. Never imply live access that was not used. Standing rule for all tools, and doubly so in negotiation: read freely, write only with the user's confirmation of the exact content. In this skill, a "write" includes a sent reply, a changed deal stage, and a logged outcome, because all three become the record the next negotiation stands on. Nothing is sent to a client from any tool by this skill.

Exact connector capabilities change as vendors update them. Verify current scope at setup time; the procedures below describe what to read and why, not a guarantee of a vendor's current API surface.

## HubSpot and Pipedrive (negotiation logging and deal history)

Purpose in this skill: the negotiation's memory. What was asked, what was offered, what was agreed, and what happens next, recorded where the pipeline lives.

Connected mode procedure:
1. Before drafting any response, read the deal record: stage, proposal version sent, stated budget if any, contacts and roles, prior notes. Prior commitments recorded here outrank anyone's recollection, including the user's.
2. After each exchange, draft the update: the ask in the client's words, your classification and diagnosis, the response sent (or its location), trades offered and their results, agreements, next step with a date. Show the draft to the user and write it only on confirmation, per the standing rule.
3. Stage changes are writes. A deal moves to "in negotiation", "closed won", or "closed lost" only on the user's confirmation, with the reason in factual language. Walked deals get the tree 5 reason, not a euphemism, because the review date pipeline depends on honest reasons.
4. Never write another client's pricing, terms, or deal structure into this deal's record, and never read another deal's commercial detail into this negotiation as a benchmark. Reading across deals for benchmarks is exactly the disclosure standing rule 3 forbids, with extra steps.

Manual mode procedure:
1. Ask the user for the deal summary or last CRM export, plus the thread, before drafting.
2. Output the log entry in the negotiation log template format for the user to paste, and a one line CRM summary in the same shape every time: date, ask, response, next step, date.

## Gmail and email threads (drafting responses)

Purpose: draft the reply inside the real thread, with the whole history in view, because negotiation errors are usually history errors.

Connected mode procedure:
1. Read the full thread, not the latest message: the proposal as sent, every concession already made by anyone, every promise about dates or terms. Quote the relevant earlier lines back in your working notes before drafting.
2. Draft the reply in thread (same subject, same recipients). Adding or removing recipients is a negotiation act (copying a boss is escalation; dropping procurement is a snub) and is done only on the user's explicit instruction.
3. The draft stays a draft. The user reviews the exact text and sends, or confirms the send, themselves.

Manual mode procedure:
1. Ask the user to paste the thread, oldest first, and to say who each sender is if names are ambiguous.
2. Work from the paste and say so. If the paste is partial (latest message only), flag that history based checks (prior concessions, prior promises) could not be run, and list that as a risk on the draft.

## PandaDoc and DocuSign (proposal status and redlines)

Purpose: know where the document actually is before responding to what the client says about it.

Connected mode procedure:
1. Where a connector exists, read document status: sent, viewed, opened sections where the tool exposes them, redline or comment activity, completed or declined. A client who says "legal has it" while the status shows unopened for nine days is diagnostic data; use it gently and factually.
2. If redlines come back through the tool, extract the changed clauses into the terms response table (clause, their position, classification) rather than negotiating inside the document's comment threads. Clause by clause negotiation in comments produces storms and no single record.
3. Hard rule, shared with the scope skill: the skill never sends a document for signature, re-sends, or triggers an envelope without the user's explicit approval of that specific send. Creating or altering a draft document is also a write: show the user first, create on confirmation.

Manual mode procedure:
1. Ask the user for the redlined file or the client's summary of changes, plus the date the document was sent.
2. Build the clause table from what was provided, and mark any clause the summary does not mention as "not seen", never as "agreed".

## Google Sheets (comparing competing quotes the client supplied)

Purpose: an honest, deliverables level comparison when, and only when, the client has supplied a competing quote and asked for a comparison, or chosen to share it.

Connected mode procedure:
1. Build the comparison in a sheet the user owns: rows are deliverables and protections (per phase and per SKU: strategy, masters, adaptations, rounds included, production liaison, source files, guidelines, terms), columns are the studio's proposal and the supplied quote. Populate only from the two documents. Cells the quote does not address read "not stated", never zero and never an assumed exclusion presented as fact.
2. Rates from the studio's proposal are the proposal's own figures (already client facing). Internal day maths and margins never enter this sheet (see the scope skill's transparency rule).
3. The user approves the sheet before it is shared, and decides whether it is shared at all.

Manual mode procedure: output the same comparison as a markdown table for the user to paste, with the same rules.

Standing cautions for both modes:
- The competing quote is the client's document, supplied by them. The comparison comments on what it states, never on the competitor's real business, which you do not know.
- If the client will not supply the quote, there is no comparison to build; work from your own deliverables list instead (playbook entry 3).
- Never place a third client's quote, terms, or pricing in the sheet. The comparison has exactly two columns, ever.

## Mode declaration (required footer on tool-assisted outputs)

Mode: [Connected / Manual]
Seen: [threads, records, documents actually read, with dates]
Not seen: [anything relevant that was unavailable, and what that means for the draft, for example unrun history checks]
