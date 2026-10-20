<!-- Generated from "01 NRA specifications guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This guideline outlines how legal, technical, and advisory specifications are curated, classified, stored, and maintained within the NRA model in Enterprise Architect (EA). Specifications form a traceable knowledge base and serve as sources for modelled Requirements that connect to NRA architecture components.

**Audience:** NRA maintenance team.

| Version | Author             | Note                                                                                                                                                                                                                                                                               |
| ------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Petr Bureš         | Revised, simplified structure of the Specification, added requirements connection.                                                                                                                                                                                                 |
| 1.1     | Petr Bureš, Claude | After the 2.1.0/2.2.0 model update: Keywords per type, sourceVersion, global issue link, deprecation aligned with model versioning (Guideline 06). Open questions resolved: Technical Specifications and Recommendations are linked via Requirements. Approved on 20 October 2026. |

# Scope

This guideline covers:

  - All Specification objects maintained in EA

  - Structure, classification and linkage

  - Excludes:
    
      - Specifications derived from KPIs (see Guideline 2)
    
      - Requirements derived from Specifications (see Guideline 3)
    
      - Versioning and change management of the model (see Guideline 06) and modelling conventions (see Guideline 07)

# Role of Specifications in the NRA

Specifications are modelled to represent formal, external documents (legal acts, standards, guidance) relevant to the NRA. These are high-level sources and are **not directly linked** to architecture objects. Instead, **Requirements** are derived from them to establish traceable constraints and obligations in the model.

\> **Specification → Requirement → NRA Object** This layered linkage supports flexibility, traceability, and clarity.

  - A single Specification may yield multiple Requirements

  - Some Specifications may yield no Requirements if not applicable to the architecture

# Specification Folder Structure

Specifications are maintained in: Supplements\\Specifications and Recommendations

Subfolders represent specification categories:

  - **Legal** – EU directives, regulations, implementing acts

  - **Technical** – e.g., DATEX II, NETEX, SIRI

  - **Recommendation** – NAPCORE guidance, industry good practices

  - **Profiles** – Data model profiles

  - **KPI Framework** – References to NLKF guidance

  - **Superseded** – Deprecated specs with trace links retained

![](media/01%20NRA%20specifications%20guideline/image1.png)

# Modelling Specifications in the NRA

## Specification Content

Following structure describe and document specifications:

  - **Short Name** Concise title used in diagrams, lists, or references. Typically an abbreviation or a commonly recognized term.

  - **Full Name** Official, unabbreviated name of the specification.

  - **Link** URL linking directly to the official source document or specification repository.

  - **Type** Classification of the specification, selected from the following: *Legal*, *Technical*, *Recommendation*, *Profile*, *KPI*.

  - **Keywords** The EA Keywords field carries the type label printed in the documentation: “Legal Specification”, “Technical Specification”, “Recommendation”, “Profile”. Keywords are mandatory; tools/check.py reports specifications without them.

  - **sourceVersion** Tagged value with the version or date of the external document the model reflects (e.g. “3.6” for DATEX II, “2024” for an NLKF edition). Optional, but recommended for Technical Specifications and Profiles.

  - **Description** A brief summary of the specification’s purpose and scope. If the specification supersedes a previous version, highlight the key changes or improvements.

  - **Additional Context** Explanation of the specification’s relevance within the system landscape (e.g. its role in the NAP ecosystem). Include noteworthy attributes, constraints, or expected benefits that are valuable for implementers or stakeholders.

  - **Related Resources** A curated list of associated documents that further explain, support, or operationalize the specification. May include:
    
      - Delegated regulations and legislative texts
    
      - Parts or modules of the standard
    
      - Implementation guidelines and manuals
    
      - Evaluation or summary reports
    
      - Informative web articles and official portals
    
      - Schema repositories, technical tools, or open-source software

  - Each ‘**Related Resources**’ entry should include:
    
      - **Short name** (hyperlinked if available)
    
      - **Brief description** outlining the document’s role or content

## Naming Convention

