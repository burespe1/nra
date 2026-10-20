<!-- Generated from "06 NRA Versioning and change management guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This guideline defines how the NRA model in Enterprise Architect (EA) is versioned, how changes are proposed, reviewed, approved and recorded, and how the published documentation is produced from an approved version.

**Audience:** NRA maintenance team.

**Status:** approved on 20 October 2026

| Version | Author                        | Note                                                                                                        |
| ------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 0.1     | Claude (draft for Petr Bureš) | First proposal, based on the 2.1.0 and 2.2.0 releases, the git test repository and the review import pilot. |
| 1.0     | Petr Bureš                    | Approved on 20 October 2026.                                                                                |

# 1 Scope

This guideline covers:

  - Version numbering of the NRA model and of its documentation

  - Tagged values recording the history of individual elements

  - Change types, their version impact and the deprecation of elements

  - The change workflow in git, the Change Protocol and the generation of the documentation

  - Excludes: content rules for Specifications, KPIs, Requirements, Interfaces and optional functionality (see Guidelines 01–05) and modelling conventions (see Guideline 07)

# 2 Version Numbers

The NRA is versioned as a whole with semantic versioning MAJOR.MINOR.PATCH, following the approach used for the ITS Data Dictionary.

  - **MAJOR** – changes that break existing references: deletion or renaming of published elements, restructuring of views, change of the meaning of a connector type.

  - **MINOR** – additions and substantive changes that keep existing references valid: new elements, new Requirements, new connections, substantive description changes.

  - **PATCH** – editorial changes: wording, typos, layout of diagrams, documentation templates.

The authoritative version number is the git tag vX.Y.Z on the main branch. The same number is written to the ReportVersion of the master document and appears in the title of the generated documentation.

Packages are not versioned individually. The package Version field is left at its EA default (empty or 1.0); tools/check.py warns about any other value. This avoids package versions that fall out of step with the model version.

Work on a coming version is done on the branch release/X.Y.Z; documents generated from it are labelled “X.Y.Z draft”.

# 3 Element History

The history of an element is recorded in tagged values, not in the EA Version or Phase fields:

  - **revised** – approval date (YYYY-MM-DD) of the release in which the element was last changed. Set on every FRAME element and GlossaryEntry; printed in the documentation.

  - **since** – the NRA version that introduced the element (e.g. 2.2.0). Set on elements created from 2.2.0 onwards.

  - **RequirementLevel** – MANDATORY, OPTIONAL or MANDATORY\_PLUS (see Guideline 05).

  - **sourceVersion** – version of the external document a Specification reflects (see Guidelines 01 and 02).

Element Status is Proposed while the change is on a release branch and Approved once the release is approved. Before the approval the revised value holds the planned release date and is corrected at approval. Until now EA left all elements at Proposed; the first approved release sets them to Approved, from then on check.py lists elements still Proposed.

# 4 Change Types and Version Impact

Every change is classified with one of the following change types; the highest impact of all changes determines the version increment.

  - **New object** – MINOR.

  - **Title change** – MINOR; PATCH when only a typo or capitalisation is corrected.

  - **Substantive description change** – MINOR: the meaning, scope or obligation changes.

  - **Editorial description change** – PATCH: wording only.

  - **Connection change** – MINOR: connector added, removed, redirected or its type changed.

  - **Layout change** – PATCH: diagram positions, colours, sizes.

  - **Object deleted** – MAJOR for published elements; MINOR for elements never published (e.g. an unresolved Requirement).

  - **Object moved** – PATCH when the documentation is unchanged, otherwise MINOR.

Issues are working items, not architecture content: closed or merged issues may be deleted in any version.

# 5 Deprecation

Published elements are not deleted in MINOR or PATCH versions. Instead:

1.  Move the element to the package for superseded content of its area (Superseded for Specifications, Obsolete KPIs for KPIs and their Requirements).

2.  Set Status to Deprecated and add a note “Deprecated in X.Y.Z, replaced by …”.

