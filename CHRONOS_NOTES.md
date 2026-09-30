# Chronos — Notes & Decisions

## Azure / Microsoft stack integration (deferred)

**Status:** Not part of the initial build. Revisit later, optional.

**Context:** A friend (advice relayed to Christopher) noted that American Airlines
technical interviews may cover PowerShell, Azure, Active Directory, and general
Microsoft cloud/hardware knowledge. Microsoft Learn modules (e.g. AZ-900 Azure
Fundamentals, MS-900 M365 Fundamentals, and the PowerShell for Beginners module)
are the recommended free path to build that knowledge, tied to a Microsoft account.

**Decision:** Get Chronos working end-to-end first, using the current planned stack.
Azure integration is a possible *later* enhancement, not a blocker — Chronos
doesn't need Azure to function.

**If revisited later, two natural tie-in points:**
1. **PowerShell** — the existing Windows-only process-killing / app-blocking script
   (tested on the Windows PC or via GitHub Actions) already doubles as real
   PowerShell practice — no separate project needed.
2. **Azure** — could host the RAG/AI classifier on Azure Functions, or move
   LeetCode history storage to Azure Blob/Cosmos DB, purely for resume-relevant
   Azure exposure. Adds complexity — not required for Chronos to work.
