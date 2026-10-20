<!-- Generated from "07 NRA Modelling conventions guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

Modelling Conventions of the NAP Reference Architecture

**Purpose:** This guideline collects the conventions that keep the NRA model consistent and printable: package aliases, naming, Keywords, connector directions and stereotypes, glossary and the automated checks of tools/check.py.

**Audience:** NRA maintenance team.

**Status:** approved on 20 October 2026

|         |                               |                                                                                          |
| ------- | ----------------------------- | ---------------------------------------------------------------------------------------- |
| Version | Author                        | Note                                                                                     |
| 0.1     | Claude (draft for Petr Bureš) | First proposal, based on the fixes made in the 2.1.0 and 2.2.0 releases.                 |
| 1.0     | Petr Bureš                    | Approved on 20 October 2026; kept as a separate guideline, not merged into Guideline 06. |

1 Scope

This guideline applies to all views of the NRA model. Content rules of individual element types are in Guidelines 01–05; versioning is in Guideline 06.

2 Packages and Documentation

  - The package Alias is printed as the chapter heading by the templates NC\_N\_PDEnotes, NC\_NN\_Pnotes, NC\_NN\_NNN\_PECEnotes and NC\_NN\_NNN\_PEDNCEN. Every package printed by these templates has an Alias (e.g. “K.1 Availability”).

  - The order in the project browser is the order in the documentation; the templates use tree order ascending.

  - Working packages are not published: Supplements\\Requirements\\Unresolved, Obsolete KPIs.

  - Requirements are not kept in view folders; they live only under Supplements\\Requirements (see Guideline 03).

3 Naming

  - The same element has the same name everywhere; no leading or trailing spaces, no double spaces, consistent capitalisation.

  - Functions: “F\<number\> \<verb phrase\>”, e.g. F3.6.11 Monitor NAP Usage and Performance.

  - Requirements: “L.n.n \<label\>” or “K.n.n.n \<label\>” – a space separates the number and the label (see Guideline 03).

  - Specifications: prefix and number followed by the label, e.g. L8 Directive (EU) 2023/2661 - ITS (recast) (see Guideline 01).

  - Global issues have fixed names: “Does not yield a Requirement”, “Missing functionality for the Requirement”.

4 Keywords

The EA Keywords field is printed as the element type in the documentation and is mandatory for elements in published packages. Values in use:

  - Organisational view: Stakeholder, Actor, Role, Agreement

  - Motivational layer: Vision, Mission Statement, ITS Domain, ITS Service, Topic, User Need, Expectation, Benefit

  - Functional view: High Level Function, Low Level Function, Functional Data Flow, Data Store, Terminator

  - Physical and communications view: Subsystem, Module, Physical Data Flow, Interface

  - Supplements: Requirement, Legal Specification, Technical Specification, Recommendation, Profile

Keywords are written in title case, matching the FRAME stereotype names (harmonised in 2.2.0).

5 Connectors

Direction and stereotype follow these conventions (source → target):

  - **Function → data flow**: Information flow labelled OUT; **data flow → function**: labelled IN. The label always matches the arrow.

  - **Low level function → high level function**: Aggregation «componentof» (part → whole).

  - **User Need → function**: Association «Servedby».

  - **Role → Actor**: «defines»; **Agreement → Role**: «adheres to».

  - **Requirement → NRA object**: «fulfilled by»; one Requirement may have several targets (see Guideline 03).

  - **Specification → Requirement**: Abstraction (or Usage); **Specification → global issue**: Association.

  - **Between Specifications**: Realization (regulation → directive), Usage (standard → regulation, profile → standard), Substitution (new → repealed).

Duplicate connectors between the same two elements are not allowed; an inverted IN/OUT label or a reversed «componentof» is an error.

6 Abbreviations and Glossary

  - GlossaryEntry elements in Supplements\\Glossary are the single source of the glossary; the EA project glossary is synchronised from them before generating the documentation.

  - An abbreviation is introduced as “Full term (ABBR)” at its first use in an element note; combined roles are written with a slash without spaces (e.g. CA/NB), and each part has its own glossary entry.

  - Every GlossaryEntry carries the tagged value revised.

  - New abbreviations introduced in a review get a glossary entry; the review import warns about abbreviations not yet in the glossary.

7 Diagrams

  - Every element on a diagram exists once in the project browser; no copies with the same name.

  - Requirements are dragged onto a view diagram only to create the link and are removed afterwards.

  - OPTIONAL functions are filled light blue (RGB 204, 229, 255); a legend on the diagram explains the colour (see Guideline 05).

8 Automated Checks

tools/check.py runs on every pull request and can be run locally (python tools/check.py model/NRA.qea). Errors block the merge; warnings are reviewed.

  - **Errors**: model document referring to a deleted package; missing Keywords in published packages; missing revised; dangling connectors; IN/OUT label against the arrow; «componentof» whole → part; wrong User Need link; Requirement name pattern; published Requirement without «fulfilled by»; unresolved Requirement without an issue; MANDATORY\_PLUS without the keyword OPTIONAL.

  - **Warnings**: missing package Alias; package Version other than the default; Requirement without source Specification; Specification yielding nothing; function without RequirementLevel; duplicate names; incomplete elements (function without IN/OUT data flows or parent function, role without actor, agreement without two parties); open maintenance items (tasks and issues from reviews); elements still Proposed after the first approved release.
