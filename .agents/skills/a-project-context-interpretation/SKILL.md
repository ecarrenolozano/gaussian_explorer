---
name: a-project-context-interpretation
description: interpret the canonical project context document and produce a structured, evidence-based summary of project purpose, scope, deliverables, stakeholders, constraints, terminology, revision history, and approval status. use when downstream workflow stages need a reliable overview from sdlc_docs/00_project_context/project_context.md.
---

# Project Context Interpretation

## Purpose

This skill interprets the canonical project context document and converts it into a concise, structured, and evidence-based overview. It helps downstream SDLC activities understand the project's purpose, scope, deliverables, stakeholders, constraints, terminology, revision history, missing information, and approval status before proceeding.

## Core Workflow

1. **Locate the context file:** Ensure that `sdlc_docs/00_project_context/project_context.md` exists.  
   - *Precondition:* The repository should follow the SDLC-docs convention. If the file is missing, report an error like *"Project context file not found."* Prompt the user to provide or confirm the path.
2. **Read file content:** Use the `Read` tool to open and read the entire Markdown file as text.
3. **Split into sections:** Parse the content by heading markers. The expected sections (case-insensitive) are:
   - Project Name (under "Project Overview")
   - Purpose
   - Scope
   - Key Deliverables (list)
   - Rationale
   - Stakeholders (markdown table with roles/interests)
   - Constraints (bullet list)
   - Key Concepts / Terminology (table)
   - (Reference Links may be empty)
   - Revision History (table)
   - Approval (checkbox line)

   For each section, extract the relevant content (text, list items, or table rows). 

4. **Extract fields:** Based on headings:
   - **Project Name:** Text after "**Project Name:**" (strip markdown).
   - **Purpose:** Text after "**Purpose:**".
   - **Scope:** Text after "**Scope:**".
   - **Key Deliverables:** Each bullet under "Key Deliverables" becomes a list item.
   - **Rationale:** The paragraph(s) under "## 2. Rationale".
   - **Stakeholders:** Parse the table under "## 3. Stakeholders"; collect each row's *Role* and *Responsibility / Interest*.
   - **Constraints:** Each bullet under "## 4. Constraints".
   - **Terminology:** From "## 5. Key Concepts / Terminology", map each *Term* to its *Definition*.
   - **Revision History:** Optionally record version/history if needed.

5. **Normalize data:** Trim whitespace, unify formatting (e.g. remove bullet `- ` markers, strip trailing periods consistently). If lists have trailing periods or missing punctuation, standardize them.

6. **Check consistency / clarifications:** 
   - If any required section is empty or missing (e.g. no "Scope:" line found), **ask for clarification** instead of assuming. For example, say: *"The Scope section appears to be missing or unclear. Can you confirm it?"*.
   - If headings are typos (e.g. "Purpse" instead of "Purpose"), try to infer or prompt the user.
   - Ensure lists (deliverables, constraints) are correctly captured. If a bullet is malformed, flag it.
   - Note: this skill does **not** handle out-of-scope items (e.g. design decisions or implementation); those should be covered by other skills/documents.

7. **Construct output:** Build a JSON (or structured) summary containing all extracted fields. For example:
   ```json
   {
     "project_name": "...",
     "purpose": "...",
     "scope": "...",
     "key_deliverables": ["...", "..."],
     "rationale": "...",
     "stakeholders": [
       {"role": "...", "interest": "..."},
       ...
     ],
     "constraints": ["...", "..."],
     "terminology": {"Term1": "Definition1", ...},
     "revision_history": [{"version": "...", "date": "...", ...}, ...],
     "approved": false,
     "approval_status": "Not Approved",
     "approval_indicator": "red"
   }
   ```

8. **Summarize the project context:** Provide a concise, human-readable summary covering the project name, purpose, scope, deliverables, stakeholders, critical notes, and missing information. Use tables or lists only when they improve clarity.

9. **Flag issues clearly:** Use icons and formatting to highlight missing information, inconsistencies, risks, and items requiring user confirmation.

10. **Show the approval status in chat:** Display a prominent approval badge at the beginning or end of the final response. Do not add it to the project-context file.

* `🟢 **Status: APPROVED**`
* `🔴 **Status: NOT APPROVED**`
* `🟡 **Status: APPROVAL UNKNOWN**`