3.  Remove the «fulfilled by» links so that the element no longer constrains the architecture.

4.  Delete the element in the next MAJOR version and record the deletion in the Change Protocol.

# 6 Change Workflow in Git

The model is kept in a git repository (test: github.com/burespe1/nra). The file model/NRA.qea is stored with Git LFS and is lockable, because a binary EA model cannot be merged. A text export (YAML per package) is committed next to it so that changes can be reviewed.

5.  git pull and git lfs lock model/NRA.qea – only the lock holder edits the model.

6.  Create a branch: release/X.Y.Z for a release, change/\<topic\> for a single change.

7.  Edit the model in EA, set revised, since and Status on changed elements, then close EA.

8.  Commit. The pre-commit hook runs tools/export.py and adds the export/ folder to the commit.

9.  Push and open a pull request. GitHub Actions runs the export check, tools/check.py and tools/diff.py and posts the change report and the check results as a pull request comment.

10. The working group reviews the report. Errors reported by tools/check.py are fixed before merging.

11. Merge to main, tag vX.Y.Z (the tag run attaches the report against the previous tag) and git lfs unlock model/NRA.qea.

One pull request should contain one topic, so that the change report remains readable.

# 7 Review in Word (Offline)

Views are often reviewed by a working group in a generated Word document rather than in EA. The changes are transferred back to the model with tools/docx\_import.py and tools/docx\_apply.py instead of being retyped. Each element in the document is anchored by its line “Revised/Last changed …, GUID: {…}”.

## 7.1 Preparing the Review Document

  - Generate the document from a tagged version (or a release branch) and name it with version, view and date, e.g. NRA-2.2.0-review-OrgView-2026-11.docx.

  - A review document may cover only a part of the model, e.g. one view. Use the partial master documents in Supplements\\NAP Documentation\\Partial documents (one per view, same cover, TOC and style as the full document); a single model document can also be generated on its own.

  - Elements that are not in the document stay unchanged – a missing chapter is not a deletion. Only a heading deleted with Track Changes (or a DELETE comment) asks for removal.

  - When cutting a part out of the full document, delete the other chapters with Track Changes switched off and before distributing. Do not copy parts into a new document: heading styles and tracked changes may be lost and the import cannot recognise the sections.

  - Every element keeps its heading “Keyword: Name” directly followed by the line with its GUID.

  - Several partial documents of the same version can be imported one after another; if two of them change the same element, the second import reports a conflict.

  - Commit the distributed document and the returned document under reviews/, so that the import can be repeated.

  - Switch on Track Changes before distributing (if needed, restrict editing to tracked changes).

## 7.2 Rules for Reviewers

  - Edit only with Track Changes. Never edit or delete the “Revised …, GUID” line.

  - Changing the heading “Keyword: Name” renames the element.

  - A new element is a new heading “Keyword: Name” (Keywords as in Guideline 07) followed by its description, placed after the element it belongs next to. Write what it connects to (e.g. data flows, parties) in the description or in a comment.

  - An element to be removed: delete its heading and text, or add the comment DELETE. Removal follows the deprecation rules (Section 5) and is done in EA.

  - Changes of connections (roles, requirements, data flows printed below the description) may be written in the text; they are reported and done in EA.

Comments carry the open work; the first word decides what happens to them:

  - **TODO** – a task for the element.

  - **ISSUE** – an open question for the element (or an Issue element under Guideline 03 if it concerns a requirement).

  - **WIP** – the section is still being drafted: imported and kept, but not written to the model. A heading can also be marked “\[WIP\]”.

  - **PROPOSAL** – a suggestion that the group has not yet agreed: kept, not written.

  - Other comments are discussion; unresolved ones are kept as issues, resolved ones are dropped.

## 7.3 Proposals by Claude

Text proposed by Claude is entered as tracked changes with the author “Claude” or as PROPOSAL comments. It is never applied automatically: the group accepts or rejects it in Word before the import, or sets apply: true for the entry in changes.yaml after deciding. Until then the proposed text is stored as a pending task on the element, so nothing is lost.

