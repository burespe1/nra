<!-- Generated from "03 NRA Requirements guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** To define how Requirements are derived from Specifications and used as the formal layer for constraining and informing NRA architecture elements.

**Audience:** NRA maintenance team.

| Version | Author                      | Note                                                                     |
| ------- | --------------------------- | ------------------------------------------------------------------------ |
| 1.0     | Petr Bureš, Benjamin Witsch | Revised, connection to Specifications, moved from other guidelines here. |

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

  - Requirements are maintained in the EA model under: Supplements\\Requirements, they also could be found in the folder with original specifications as well as in the views (Open question)

  - The folder structure for the Requirements is not fully developed.

  - Each Requirement is created as a **Requirement** object. Its name is derived from the specification that yielded the requirement.

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

\> One Requirement may reference multiple Specifications if relevant

![](media/03%20NRA%20Requirements%20guideline/image1.png)

## Requirement Content

Each Requirement includes:

  - **Name**: Based on KPI or Spec reference (e.g., K.1.3.1 – Latency Threshold)

  - **Description**: Clearly worded obligation or constraint. One clear “SHALL” style clause OR a list of items that must be fulfilled (e.g. list of data types to be published). Exception for KPIs:
    
      - A single sentence for one-condition thresholds
    
      - A list when multiple options satisfy the threshold

  - **Reference**: Trace link to originating Specification

  - **Source Note**: <span class="underline">Optional</span> note referencing original wording or clause

![](media/03%20NRA%20Requirements%20guideline/image2.png)![](media/03%20NRA%20Requirements%20guideline/image3.png) ![](media/03%20NRA%20Requirements%20guideline/image4.png)

## Foldering and Flow

  - Created often under the associated Specification’s folder

  - Requirements remain in the same folder as their associated Specification (KPI) until moved during the final step.

Once created and linked:

  - Move the Requirement object to the Supplements\\Requirements package.

  - After it’s linked to the relevant NRA object, relocate it to the view-specific View\\Specifications & Requirements subfolder.

# Linking Requirements to NRA Objects

## Mapping logic

To minimize redundancy, a top-down mapping order is followed:

1.  Subsystem

2.  Module

3.  Interface

4.  Actor / Agreement

5.  Function or Datastore

6.  Other objects (if needed)

## Linking process

  - Drag the Requirement into the target view.

  - Check for any contradictions:
    
      - Revise the NRA object’s description, or
    
      - Propose an update to the Requirement and the original Specification.

  - Create a “**fulfilled by**” link from the Requirement to the NRA object.

  - Verify the link in the **Traceability** window.

  - Remove the Requirement from the view and place it in the correct Specifications & Requirements subfolder.

## Exceptions

  - If there is no functionality (NRA content) to satisfy the Requirement then link the Requirement instead to a global issue “**Missing functionality for the Requirement**”

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
