<!-- Generated from "04 NRA Interfaces guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This guideline outlines how Interfaces are worked with, curated, classified, stored, and maintained within the NRA model in Enterprise Architect (EA). Interfaces form a traceable knowledge base and serves as sources for modelled Requirements, Information Objects and Specifications.

**Audience:** NRA maintenance team.

| Version | Author      | Note                                                                                                                 |
| ------- | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Petr Bureš  | Revised, simplified structure of the Interface, added requirements, Information object and Specification connection. |
|         | Darko Illic |                                                                                                                      |

# Scope

This guideline covers:

  - Content of the Interface and how it is linked to the other NRA objects

# Role of Interface in the NRA

**Definition**: a point where two systems, subjects, organizations, etc. meet and interact.

In FRAME the interfaces connections to the Architecture and its content is not specified.

In the NRA **the interface is a central point** of the communications view, attached to the physical data flow, connecting two components of the system (subsystems or modules). The intention of the Interface is to describe the use of the interface, classify it, analyse its connection and safety requirements, to identify (connect) relevant requirements, specifications and information objects.

# Modelling Interfaces in the NRA

## Naming Convention

Interface names follow this format:

  - A meaningful name focusing on the main interface purpose

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
    
      - **maximum delay** \[s\]: the acceptable latency of the message (urgency)
    
      - **message interval** \[s\]: how often message needs to be transmitted
    
      - **security level** \[-\]: what is the needed security level for the transmitting

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

### Assessing acceptable max delay in a functional dataflow

In this part we assess what is the maximum acceptable delay between start and end of the transaction carrying the data item. It comprises of data transfer, reception, processing and response, there could be intermediate communication between the parties. This parameter assesses what is the typical delay that is perceived as waiting too long, e.g. what could be harmful to the connected systems, what could be bad as perceived by a human connected to interface (and waiting for the response). If the data flow is broken down to 2 ways of communication, e.g. req...

The allowable delay from when data is generated to when it is utilized. Based on the urgency, potential pre-actuality \[1\]of the data and type of data. For highly dynamic data like incident, accidents or status information (travel times) is this value rather low, while for some static data updates it could be days

This is critical parameter that together with message size defines initial bandwidth requirements.

  - **Result**: a number in ms, s, min defining acceptable waiting time of the initiating party till the transaction is completed.

  - **Examples**: for data type “request” = light weight, e.g. 0,1 s for the reaction to a query

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

### Security

TODO description:

From darko:

After consolidation with Sara Linhas we would propose the following security levels:

**None**: Public information with no security requirements.

**Low**: Data that requires protection against unauthorized changes and no identification for access.

**Medium**: Data that requires protection against unauthorized changes and identification before access .

**High**: Data that needs to be protected against unauthorized reading and indentification before access, often using encryption

From sara:

From: sara: <span class="underline">From medium Security Level, it is advisable to require multi factor authentication (MFA</span> ~~(~~ <span class="underline">- via OIDC/OAuth2) to authorize all credential changes, machine-account issuance to reduce account-takeover risk, for administrative actions (role grants, machine user creation) and block changes without recent re-auth.</span>

**None**: Public information with no security requirements.

**Low**: Data that requires protection against unauthorized changes and identification before use.

**Medium**: ???

**High**: Data that needs to be protected against unauthorized reading, often using encryption

  - **Result**: a label **None, Low, Medium, High** depending on the data sensitivity

  - **Examples**: for data type “request” in functional dataflow describing metadata search it Low security.

### Combining the values

For the interface the overall values must be assessed.

  - Minimum message interval / factor gives overall inter message gap

  - Minimum data rate per link is MAX SIZE / MAX Delay \* factor

## Communications Requirements example

> ![](media/04%20NRA%20Interfaces%20guideline/image1.png)
> 
> Figure 1 Example of Communication Requirements

# Connecting Interface to other NRA objects

The Interface is specified by its description, communication requirements, physical data flow – triplet (subsystem/module – data flow – subsystem/module) and by:

  - Recommendations linked to the Interface: Specifications linked directly are not mandatory, they serve as a good example

  - Requirement(s) linked to the Interface: Specifications linked to the Interface via requirements yield mandatory requirements (either form the law or by decision of the NAPCORE)

  - Information Object(s) linked to the Interface: if there is specific information object known (described, e.g. per legislative requirement) it can be linked to the Interface.

![](media/04%20NRA%20Interfaces%20guideline/image2.png)

# Open questions

  - Could the physical rata flow be linked with more interfaces? E.g. different types?

<!-- end list -->

1.  Data are available before the situation occurs (e.g. planed roadworks, new road, etc.)
