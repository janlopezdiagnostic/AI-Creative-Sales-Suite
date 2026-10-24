# Setup Guide: Figma (Connected Mode)

What this unlocks: the suite's skills can read your Figma files directly, page structure, frames, components, variables/tokens, and comments, instead of working from screenshots and exports. The Scope and Pricing Architect uses this to count deliverables and judge complexity. The research and proposal skills use it to audit pitch files and summarise client feedback threads.

Honest limits first: a skill file cannot log into Figma by itself. Connected mode works only when your AI assistant has a Figma integration installed and authorised by you. Capabilities differ by route and change over time; the test prompt at the bottom tells you in 30 seconds whether yours is live and what it can see. Last verified: Oct 24, 2026 (routes below existed; exact read scopes vary, re-run the test after any tool update).

## Route 1: Figma MCP server (Claude, Cursor, and other MCP clients)

1. You need a Figma account with access to the files you want read. Dev Mode / editor seats expose the most; view-only access reads less. Check Figma's current MCP documentation for the seat requirements before paying for a seat.
2. In your assistant's MCP settings, add Figma's MCP server using the configuration Figma publishes (remote server via OAuth sign-in, or the desktop Dev Mode server in the Figma app under Preferences, depending on the client).
3. Complete the OAuth sign-in in the browser when prompted. Authorise the narrowest scope offered that still reads files.
4. Restart the assistant, open a chat, and run the test prompt below against a file you own.

## Route 2: Connector / plugin inside your assistant

Some assistants ship a Figma connector in their directory instead of raw MCP. Install it from the connector list, sign in with the same Figma account, and run the test prompt. If your assistant offers both, prefer the connector: fewer moving parts.

## Route 3: REST API token (advanced, agent setups)

For scripted/agent environments: Figma profile → Settings → Security → Personal access tokens. Create a read-only token scoped to file content and comments. Store it in your environment's secret store, never in a chat, a repo, or a skill file. This route is what most third-party "Figma reader" tools use under the hood.

## Security rules (do not skip)

- Connect with an account that can see only what you are willing to show the assistant. Client work under NDA: if the NDA forbids third-party processing, use manual mode for that client, full stop.
- Read access is the default. If a route offers write access (posting comments, editing files), the suite's rule still applies: the AI drafts, you approve, then it posts.
- Revoke the token/connection from Figma settings when you stop using it.

## The 30-second test

Paste this into a chat with a Figma file link you own:

> Using your Figma access, list this file's pages and top-level frames, count its components and variables, and list any unresolved comments with their authors. If you cannot access the file, say exactly that and do not guess from the file name.

- Good result: a structured answer matching what you see in Figma. You are in connected mode.
- "I can't access that file": you are in manual mode. Work from exports until the connection is fixed; the skills will tell you what to export.

## Manual mode cheat sheet (no connection)

- Deliverables count: export the file's page list (screenshot of the pages panel) + paste the components panel counts.
- Feedback: copy the comment thread text from the file (select comments panel, copy) and paste it.
- Pitch audit: export frames as PDF (File → Export frames to PDF) and upload the PDF.
- Complexity signals: export variables/tokens as JSON (variables panel export, where your plan allows) or paste the token list.
