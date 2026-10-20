<!-- Generated from "02 NRA KPI guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This document outlines how Key Performance Indicators (KPIs) from the NAP Level of Service KPI Framework (NLKF) are transferred, modelled, and maintained within the Enterprise Architect (EA) model of the NAP Reference Architecture (NRA).

**Audience:** NRA maintenance team.

| Version | Author                      | Note                                                                              |
| ------- | --------------------------- | --------------------------------------------------------------------------------- |
| 1.0     | Petr Bureš, Benjamin Witsch | Revised, connection to NRA objects via Requirements and updated folder structure. |

# Scope

This guideline covers:

  - How NLKF KPI Specification objects are maintained in EA

  - Structure, classification, foldering, and linkage

  - Excludes:
    
      - Other specifications then KPIs (see Guideline 1)
    
      - Requirements derived from Specifications (see Guideline 3)

# Role of NKLF KPI Specifications in the NRA

**NLKF KPIs are modelled as Specification objects in the NRA.** They represent performance expectations defined by the *NAP Level of Service Key Performance Indicators Framework*, developed by NAPCORE. Each KPI contributes to the overall assessment and scoring of a National Access Point (NAP).

Most NLKF KPIs define a **minimum required level**; failure to meet it indicates underperformance of the NAP. These KPIs are published annually in a standalone document and then imported into the NRA model as **NRA KPI Specifications**.

As high-level references, NRA KPI Specifications are *not* linked directly to architecture objects. Instead, they serve as sources for derived **Requirements**, which are explicitly linked to relevant NRA components.

\> **Specification → Requirement → NRA Object** \> This structured linkage ensures clarity, traceability, and adaptability in the model.

  - A single NRA KPI Specification may lead to one or more Requirements

  - Some Specifications may not yield any Requirements if they are not applicable within the NRA's scope

# KPI Structure in the EA Model

  - NLKF KPIs are maintained in the EA model under: Supplements\\Specifications\\KPI Framework.

  - The folder structure mirrors the NLKF KPI categorization, with each category represented as a subfolder.

  - Each KPI is created as a **Specification** object. Its name matches the original KPI name.

![](media/02%20NRA%20KPI%20guideline/image1.png)

# Modelling KPIs in the NRA

Each KPI Specification includes:

  - ID and Name

  - Description and supporting notes

  - Options or choices (if applicable)

  - Minimum acceptable threshold (for interoperability)

![](media/02%20NRA%20KPI%20guideline/image2.png) ![](media/02%20NRA%20KPI%20guideline/image3.png)

# Managing Requirements

Some NRA KPIs Specifications result in Requirements that articulate enforceable architectural constraints. **See the Requirement guideline** for:

  - Creating Requirements

  - Moving requirement in the model

  - Mapping and Linking Requirements to NRA Objects

# KPI Maintenance and Updates

**Trigger:**

Initiated only upon the release of a new NLKF KPI Framework version.

**Version tracking:**

  - The version is recorded at the **KPI Framework package** level in EA.

  - It is not propagated into individual KPI or Requirement elements.

## Update process:

**For existing KPIs (matched by ID):**

  - Compare definitions and minimum interoperability levels.

  - If changes exist:
    
      - Update the NRA KPI content.
    
      - Identify impacted Requirements and NRA objects:
        
          - Remap or unmap as appropriate.
        
          - Adjust object definitions to align with the updated KPI.

**For deprecated KPIs (present in NRA, missing in NLKF):**

  - Delete the NRA KPI and all related Requirements and mappings.

**For new KPIs (present in NLKF, missing in NRA):**

  - Create a new NRA KPI Specification and follow full modelling, mapping, and linking steps described in Sections 2–5.
