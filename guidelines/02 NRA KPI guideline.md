<!-- Generated from "02 NRA KPI guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This document outlines how Key Performance Indicators (KPIs) from the NAP Level of Service KPI Framework (NLKF) are transferred, modelled, and maintained within the Enterprise Architect (EA) model of the NAP Reference Architecture (NRA).

**Audience:** NRA maintenance team.

| Version | Author                      | Note                                                                                                                                                                                                                           |
| ------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.0     | Petr Bureš, Benjamin Witsch | Revised, connection to NRA objects via Requirements and updated folder structure.                                                                                                                                              |
| 1.1     | Petr Bureš, Claude          | After the 2.1.0/2.2.0 model update: NLKF version in sourceVersion, category aliases, obsolete KPIs kept until MAJOR version. KPI text inserted 1:1 as a linked document (RTF), as for Interfaces. Approved on 20 October 2026. |

# Scope

This guideline covers:

  - How NLKF KPI Specification objects are maintained in EA

  - Structure, classification, foldering, and linkage

  - Excludes:
    
      - Other specifications then KPIs (see Guideline 1)
    
      - Requirements derived from Specifications (see Guideline 3)
    
      - Versioning and change management of the model (see Guideline 06)

# Role of NKLF KPI Specifications in the NRA

**NLKF KPIs are modelled as Specification objects in the NRA.** They represent performance expectations defined by the *NAP Level of Service Key Performance Indicators Framework*, developed by NAPCORE. Each KPI contributes to the overall assessment and scoring of a National Access Point (NAP).

Most NLKF KPIs define a **minimum required level**; failure to meet it indicates underperformance of the NAP. These KPIs are published annually in a standalone document and then imported into the NRA model as **NRA KPI Specifications**.

As high-level references, NRA KPI Specifications are *not* linked directly to architecture objects. Instead, they serve as sources for derived **Requirements**, which are explicitly linked to relevant NRA components.

\> **Specification → Requirement → NRA Object** \> This structured linkage ensures clarity, traceability, and adaptability in the model.

  - A single NRA KPI Specification may lead to one or more Requirements

  - Some Specifications may not yield any Requirements if they are not applicable within the NRA's scope

# KPI Structure in the EA Model

  - NLKF KPIs are maintained in the EA model under: Supplements\\Specifications\\KPI Framework.

  - The folder structure mirrors the NLKF KPI categorization, with each category represented as a subfolder. Each category package carries the Alias “K.n Category name” (K.1–K.7), printed as the chapter heading in the documentation; the packages are ordered by category number.

  - Each KPI is created as a **Specification** object. Its name matches the original KPI name. Keywords are not used for KPI Specification objects; their Requirements carry the Keywords “Requirement”.

![](media/02%20NRA%20KPI%20guideline/image1.png)

# Modelling KPIs in the NRA

Each KPI Specification is taken over from the NLKF document as follows:

  - Name: ID and name of the KPI as in the NLKF document, e.g. “KPI 1.19 Web performance – (meta)data load time”.

  - Notes: a short description of the purpose of the KPI.

  - Linked document: the complete KPI text copied 1:1 from the NLKF document as rich text (RTF), including the question, the supporting notes, the table of options or values and the minimum acceptable value for interoperability.

The KPI text is inserted in the same way as the communication requirements of an Interface (linked document in RTF). The table is not rewritten into text, so the model keeps the KPI text identical with the NLKF version, and a new NLKF version replaces the linked document as a whole. The documentation prints the linked document of each KPI Specification.

![](media/02%20NRA%20KPI%20guideline/image2.png)

# Managing Requirements

Some NRA KPIs Specifications result in Requirements that articulate enforceable architectural constraints. **See the Requirement guideline** for:

  - Creating Requirements

  - Placing Requirements in the model

  - Mapping and Linking Requirements to NRA Objects

# KPI Maintenance and Updates

**Trigger:**

Initiated only upon the release of a new NLKF KPI Framework version.

**Version tracking:**

  - The NLKF version is recorded in the tagged value sourceVersion of the KPI Framework package. The package Version field is not used for this (it is not versioned per package, see Guideline 06).

  - It is not propagated into individual KPI or Requirement elements.

  - Each changed KPI Specification and Requirement gets the tagged value revised (approval date of the NRA release); new elements also get since (NRA version).

## Update process:

**For existing KPIs (matched by ID):**

  - Compare definitions and minimum interoperability levels.

  - If changes exist:
    
      - Replace the linked document with the KPI text of the new NLKF version and update the Notes.
    
      - Identify impacted Requirements and NRA objects:
        
          - Remap or unmap as appropriate.
        
          - Adjust object definitions to align with the updated KPI.

**For deprecated KPIs (present in NRA, missing in NLKF):**

  - Move the NRA KPI and its Requirements to the package “Obsolete KPIs” (not published) and remove their «fulfilled by» links. Delete them only in the next MAJOR version of the NRA (see Guideline 06).

**For new KPIs (present in NLKF, missing in NRA):**

  - Create a new NRA KPI Specification and follow full modelling, mapping, and linking steps described in Sections 2–5.
