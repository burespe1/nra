<!-- Generated from "04 NRA Interfaces guideline - v1.2 draft.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This guideline outlines how Interfaces are worked with, curated, classified, stored, and maintained within the NRA model in Enterprise Architect (EA). Interfaces form a traceable knowledge base and serves as sources for modelled Requirements, Information Objects and Specifications.

**Audience:** NRA maintenance team.

| Version | Author                    | Note                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Petr Bureš                | Revised, simplified structure of the Interface, added requirements, Information object and Specification connection.                                                                                                                                                                                                                                                                                                       |
|         | Darko Illic               |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1.1     | Petr Bureš, Claude        | After the 2.2.0 model update: Keywords, documentation template, link types. Approved on 20 October 2026.                                                                                                                                                                                                                                                                                                                   |
| 1.2     | Claude (draft for review) | Proposal after the interface review (A10): security of the physical data flow by confidentiality, integrity and availability with the ARC-IT security classes 1–5, authentication and encryption; maximum delay split into response time and transfer time; concurrency factor per functional data flow; data categories; sizes compressed / uncompressed and table layout; examples and rules taken over from revision 2. |

# Scope

This guideline covers:

  - Content of the Interface and how it is linked to the other NRA objects

# Role of Interface in the NRA

**Definition**: a point where two systems, subjects, organizations, etc. meet and interact.

In FRAME the interfaces connections to the Architecture and its content is not specified.

In the NRA **the interface is a central point** of the communications view, attached to the physical data flow, connecting two components of the system (subsystems or modules). The intention of the Interface is to describe the use of the interface, classify it, analyse its connection and safety requirements, to identify (connect) relevant requirements, specifications and information objects.

The Interface describes the communication context. Implementation details – protocols, API design, validation or retry mechanisms – are not part of its description; where they are needed they are recorded as Requirements or Recommendations linked to the Interface.

# Modelling Interfaces in the NRA

## Naming Convention

Interface names follow this format:

  - A meaningful name focusing on the main interface purpose

  - Keywords set to “Interface”; the documentation prints each Interface with its physical data flows and linked Requirements (template NC\_NN\_NNN\_PV).

## Interface Content

Each Interface object must include:

  - **Identification** – abbreviation and long name of the interface, usually by referring to objects connected via the interface.

  - **Type** – Clearly classify the specification into one of the defined types (User Interface, Programming Interface or Hardware Interface)

<!-- end list -->

  - **Description** –a paragraph or more of description of the interface + how the interface is used in the context of the ITS Service.

<!-- end list -->

  - **Related documents** – Information about additional documents further specifying the Interface, full name of the document where in the interface specified and a hyperlink to the text.

  - **Communication requirements** (per functional data flow)
    
      - **data type**: what type of data are being transmitted
    
      - **size of message** \[B\]: the maximum expected size of the message
    
      - 
      - maximum response time \[s\]: the time until the other party starts to respond (first byte or acknowledgement)
    
      - maximum transfer time \[s\]: the time until the whole content is transferred and the transaction is closed; it determines the data rate
    
      - **message interval** \[s\]: how often message needs to be transmitted
    
      - concurrency factor \[-\]: how many users or systems are expected to use the functional data flow at the same time (assessed per functional data flow)
    
      - 
  - Security of the physical data flow (once per Interface, not per functional data flow): confidentiality, integrity and availability, security class, authentication and encryption – see Security.

## Interface type 

  - **User Interface (UI)**: The space where interactions between humans and machines occur. This includes graphical elements like buttons, icons, and menus in software applications.

  - **Programming Interface**: In software development, an interface defines a set of methods or functions that a class or system must implement, enabling different software components to interact.

  - **Hardware Interface**: The physical and logical connections between different hardware components, such as USB ports or network interfaces.

# Communications Requirements analysis

**The goal of a**nalysis of communication requirements **is to** identify the characteristics of the physical links that will carry the data, to allow safe and secure sizing of the connection. Typical question is “**What is the type of data that is passing over this link?”** yielding answers to

  - What is required bandwidth by answering sub questions: how often data is updated, how quickly they must be available, what is their maximal size, how many users are expected to access it at the same time

  - What is required security by assessing the importance of the data and importance of unintended modification and access to data.

Analysis of communication requirements constitutes analysis of each and individual **physical dataflow**. Since this could be different per functional dataflow, this analysis is **performed for each functional dataflow** of the physical dataflow. Resulting information is the maximum of each analysed functional dataflow.

**NOTE**: Sometimes even the functional dataflow is too generic and needs to be broken down into parts that have different needs.

## The process of Data Flow Analysis 

