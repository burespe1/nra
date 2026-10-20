<!-- Generated from "03 NRA Requirements guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** To define how Requirements are derived from Specifications and used as the formal layer for constraining and informing NRA architecture elements.

**Audience:** NRA maintenance team.

| Version | Author                      | Note                                                                                                                                                                                                                 |
| ------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Petr Bureš, Benjamin Witsch | Revised, connection to Specifications, moved from other guidelines here.                                                                                                                                             |
| 1.1     | Petr Bureš, Claude          | After the 2.2.0 model update: single location Supplements\\Requirements, Unresolved package, naming check, RequirementLevel, multi-object fulfilment. Requirement level rule confirmed. Approved on 20 October 2026. |

# Scope

This guideline covers:

  - How Requirements objects are maintained in EA

  - Structure, classification, foldering, and linkage

  - Excludes: How specifications are created and maintained (see Guideline 1 and 2)

  - Repeats how Requirements are derived from Specifications

# Role of Requirements in the NRA

Requirements:

  - Translate high-level spec content into model-relevant obligations

  - Are actionable and understandable within the architecture context

  - Form the only linkage between Specification and architecture object

# Requirements Structure in the EA Model

  - Requirements are maintained in the EA model only under Supplements\\Requirements, in the packages Legal Requirements, KPI Framework (one subpackage per KPI category) and Unresolved. The model documentation prints them from there.

  - The package Unresolved holds Requirements not yet linked to the architecture; it is not published. The view folders “Specifications & Requirements” are not used and are removed from the model.

  - Each Requirement is created as a **Requirement** object. Its name is derived from the specification that yielded the requirement. The Keywords field is set to “Requirement”.

# Modelling Requirements in the NRA

## When to Create a Requirement

  - **Do create** when a Specification includes actionable clauses or obligations

  - **Do not create** if the Specification only provides context or non-binding content (e.g., thresholds labelled “no feature”)

## How to create a Requirement

  - Create the Requirement in the Specifications view by dragging empty Requirement,

  - Fill in the requirement from the Specification and

  - Link it to the **Specification** using the **Abstraction** association

## Naming Convention:

Format:

  - Prefix from source Specification (L1, S1, KPI 3.2)

  - Number within the Specification (L.1.1, S.1.2, K.3.2.1 etc. – insert a bullet after the letter, for KPI shorten to K, remove any blanks)

  - Optional short label (e.g. "Establishment of NAP", “Load time web site”)

  - Requirements are ordered numerically in the project browser (K.1.9.1 before K.1.10.1).

\> One Requirement may reference multiple Specifications if relevant

![](media/03%20NRA%20Requirements%20guideline/image1.png)

## Requirement Content

Each Requirement includes:

  - **Name**: Based on KPI or Spec reference (e.g., K.1.3.1 Latency Threshold – a space, not a dash, separates the number and the label; tools/check.py checks the pattern)

  - **Description**: Clearly worded obligation or constraint. One clear “SHALL” style clause OR a list of items that must be fulfilled (e.g. list of data types to be published). Exception for KPIs:
    
      - A single sentence for one-condition thresholds
    
      - A list when multiple options satisfy the threshold

  - **Reference**: Trace link to originating Specification

  - **Source Note**: <span class="underline">Optional</span> note referencing original wording or clause

## Requirement level

The source of a Requirement determines the RequirementLevel of the functions that fulfil it (see Guideline 05):

  - Requirement derived from a Legal Specification: MANDATORY.

  - Requirement derived from a KPI minimum level: MANDATORY for NAPCORE-compliant NAPs.

  - Requirement derived only from optional KPI options or Recommendations: OPTIONAL.

![](media/03%20NRA%20Requirements%20guideline/image2.png) ![](media/03%20NRA%20Requirements%20guideline/image4.png)

## Foldering and Flow

  - Create the Requirement in Supplements\\Requirements\\Unresolved, or drag it onto the diagram of its Specification and move it there.

  - Once it is linked to an NRA object, move it to the package of its source under Supplements\\Requirements (Legal Requirements or the KPI category).

  - Every Requirement left in Unresolved is linked to a global issue (see Exceptions).

# Linking Requirements to NRA Objects

## Mapping logic

To minimize redundancy, a top-down mapping order is followed:

1.  Subsystem

2.  Module

3.  Interface

4.  Actor / Agreement

5.  Function or Datastore

6.  Other objects (if needed)

A Requirement may be fulfilled by more than one object, typically an Agreement (who is obliged) and a Module or Function (how it is done), e.g. L.2.4.

## Linking process

  - Drag the Requirement into the target view.

  - Check for any contradictions:
    
      - Revise the NRA object’s description, or
    
      - Propose an update to the Requirement and the original Specification.

  - Create a “**fulfilled by**” link from the Requirement to the NRA object.

  - Verify the link in the **Traceability** window.

  - Remove the Requirement from the view and move it from Unresolved to the package of its source.

## Exceptions

  - If there is no functionality (NRA content) to satisfy the Requirement then link the Requirement instead to a global issue “**Missing functionality for the Requirement**” (one global issue per gap type with exactly this name; the former issues “Functionality Missing”, “Function missing in the NRA for the KPI” and “Element missing” were merged into it in NRA 2.2.0). Such a Requirement stays in Unresolved.

  - tools/check.py reports as errors every published Requirement without a «fulfilled by» link and every unresolved Requirement without an issue.

## Examples

### Motivational Layer - ITS Service:

  - **Purpose**: Link Requirement that contain general requirements applicable to the entire service. To capture a high-level Requirement

  - **Example**:
    
      - **Specification**: ITS Directive 2010/40/EU
    
      - **Requirement**: to establish a framework for the deployment of ITS in-road transport, ensuring interoperability and continuity of services across the EU.

### Physical View - System/Subsystem/Module:

  - **Purpose**: Link Requirement with tangible technical, performance, or design descriptions that are detailed but not specific to interfaces.

  - **Example**:
    
      - **Specification**: mobilityDCAT-AP
    
      - **Requirement**: Use mobilityDCAT-AP for description of catalogue records. 

### Communications View - Interface:

  - **Purpose**: Link Requirement with data structure, protocol, or performance descriptions relevant to specific interfaces.

  - **Example**:
    
      - **Specification**: Commission Delegated Regulation (EU) 2015/962
    
      - **Requirement**: The interface shall be able to support the exchange of EU-wide real-time traffic information services.

### Organizational View - Agreements:

  - **Purpose**: In Agreements there is already a lot from legal acts – linking to it is natural.

  - **Example**:
    
      - **Specification**: Commission Delegated Regulation (EU) No 886/2013
    
      - **Requirement**: data must be provided free of charge to users

  - **Example**:
    
      - **Specification**: ITS Directive
    
      - **Requirement**: data must be provided in DATEX II format.

### Functional View - Function:

  - **Purpose**: Link Requirement with dominant functional requirements reflected in one or more functions.

### Organizational View - Actors:

  - > **Purpose**: Link Requirement identifying actors or describing activities and responsibilities. Also link actors to Requirement that are of their interest but are not directly relevant to NAP (e.g. standards for data description)