Specification names follow this format:

  - **Prefix**: L (Legal), S (Standard), R (Recommendation), KPI, P (Profile)

  - **Document number or version**: e.g. L1, S\_CEN14589

  - **Descriptive label**: e.g. "ITS Directive" or "Traffic Info Standard"

Example: *L8 Directive (EU) 2023/2661 - ITS (recast)*

**Important rule**: Assigning the prefix and number (e.g. L1, KPI 1.3) is important ONLY for the identification of Requirements, the naming convention of requirements rely on these prefixes. So the numbering is arbitrary and does not carry any meaning.

## Compaction Rule

Model only one Specification object per series or legislative act, regardless of the number of parts. For instance, the DATEX II suite is represented by a single object.

## Linking & Hierarchy

Specifications are arranged in this hierarchy (when applicable):

  - Directive → Delegated Regulation → Standard → Profile

**Connectors:**

  - **Realization**: from Regulation to its Directive

  - **Usage**: from Standard to the Regulation it implements

  - **Usage**: from Profile to the Standard, it extends

  - **Substitution**: from new Specification to repealed Specification

![](media/01%20NRA%20specifications%20guideline/image2.png)

\> Direct connections to NRA architecture objects are *not* used—those are managed via Requirements (see Guideline 3)

Technical Specifications and Recommendations follow the same Specification → Requirement → NRA Object rule. A direct Dependency from a Recommendation to an Interface is allowed as an informative link (see Guideline 04); it is not printed as a requirement.

# Working with Requirements 

Some Specifications result in Requirements that articulate enforceable architectural constraints. **See the Requirement guideline** for:

  - Creating Requirements

  - Placing Requirements in the model

  - Mapping and Linking Requirements to NRA Objects

**Important rule**: If the Specification does not yield any Requirement then it shall be linked to a global issue “Does not yield a Requirement”. The issue is kept in Supplements\\Issues\\Legal issues; link the Specification to it with an Association. tools/check.py warns about every Specification that has neither a Requirement (Abstraction or Usage) nor this link.

# Specification Maintenance and Updates

## Trigger

Initiated during major updates, or when external specifications are revised.

## Version Tracking

Specifications themselves are **not versioned**. Use related metadata or document references for version awareness. The version of the external document is recorded in the tagged value sourceVersion; a change of the model element itself is recorded by the tagged values revised and since (see Guideline 06).

## Update Procedure

This procedure outlines how to maintain the specification registry when changes occur, ensuring all links and dependencies remain accurate and up to date.

**📌 When an Existing Specification Is Updated**

  - **Review** the content of the updated specification.

  - **Update** the metadata and description fields to reflect the changes.

  - **Verify all linked Requirements and Issues**:
    
      - **Revise** or **retire** Requirements that are no longer valid.
    
      - **Remap** or **unmap** impacted NRA components accordingly.

**🗂 When a Specification Is Deprecated**

  - **Move** the deprecated specification to the *Superseded* folder.

  - **Relink downstream Requirements and NRA mappings** to the replacement Specification.
    
      - If no direct replacement exists:
        
          - **Assess** each Requirement and mapping:
            
              - Can it be mapped to a different specification?
            
              - Is it now redundant due to other existing Requirements?
            
              - If not, create an empty placeholder object titled **“Generic Specification”** and map the Requirement there.

  - **Create a trace link** to any Specification that supersedes or replaces the deprecated one.

  - Keep the deprecated Specification in the Superseded folder at least until the next MAJOR version of the NRA; deleting it is a breaking change and is recorded in the Change Protocol (see Guideline 06).

**➕ When a New Specification Becomes Relevant**

  - **Add** the Specification to the appropriate domain-specific subfolder.

  - **Apply modeling rules** outlined in Sections 4–5.

  - **Derive and link Requirements** based on the Specification’s content and scope.

# Specification examples

This structure ensures that each specification is clearly identified, classified, and described, making it easier to reference and understand its context and use.

## Legal specification

### RTTI Delegated regulation

**Short name:** Regulation (EU) 2015/962 - RTTI

**Type**: Legal

**Full Name:** Commission Delegated Regulation (EU) 2015/962 of 18 December 2014 supplementing Directive 2010/40/EU with regard to the provision of EU-wide real-time traffic information services

