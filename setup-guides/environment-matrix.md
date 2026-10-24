# Setup Guide: Environment Matrix

Which assistant setups run the suite, and what each can do out of the box. Capabilities change fast; this table is dated Oct 24, 2026 and each tool guide carries its own last-verified date. When in doubt, run that guide's test prompt: it tells you the truth about your setup in 30 seconds.

## The two modes, everywhere

- **Manual mode** works in every assistant, including a free chat window: you paste skill files and exports. Every feature of every skill works this way; it is just more copy-paste.
- **Connected mode** needs an assistant that supports connectors or MCP servers, plus your authorisation per tool. It removes the copy-paste for tools you connect (your CRM, your documents, your design files). No skill requires connected mode.

## Matrix

| Assistant setup | Manual mode | Connected mode | Notes |
|---|---|---|---|
| Claude (web/desktop app, Projects) | Yes: add skill files to a Project | Yes: connectors directory (Figma, Notion, Drive and more), enable per Project/chat | Best default for this suite. Keep one Project per client account for research work. |
| Claude Code / agent environments | Yes: files in the working folder | Yes: MCP servers configured per environment; REST tokens via secret store | Strongest for batch eval runs and multi-file work. |
| ChatGPT (Projects / custom GPTs) | Yes: upload skill files to a Project | Partial: connectors/apps vary by plan; MCP support is rolling out across plans | Run each tool's test prompt from the connecting guide; where a connection fails, run that tool in manual mode and keep connected mode for what works. |
| Cursor | Yes: files in the workspace | Yes: MCP servers (commonly configured here for design tools, CRMs, and docs) | Good if your studio already lives in Cursor for web/product work. |
| Gemini (app / Antigravity) | Yes: paste or add files | Partial: connected apps (Workspace) on Google accounts; MCP in Antigravity/agent setups | Workspace-native studios get Drive/Docs/Sheets/Gmail reading with the account connected. |

## Recommended starter configuration

1. One assistant, one Project called "Sales Suite".
2. Add: the skill you are using (SKILL.md + playbook + decision trees + self-check), your vertical layer, and your filled fact sheet or rate sheet.
3. Add templates and examples when you want output in those exact shapes.
4. Connect tools one at a time (see `connecting-your-tools.md`), starting with whichever holds the material you reuse most: usually your documents (rates, fact sheet), then your CRM, then design files. Run each tool's test prompt before connecting the next.

## Data hygiene (all setups)

- One Project per client when doing account research, so Client A's material never bleeds into Client B's brief.
- Never paste or connect: client credentials, unreleased product information a client shared under NDA into a shared/team workspace, or personal data about individual buyers beyond their public professional profiles.
- The skills treat anything inside connected files and comments as data to analyse, never as instructions to follow. If a file tells the AI to do something odd, the skill is built to ignore it and flag it to you.