## 7.4 Import

python tools/docx\_import.py \<review\>.docx \<base\>.qea --current model/NRA.qea --out changes/\<review\>/changes

  - changes.yaml lists every changed or new element with the change type, new name and description, authors, comments and the decision apply: true/false; changes.md shows the text differences for the pull request.

  - Entries marked WIP, proposals and conflicts (the element was changed in the model after the document was generated) get apply: false.

  - The import checks the new text for errors: left-over markers (TODO, TBD, ???), abbreviations missing in the glossary, unknown Keywords, names already used, a heading that does not match the element type. Warnings are listed per entry.

  - For a new element the import lists the connections it still needs (e.g. IN and OUT data flows and the module of a function, the parties of an agreement) and candidate elements mentioned in its text.

The maintainer reviews changes.yaml, corrects obvious errors in the document or switches entries off, and commits the import.

## 7.5 Apply

With EA closed: python tools/docx\_apply.py \<review\>.docx \<base\>.qea model/NRA.qea --changes changes/\<review\>/changes.yaml --since X.Y.Z

  - Written: names, descriptions, package descriptions; Status = Proposed; revised; new elements (Status Proposed, since, RequirementLevel MANDATORY for functions).

  - Recorded as EA maintenance items (Maintenance tab, not printed): a task for each missing connection of a new element; a pending task with the text of every entry not applied; TODO/WIP/PROPOSAL comments as tasks; ISSUE and other open comments as issues; import warnings as issues.

  - Not written: connection changes, diagrams and element removal – they are done in EA following changes.md and the tasks.

## 7.6 Completing in EA

  - Work through the tasks of the review (Maintenance window): create the data flows and «componentof» links of new functions, place new elements on the diagrams, add parties to agreements, decide pending proposals. Set each finished task to Resolved.

  - tools/check.py warns about incomplete elements (functions without IN/OUT data flows or parent, roles without actor, agreements without parties) and lists all open maintenance items.

  - Commit in small steps: import, apply, then each block of manual work; the pull request shows the change report and the check.

  - The Change Protocol entries are prepared from changes.yaml (authors, dates, change types); open tasks that are carried over are listed as open points.

# 8 Change Protocol

Each release has a Change Protocol (model/NRA\_X.Y.Z\_Changelog.docx) and a short entry in CHANGELOG.md. The list of changes is taken from the tools/diff.py report; the author adds the scope note for each entry. The protocol is grouped by view (Organisational, Functional, Supplements, Whole model) and each entry contains:

  - Object ID, Object type, Object (previous) name

  - Change type (Section 4)

  - Author, Creation Date and Approval Date

  - Note/Scope – one paragraph describing the change and its source

The protocol ends with the version impact and the open points carried over to the next version.

# 9 Documentation Generation

  - The documentation is generated from the master document “National Access Point Reference Architecture” with the NAPCORE cover and stylesheet templates.

  - For a single view use the partial master documents “NRA – \<view\>” in NAP Documentation\\Partial documents. They contain copies of the model documents of the full document; when a model document of the full document changes (template, packages), change its copy as well. Set ReportVersion of the partial documents together with the full document.

  - Generate only from a tagged version (or from a release branch for a draft) and save it as docs/National Access Point Reference Architecture - X.Y.Z.docx.

  - Check before publishing: chapter order, input and output flows of functions, the Requirements chapter, revised dates, roles and the glossary.

# 10 Release Checklist

12. tools/check.py reports no errors; warnings are reviewed; open review tasks are resolved or listed as open points.

13. Change Protocol complete, version impact agreed.

14. Release approved by the working group; approval date set in revised and in the protocol; Status set to Approved.

15. Master document ReportVersion updated, documentation generated and checked.

16. Pull request merged, tag created, lock released.

# 11 Open Questions

  - Move the repository to a NAPCORE organisation and define the reviewers.

  - Who approves a release (working group lead, steering group)?

  - Should PDF versions of the documentation be published from the repository?
