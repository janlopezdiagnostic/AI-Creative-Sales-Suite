# Setup Guide: Connecting Your Tools (Optional)

This guide is deliberately generic. The suite does not belong to any one tool, and no tool is the headline. Whatever your studio already uses for design files, documents, client tracking, and proposals, the pattern for connecting it to your AI assistant is the same, and the manual way (copy, paste, export) always works if you never connect anything at all.

Read this only when you want the connected way. Most studios should start manual and connect one tool later, if ever.

## The pattern (the same for every tool)

1. **Connect.** In your assistant's settings, look for its connector or app directory, or (for agent-style setups) its MCP server list. Find your tool, sign in with your own account, and grant the narrowest access offered. Read access is the default; grant write access only if the tool forces it, because the suite's rule below still applies.
2. **Test.** Run the 30-second test for that tool (template below). If the assistant cannot actually see the material, you are in manual mode for that tool, whatever the settings screen claims.
3. **Declare.** The skills state their mode at the top of their outputs: connected (and which tools), or manual. Believe the declaration, not the settings screen.
4. **Disconnect when done.** Revoke the connection from the tool's own settings when you stop using it, and never connect a client's system with your credentials on a shared machine.

## The rules that apply to every connection

- **Read first.** The assistant reads. Anything it would change or send (a CRM update, a comment, a document share, a proposal send) is drafted for your approval first. Connecting a tool never switches this off.
- **What is inside a file is information, not instructions.** Comments, briefs, and documents sometimes contain text aimed at AI tools. The skills treat that text as something to report, never something to obey.
- **Client confidentiality comes first.** If a client's contract or NDA forbids third-party processing of their files, that client stays manual, full stop. Connect with an account that can see only what you are willing to show the assistant.

## The tools, by the job they do

### Design and artwork files
*Examples: Figma, Adobe Creative Cloud (InDesign, Illustrator, Photoshop), Affinity, Sketch.*
What the suite reads: file and page structure, counts of deliverables and variants, component or library usage, open comments. Used to count what a job really contains and to audit delivered files.
Manual fallback: PDF exports, a screenshot of the pages or layers panel, comment threads copied as text. For Adobe desktop files this is the primary route in most setups, since full connectors are rare; the skills are written to work from exports there.

### Documents, notes, and files
*Examples: Google Workspace (Docs, Sheets, Drive), Notion, Microsoft 365, Dropbox.*
What the suite reads: your rate card or price list, the studio fact sheet, briefs, past proposals, meeting notes, pricing spreadsheets.
Manual fallback: paste the text, or upload the exported file. This is the category most worth connecting first if you connect anything, because your rates and fact sheet get reused in every job.

### Client and deal tracking (CRM)
*Examples: HubSpot, Pipedrive, or a spreadsheet doing the same job.*
What the suite reads and drafts: deal stage, last contact, open tasks. Logging a call, moving a deal, or noting an outcome is a write: drafted for you, applied only on your confirmation.
Manual fallback: paste the deal list or export it as a spreadsheet.

### Finding and checking contacts
*Examples: Apollo, Clay, LinkedIn Sales Navigator.*
Rules that do not bend: Sales Navigator is manual only, always (you paste or export; the assistant analyses). Enrichment tools are read-only verification: the suite checks details you already hold, it does not harvest lists, and it never scrapes anything.

### Proposals and signing
*Examples: PandaDoc, DocuSign, or PDFs from your documents.*
What the suite reads: proposal status, who has viewed or signed, redline comments. Creating a draft inside these tools counts as a write and needs your confirmation, like any other send.

### Boards and workshops
*Examples: Miro, FigJam.*
What the suite reads: range maps, workshop boards, prioritisation grids from discovery sessions. Manual fallback: export the board as PDF or paste the text contents.

### Scheduling and call records
*Examples: Calendly, Loom, your recorder or meeting platform transcripts.*
What the suite reads: booking intake answers (useful discovery material) and call transcripts, which the Discovery Call Kit turns into briefs. Manual fallback: paste the transcript.

## The 30-second test (adapt it per tool)

Paste this into a chat, naming a file or record you own:

> Using your connection to [tool], open [the named file or record]. Tell me its structure: the main sections or pages, a count of what is inside, and any open comments or tasks. If you cannot access it, say exactly that, and do not guess from the name.

- A structured answer matching what you see in the tool: connected mode is live for that tool.
- "I can't access that": manual mode for that tool. Work from exports; the skills will tell you exactly what to export.

## One worked example: Figma

Figma is the worked example only because its connection routes are the most documented, not because the suite prefers it. Routes: (1) Figma's MCP server, added in your assistant's MCP settings with OAuth sign-in (seat requirements vary; check Figma's current documentation before paying for a seat); (2) a Figma connector in your assistant's directory, if it offers one (prefer this, fewer moving parts); (3) advanced, a read-only personal access token for agent setups, stored in a secret store, never in a chat or a file. Run the test above against a file you own. Everything the design-files section says about manual exports applies unchanged when the connection is off.

The same shape of route (connector in the directory first, MCP second, token last) is what to look for with every other tool above. If a tool offers none of them, that tool simply stays manual, and nothing in the suite is lost.