### Assessing type of data 

Inspect all functional data flows in the interface, to get info what "**data items**" is passed over there, use common sense and your experience with what "**data items**" shall be passed over in this interface, There could be more types of data, it could just be a response to a request.

  - **Result**: identification and very short description of the data being carried by the analysed functional data flow.

  - **Examples**: static road network information, dynamic travel and traffic information, request, acknowledgement, ...

### Assessing maximum size of a functional dataflow

In this part we examine all identified “data items” within the functional data flow and try to assess its maximal size. The maximal size here is expert expectation of a LIMITED quantity – it must be justifiable in the framework of the NAP. This is a key entry to the bandwidth analysis.

 **MAXIMUM size Is** without real outliers of the data items. It is a value with which a NAP should be able to work in expected range of parameters. Should the size increase, the NAP must still be operational – but some other parameters (e.g. latency) could be affected). The correct value of the maximum size allows system designers to properly size the implementation = too low and system will be lagging. Too big and there will be wasted resources.

  - **Result**: a number in kB, MB, GB defining acceptable size of the data objects in the functional dataflow. identification and very short description of the data being carried by the analysed functional data flow.

  - **Examples**: for data type “request” = this is light-weight data object, with no data content, therefore it shall be small, usually carrying credentials = 1 kB

  - Data are described by category, each in its own row of the table: static data change about every 3 months (e.g. road network), semi-static data about once a week and have a size similar to static data, dynamic and status data are provided as snapshots updated on every change or periodically (typically every 5 minutes).

  - Where compression is mandatory, the size of data is given as a pair compressed / uncompressed (e.g. snapshot of traffic events 3 MB / 52 MB, national road network 285 MB / 1,900 MB); traffic and network data compress well, typically 1:7 to 1:30. Sizes of requests, responses and other messages without a second value are uncompressed.

### 

### Assessing response time and transfer time in a functional dataflow

Two values are assessed. The response time is the time until the other party starts to respond (first byte or acknowledgement); it is what a user or a connected system waits for and is typically 0.1–1 s. The transfer time is the time until the whole content is transferred and the transaction is closed; it determines the required data rate and may be much longer for large content.

In this part we assess what is the maximum acceptable delay between start and end of the transaction carrying the data item. It comprises of data transfer, reception, processing and response, there could be intermediate communication between the parties. This parameter assesses what is the typical delay that is perceived as waiting too long, e.g. what could be harmful to the connected systems, what could be bad as perceived by a human connected to interface (and waiting for the response). If the data flow is broken down to 2 ways of communication, e.g. req...

\[1\]pdates it could be days

This is critical parameter that together with message size defines initial bandwidth requirements.

  - **Result**: a number in ms, s, min defining acceptable waiting time of the initiating party till the transaction is completed.

  - **Examples**: for data type “request” = light weight, e.g. 0,1 s for the reaction to a query

  - Typical transfer times: request, acknowledgement or “not modified” answer 0.1 s; metadata page 2 s; metadata harvesting 10 s; snapshots of dynamic and status data 3 s – a consumer polling every 30 s needs a changed snapshot at once; static and semi-static data and uploads 60 s for 1.5 GB compressed / 10 GB uncompressed – users have problems with downloads that take too long; 60 s corresponds to 25 MB/s per transfer, which a common business connection and a NAP server with a 1 Gbit/s link can provide. Large uploads are acknowledged within the response time and processed asynchronously.

  - The timeliness of the data – from an event to its availability at the NAP – is a quality requirement of the data (Requirements, KPIs), not a parameter of the Interface.

### Interval between messages

