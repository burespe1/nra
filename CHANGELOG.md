# Changelog – NAP Reference Architecture

Releases newest first. Each release groups its changes into Added / Changed / Archived / Editorial; the full change protocol is in `docs/`.

## v2.2.0 – draft (branch `release/2.2.0`)

Resolution of the 12 unresolved requirements (Guidelines 01, 03, 05) and alignment with Guidelines 01–07 (approved 2026-10-20).

- **Added:** function F3.6.11 Monitor NAP Usage and Performance (OPTIONAL); issue *Does not yield a Requirement*.
- **Changed:** F3.6.1, F3.6.2, F3.6.4, F3.6.5, F3.6.9 extended (MANDATORY_PLUS, optional parts marked OPTIONAL); 10 requirements moved from Unresolved to their packages and linked to the architecture; L.12.1 (NIS2) as conditional requirement; User Need → F3.6.4 links converted to «Servedby»; issues resolved/closed; RequirementLevel on all functions (MANDATORY by default); K.1.16.1, K.1.19.1, K.7.5.1 linked («fulfilled by»); issue *Functionality Missing* renamed to *Missing functionality for the Requirement*; F3.6.11 on the functional tree (light blue = OPTIONAL); template NC_NNN_Functions prints the requirement level; partial master documents per view (*NAP Documentation/Partial documents*) for reviews in Word; K.1.19.1 threshold corrected to the KPI 1.19 minimum (“shall not be higher than 2 sec”).
- **Archived:** requirement L.9.1 (Single Digital Gateway) removed, specification L9 linked to *Does not yield a Requirement*; three closed issues merged; five empty *Specifications & Requirements* view folders removed (and the model-document reference to one of them).
- **Editorial:** K5.4.1 → K.5.4.1; package versions reset to default (model versioned by tag), NLKF edition in `sourceVersion`; Keywords in title case (Low Level Function, High Level Function, Physical Data Flow); notes of all views and Supplements formatted consistently (bold labels, blank line before headings, bullet lists); documentation templates in British English; missing words and typos in the UVARBox note.

## v2.1.0 – 2026-10-20

Organisational View revision by NAPCORE-X WG 4.6.3, consistency and documentation fixes. Protocol: `docs/NRA_2.1.0_Changelog.docx`.

- **Added:** Agreement *Content provision contract/agreement*; model document *Supplements - Requirements* (requirements now published); glossary terms CA/NB, NAP Operator and 9 abbreviations; tagged values `revised`/`since`.
- **Changed:** Competent Authority / National Body renamed and redefined; descriptions of all actors and roles; IN/OUT labels of 62 function–data flow connectors aligned with the arrows; Componentof directions unified; documentation templates repaired.
- **Archived:** two duplicate high-level data flows.
- **Editorial:** CA/NB naming, glossary wording, requirement names and order.

## v2.0.0 – 2025-07-04

Baseline (`NRA_20250704-clean.qea`).