**Link:** <https://eur-lex.europa.eu/eli/reg_del/2015/962/oj>

**Description:** This regulation defined the initial technical specifications for the provision of EU-wide real-time traffic information (RTTI) services under Directive 2010/40/EU. It established requirements for the availability, accessibility, exchange, and re-use of static and dynamic road traffic data. It introduced the concept of a minimum level of service and required Member States to designate National Access Points (NAPs) for data publication. The regulation was repealed with effect from 31 December 2024 and replaced by Regulation (EU) 2022/670, which introduced updated data categories, performance requirements, and alignment with current ITS deployment practices.

**Additional details:** NAPs were required to provide machine-readable access to RTTI-relevant datasets, including road network attributes, traffic regulations, and real-time traffic status. The regulation mandated metadata publication, data quality assurance, and use of harmonised formats to support cross-border interoperability. It served as the legal foundation for early RTTI deployments and was superseded to reflect evolving data models and service expectations.

**Related Documents:**

  - [Regulation (EU) 2022/670](https://eur-lex.europa.eu/eli/reg_del/2022/670/oj) – Successor regulation introducing revised RTTI specifications.

  - [European Commission RTTI Guidance](https://transport.ec.europa.eu/transport-themes/smart-mobility/road/its-directive-and-action-plan/safety-related-traffic-information-srti-real-time-traffic-information-rtti_en) – Implementation context and technical interpretation.

  - [DATEX II Reference Profile for RTTI](https://docs.datex2.eu/recommended-profiles/rrp/rtti/) – Defines the harmonised data model for compliant RTTI data exchange.

  - [NAPCORE RTTI Workstream Summary (PDF)](https://napcore.eu/wp-content/uploads/2025/05/DD_2022_670.pdf) – Overview of Member State alignment and implementation under the updated regulation.

## Technical standards

### GBFS

**Short name**: General Bikeshare Feed Specification (GBFS)

**Type: Technical Standard**

**Full Name: General Bikeshare Feed Specification (GBFS)**

**Link: <https://www.gbfs.org/>**

**Description: GBFS is an open, real-time data standard for shared mobility systems (e.g. bikeshare, scooters, mopeds). It defines a uniform JSON-based structure for publishing system status, vehicle availability, pricing, and station metadata. GBFS is designed for public consumption by trip planners, mobility apps, and data aggregators. It is read-only and does not support transactional operations.**

**Additional details: -**

**Related Documents:**

  - **[GBFS GitHub Repository](https://github.com/MobilityData/gbfs) – Specification source, schemas, governance model.**

  - **[GBFS v3.0 Specification](https://github.com/MobilityData/gbfs/blob/master/gbfs.md) – Latest stable version with feed definitions and field requirements.**

  - **GBFS Validator Tool – Online tool for schema validation and feed diagnostics.**

  - **[GBFS Systems Catalog](https://github.com/MobilityData/gbfs/blob/master/systems.csv) – List of known GBFS-compliant deployments.**

  - **[<span class="underline">GBFS website</span>](https://gbfs.org/): GBFS specification web site**

## Recommendations

### MQA Methodology

**Short name**: MQA Metadata Quality Assessment Methodology

**Type**: Recommendation

**Full Name:** Metadata Quality Assessment Methodology.

**Link:** <https://data.europa.eu/mqa/methodology?locale=en>

**Description** The Metadata Quality Assessment (MQA) is a tool developed by the consortium of data.europa.eu to study the quality of metadata harvested by data.europa.eu. It is intended to help data providers and data portals to check their metadata quality and to receive suggestions for improvements. The results are presented via the MQA and are also available as download. In the following we describe the functionality of the MQA and the methodology it uses.

**Additional details**: The NAPs are encouraged to follow this methodology since it would allow better interoperability between NAPs. There is also SHACL validator available <https://data.europa.eu/mqa/shacl-validator-ui/data-provision>. Norwegian NAP has implemented this methodology, see <https://transportportal.no/> in any of the catalogue records.

**Related Documents**: -

# Annex

![](media/01%20NRA%20specifications%20guideline/image3.png)