**interval between messages,** what you could expect as a system e.g. a combination of an estimation of how often one would need to get this with estimation of how many users would want it at the same time.  e,g, querying metadata (guess 1 by 60 minutes? users 60? =  interval 1 minute. The number of estimated users is in the note of the interface. It is largely based on type of data being transferred, for a statis data the interval could be ½ year. For dynamic data, few seconds.

Specifies the frequency with which the <span class="underline">data items are generated</span>. The message generation is periodical or in expected.

This is critical parameter that together with message size defines initial bandwidth requirements.

  - **Result**: a number in seconds, minutes, hours, months, years defining how often we expect the message to repeat.

  - **Examples**: for data type “request” in functional dataflow describing metadata search it is very hard to guess, we need to come with a number combining requests of a person = e.g. 5 minutes

### Factor

This is an expectation of multiple identities requesting the data, accessing the functionality at the same time. For the static data download there is low probability of concurrent downloaders, however for dynamic the concurrency becomes an issue.

This is critical parameter that multiplies previous values by a factor.

  - **Result**: a number of concurrent accesses that are being served and the same time and share their latency requirements.

  - **Examples**: for data type “request” in functional dataflow describing metadata search it is very hard to guess, lest say = it is for service providers, so an expected number not all of them trying to fit in the same message interval, guess 10 for metadata.

  - The concurrency factor is assessed per functional data flow, because it differs by data type: static data downloads 1–2, snapshots of dynamic data polled by the registered systems of content consumers 5, uploads by content providers 1.

### Security

  - 
  - 
Security is assessed once for the physical data flow of the Interface, not for each functional data flow. The approach follows ARC-IT, the US National ITS Reference Architecture, which rates confidentiality, integrity and availability of information flows according to FIPS 199.

  - **Confidentiality** High: disclosure poses a substantial risk to the operation of the NAP or to safety. Moderate: personal data, credentials, commercially sensitive or non-public data. Low: data intended for publication.

  - **Integrity** High: falsified data directly affect safety or mobility, or are distributed from the NAP to all consumers. Moderate: an error misleads the user but can be detected. Low: the data are not used directly for decisions.

  - **Availability** High: an outage endangers safety (not expected for a NAP). Moderate: consumers rely on the flow continuously. Low: the data are not needed for immediate decisions.

Each property of the physical data flow takes the highest level found in its functional data flows.

The Interface is assigned the lowest ARC-IT security class (confidentiality / integrity / availability) that meets all three levels and exceeds them in no more than two properties:

  - Class 1: Low / Moderate / Moderate

  - Class 2: Moderate / Moderate / Moderate

  - Class 3: Moderate / High / Moderate

  - Class 4: High / High / Moderate

  - Class 5: High / High / High

Two flags complete the assessment. **Authentication** – required when the flow needs the identification of the user or system (account, API key). **Encryption** – required when confidentiality is Moderate or higher or credentials are transmitted, otherwise recommended.

  - Result: confidentiality, integrity and availability levels, security class, authentication and encryption, with a one-sentence rationale.

  - Example: Machine Data Access – Low / High / Moderate, security class 3; authentication required; encryption required; dynamic data (SRTI, RTTI) affect safety and mobility and consumers rely on the feed continuously.

Security measures such as multi-factor authentication for credential changes are recorded as Requirements or Recommendations, not as security levels. In the model the values are stored as tagged values of the Interface: Confidentiality, Integrity, Availability, SecurityClass, Authentication, Encryption.

### Combining the values

For the interface the overall values must be assessed.

  - 
  - 
  - Minimum inter-message gap = smallest (message interval / concurrency factor) of the functional data flows

  - Minimum data rate for link = largest (maximum size / maximum transfer time × concurrency factor) of the functional data flows

Example (Machine Data Access): max(1.5 GB / 60 s × 2; 3 MB / 3 s × 5; 2 MB / 3 s × 5) = max(50; 5; 3.3) = 50 MB/s (static and semi-static data 1.5 GB compressed); inter-message gap 30 s / 5 = 6 s (snapshots polled every 30 s).

## Communications Requirements example

The table starts with a title row naming the physical data flow and lists for each functional data flow its content, maximum size per message (compressed / uncompressed), maximum response time and maximum transfer time in seconds, message interval and concurrency factor, followed by the rows Minimum data rate for link and Minimum inter-message gap. The security of the physical data flow follows the table. Figure 1 shows the table of the interface Machine Data Access.

> ![](media/04%20NRA%20Interfaces%20guideline%20-%20v1.2%20draft/image_a10.png)
> 
> 1

# Connecting Interface to other NRA objects

The Interface is specified by its description, communication requirements, physical data flow – triplet (subsystem/module – data flow – subsystem/module) and by:

  - Recommendations linked to the Interface: Specifications linked directly are not mandatory, they serve as a good example

  - Requirement(s) linked to the Interface: Specifications linked to the Interface via requirements yield mandatory requirements (either form the law or by decision of the NAPCORE)

  - Information Object(s) linked to the Interface: if there is specific information object known (described, e.g. per legislative requirement) it can be linked to the Interface.

  - Requirements are linked with «fulfilled by» from the Requirement to the Interface, as for all other NRA objects (see Guideline 03 and Guideline 07).

  - A physical data flow is linked to more than one Interface only when the communication contexts, the security or the parameters of its functional data flows differ substantially; otherwise one Interface covers it.

![](media/04%20NRA%20Interfaces%20guideline%20-%20v1.2%20draft/image2.png)

# 

  - 
<!-- end list -->

1.  Data are available before the situation occurs (e.g. planed roadworks, new road, etc.)
