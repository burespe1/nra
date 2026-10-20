## Review import: Comparison Document_Organisational View.docx

Base model: `NRA_20250704-clean.qea`

| | count |
|---|---|
| elements/packages with changes | 21 |
| title changes | 3 |
| description changes | 20 |
| structure (manual) | 0 |
| conflicts | 0 |
| unmapped sections | 0 |
| comments | 2 |
| new elements | 1 |
| not applied (WIP / proposal / conflict) | 0 |
| warnings | 0 |

<details><summary><b> NAP Organisational View</b> – package description change</summary>


```diff
--- 
+++ 
@@ -1,4 +1,5 @@
-The Organizational View provides information about the actors, their roles and responsibilities, and relationships between roles in terms of lawful or contractual relationships. It also depicts desired business results and business processes for the ITS deployment which are related to the sub-set ITS architecture (owns, plans, maintains, deploys, implements, tender, …).
-The View consists of Actors performing one or more Roles, Agreements between the Roles, and relations to the Components and Modules.
-In the NAP Reference Architecture, the main Actors are the NAP Operator, the NAP Content Provider, the NAP Content Consumer, the National Body, the Member State, the European Commission, and the NAP Technical Operator. The Organizational View describes their responsibilities/obligations and identifies typical representatives of those roles. It also describes what lawful obligations these roles have (modelled as the relationship between the law-making roles and other roles) and what shall be the content of a contractual relationship between the roles.
-IMPORTANT: All lawful obligations come from the policy maker roles towards other roles, i.e., contracts between two non-policy-making roles do not contain what is already given, for the relationship of those roles, by the law.
+version: 2.0
+The Organisational View provides information about the Actors, their Roles and responsibilities, and relationships between roles in terms of lawful or contractual relationships. It also depicts the processes relevant to the ITS deployment (owns, plans, maintains, deploys, implements, tenders, …).
+The View consists of Actors assuming one or more Roles, the Agreements between the Roles, and their relations to the Components and Modules.
+In the NAP Reference Architecture, the main Actors are the European Commission, the Member State, the Competent Authority/National Body, the NAP Operator, the NAP IT Provider, the NAP Content Provider, and the NAP Content Consumer. The Organisational View describes the responsibilities, obligations and the typical representatives of each role. It also describes the lawful obligations of these roles, modelled as relationships between the law-making Roles (European Commission and Member State) and the other Roles. It further outlines the expected content of contractual relationships between the Roles.
+IMPORTANT: All lawful obligations come from the policy maker Roles (EC and MS) towards other Roles. Contracts between two non-policy-making roles do not repeat obligations already defined by law.
```
- 💬 Sara Linhas: CA/NB vs NB/CA ↳ Bures, Petr: yes we will change it in the picture to CA/NB. ↳ Bures, Petr: model...

</details>

<details><summary><b>Actor Content Consumer</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1,3 +1,3 @@
-Public and private organizations that are using static or dynamic traffic and travel information or any other relevant content, made accessible, under the Delegated Regulations obligations, via NAP, to create multimodal or traffic and travel or mobility information or were provided by the terms and conditions using the data for other related purposes. They are one or a group of actors who get added value by using data promoted by NAP.
-NOTE1: We do not create objects for each Content Consumer actor type.
-NOTE2: Content Consumer includes the Data User term as it is specified in MMTIS and RTTI regulations.
+Public or private entity that accesses, retrieves, or uses data or information made accessible through the National Access Point for the purpose of developing services, applications, or analyses.
+NOTE1:
+Content Consumer includes the terms Data User, Data Consumer and Data Recipient terms as specified in EU legal acts.
@@ -6,13 +6,13 @@
-road authorities
-public or private road operator/s
-traffic managers
-tolling operators
-service providers*
-broadcasters dedicated to traffic information
-transport authorities,
-transport operators,
-travel information service providers,
-digital map producers,
-transport on-demand service providers
-infrastructure managers
-data users, any public or private entity or any other entity using data listed in the Delegated Regulations
+Road authorities
+Public or private road operators
+Traffic managers
+Tolling operators
+Service providers
+Broadcasters dedicated to traffic information
+Transport authorities
+Transport operators
+Travel information service providers
+Digital map producers
+Transport on-demand service providers
+Infrastructure managers
+Data users, any public or private entity or any other entity using data accessible via NAP.
```

</details>

<details><summary><b>Actor Content Provider</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1,3 +1,3 @@
-Any legal person, data subject, or public or private entity/organization who has the right to grant access to or to share the data under its control. The subject in question shall hold the data that are required to be made accessible via NAP by or more of the Delegated Regulations.
-NOTE1: We do not create objects for each Content Provider actor type.
-NOTE2: Content Provider includes the Data Holder term as it is specified in MMTIS and RTTI regulations.
+Public or private entity that supplies content (e.g., data, metadata, documents) to the National Access Point, making it available for reuse in accordance with the requirements of the EU legal acts and National Laws.
+NOTE1:
+Content Provider includes the Data Holder, Data Provider, Service Provider terms as specified in EU legal acts.
@@ -5,0 +6,17 @@
+Automotive industries (when acting as service providers)
+Broadcasters dedicated to traffic information
+Holders of in vehicle generated data
+Infrastructure managers
+Operators of publicly accessible recharging points
+Operators of publicly accessible refuelling points
+Owners of recharging/refuelling infrastructure
+Public or private parking operators
+Public or private road operators
+Recharging and refuelling related stakeholders
+Road authorities
+Service providers*
+Tolling operators
+Transport authorities
+Transport operators
+Transport on demand service providers
+Travel information service providers
@@ -11 +28 @@
-* ‘service provider’ means any public or private provider of a real-time traffic information service, excluding a mere conveyer of data to data users;
+* ‘service provider’ means any public or private provider of a real-time traffic information service, excluding a mere conveyer of data-to-data users;
```

</details>

<details><summary><b>Actor European Commission</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1 +1 @@
-European Union responsible entity for the creation of the law and its publication.
+European Union’s main executive body, responsible for proposing legislation, its publication, upholding EU treaties and ensuring Member States apply EU law and policies.
```

</details>

<details><summary><b>Actor Member State</b> – editorial description change</summary>


```diff
--- 
+++ 
@@ -1 +1 @@
-European Union Member State is the responsible entity for the application and transposition of ITS-related EU laws and the creation of the national legal framework for the operation of the NAP and its surrounding entities.
+European Union country responsible for the application and transposition of ITS-related EU laws and the creation of the national legal framework for the operation of the NAP and its surrounding entities.
```

</details>

<details><summary><b>Actor NAP Operator</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1,2 +1,2 @@
-Any public or private organization responsible for collecting and publishing information about content generated by Content Providers (metadata) under the Delegated Regulations obligations, to any interested party (Content Consumers) without prejudice.
-The NAP (National Access Point) Actor represents and fulfils the interests of the NAP (National Access Point) Stakeholder.
+Public or private entity designated to manage, maintain and operate the National Access Point, ensuring the accessibility of data and that the NAP functions in line with the requirements of the applicable EU legal acts, further specified in national legislation or governance documents.
+The National Access Point (NAP) Actor represents and fulfils the interests of the National Access Point (NAP) Stakeholder.
@@ -4 +4 @@
-Usually, a department of the MS relevant Ministry (responsible for Transport matters), a state-owned organization, or a research organization. Usually, based on the explicit stating of the entity in the national law.
+Usually, a department of the Member State’s ministry responsible for transport, a stateowned organisation, or a research institution acts as NAP Operator. The organisation fulfilling this role is generally designated explicitly in national legislation or related governance documents.
```

</details>

<details><summary><b>Actor National Body / Competent Authority</b> – title change; substantive description change</summary>

- name → **Competent Authority / National Body**

```diff
--- 
+++ 
@@ -1,2 +1,2 @@
-Independent entity performing compliance assessment of the Content Providers, their specific content, the NAP operation, and reporting its findings to the MS.
-The NB/CA (National Body / Competent Authority) actor represents and fulfils the interests of the National Body / Competent Authority Stakeholder.
+A Competent Authority / National Body is an impartial and independent public or private entity designated by a Member State to monitor and report to the MS the operation of the National Access Point and to verify compliance of the Content Providers (CPs) with the requirements established by the ITS Directive and its Delegated Regulations, including the prescribed availability and accessibility, format, and quality requirements for data and services made accessible through the National Access Point.
+Note: The term National Body can be used interchangeably with Competent Authority, but it carries an additional requirement of impartiality and independence for the organisation towards Service Providers, public and private Road Operators, Parking Operators and Broadcasters. The term National Body remains valid in current legislation.
@@ -4 +4 @@
-Usually, a department of the MS Ministry of Transport and an independent body. Based on the explicit naming of the entity in the national law. The NB/CA shall be independent of CPs and NOs since it checks its compliance.
+Usually, a Member State department of the Ministry of Transport. The Competent Authority / National Body assignment shall be formalised through explicit designation in national law. Can also be represented by a private entity assigned by and cooperating with the government body
```

</details>

<details><summary><b>Role European Commission (EC)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -2 +2 @@
-Creation of the EU law that responds to the action plan and white/green books defining the advances in the health, safety, or environmental agendas.
+Creation of EU law that responds to the action plan and white/green books defining the advances in health, safety, or environmental agendas.
@@ -4 +4 @@
-Create a legal document (based on the Expert input and MS consultation) to be adopted by the defined approval procedure. To observe the adoption of those legal documents (assessing the obligations of MSs and reacting in case of non-adoption).
+Create legal documents (based on expert input and Member State consultation) to be adopted through the defined approval procedure. Observe the adoption and implementation of those legal documents, assessing Member State obligations and reacting in cases of non-adoption.
```

</details>

<details><summary><b>Role Member State (MS)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -2 +2 @@
-Transposition of the ITS Directive to the national law and setting up responsibilities for NAP and NB/CA operation.
+Transposition of the ITS Directive into national law and setting up responsibilities for the NAP and the CA/NB operation.
@@ -4 +4 @@
-Create a legal framework for the operation of the NAP and NB/CA, including clear definitions of their responsibilities, duties, and rights. Clear definition of obligations of Content Providers and selected Content Consumers.
+Create a legal framework for the operation of the NAP and CA/NB, including clear definitions of their responsibilities, duties, and rights. Constitute the obligations of Content Providers and selected Content Consumers as required by EU law and further specified in national legislation.
```

</details>

<details><summary><b>Role NAP Content Consumer (CC)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1 +1 @@
-IMPORTANT: Content Consumer includes the Data User term as it is specified in MMTIS and RTTI regulations
+IMPORTANT: Content Consumer includes the terms Data User, Data Consumer, Data Recipient as specified in EU legal acts.
@@ -5 +5 @@
-Provision of the service based on the consumed data, or any other task related to data processing and analysis. Sign a contract for content consumption with a content provider or with a proxy. Feedback to content providers. Timely and accurate integration of the subscribed content to their products and services.
+Access and use data in accordance with the defined legal, licensing or contractual conditions. Abide to the Terms and Conditions of the NAP, including e.g., registration requirements, attribution requirements or special license conditions. Provide feedback to Content Providers (e.g., on access, quality or integration of the data), or, where applicable to the NAP via feedback channels. Ensure the proper, timely and accurate integration of the subscribed content to their products and services.
```

</details>

<details><summary><b>Role NAP Content Provider (CP)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -1 +1 @@
-IMPORTANT: Content Provider includes the Data Holder term as it is specified in MMTIS and RTTI regulation.
+IMPORTANT: Content Provider includes the Data Holder, Data Provider, Service Provider terms as specified in EU legal acts.
@@ -3 +3 @@
-Publish metadata (and in certain cases data) at the NAP. Provide self-declaration and assistance in case of compliance assessment. Provide data in the prescribed format and with the desired level of quality.
+Publish content (e.g., data, metadata, documents) at the NAP. Provide the required self-declaration(s) and accompanying documents in accordance with the compliance assessment process. Provide data in the prescribed format and with the desired level of quality, as required by EU law and further specified in national legislation.
@@ -5 +5 @@
-Publish content they generate based on requirements from the Delegated Regulations under the FRAND conditions. In cases of safety-related traffic information publish content for free. Be of assistance to the NB/CA when performing a compliance assessment and correct any issues found promptly. Publish data with a desired level of quality in a timely fashion and in a prescribed format.
+Publish content they generate, hold, aggregate or curate and have the right to share based on requirements from the EU law and national law, under the FRAND conditions. Publish, free of charge, any content referent to categories that EU laws require free provision (e.g., safety-related traffic information). Collaborate with the CA/NB compliance assessment process and correct any issues found promptly. Publish content with the required level of quality, updated at an appropriate frequency, in a timely manner and up to date, using the prescribed format(s), as applicable.
```

</details>

<details><summary><b>Role NAP IT Provider (NIT)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -2 +2 @@
-Manage IT allowing NAP operation under the service level agreement.
+Manage the technical infrastructure enabling the operation of the NAP under the service level agreement.
@@ -4 +4 @@
-Set up the IT infrastructure. Scale the IT infrastructure according to the CPs, CCs, and NO demands. Operate, manage, and secure the infrastructure. Report to the NO and resolve promptly any technical issues. Provide technical user support.
+Set up the IT infrastructure. Scale the IT infrastructure according to usage patterns, feedback and requirements established by the NAP Operator (NO). Operate, monitor, manage, and secure the infrastructure. Report to the NO and promptly resolve any technical issues affecting the proper operation of the NAP. Provide technical user support (e.g., address access issues, API usage, platform errors).
```

</details>

<details><summary><b>Role NAP Operator (NO)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -2 +2 @@
-Publish information about Content Providers (CP) and their content in a transparent and timely manner. Provide free-to-all, barrier-free access to information collected by NO.
+Publish information about Content Providers (CPs) and their content in a transparent and timely manner. Provide free-to-all, barrier-free access to information available in the NAP.
@@ -4,3 +4,2 @@
-Publish information about the responsibilities of the Content Providers (CP), and the purpose of the NAP. Provide guidance and help to entities obliged to publish metadata to the NAP. Publish metadata about Content Providers and their content, free-to-all, barrier-free at the NAP. Enable CP to update/insert any information about their content or their organization. Publish metadata quality guidelines. Handle the exceptions about metadata/data not meeting threshold conditions for its publication (i.e., content is not in prescribed format). Promote the NAP and provide support for the Content Providers and Content Consumers. Monitor metadata quality and, potentially, data usage and provide this information either at NAP (if in the public interest) or to MS. Report to the MS about its operation. Keep the NAP-published metadata up to date. Provide a mechanism to collect feedback from the Content Consumers (CC) on the Content Providers' content.
-The tasks of the NAP Operator (or NAP) are NOT data processing, they publish Content Providers (meta)data in one place.
-NOTE: The organization performing the NAP Operator (NO) role can also perform other roles (i.e. Content Provider and Content Consumer) these roles do not intersect and shall be performed in such a way as to avoid conflict of interest.
+Ensure the accessibility of content through the NAP by providing the necessary means and conditions for Content Providers. Promote the NAP as a national source of ITS related information. Prepare, maintain and publish the Terms and Conditions of the NAP. Provide guidance and support to Content Providers and Content Consumers. Guarantee that metadata is accessible free-to-all and barrier-free at the NAP. Maintain and publish the Content Provider information in accordance with GDPR. Publish (meta)data quality guidelines. Establish mechanisms to facilitate the update, submission or publication of content at the NAP. Establish mechanism(s) to collect feedback from NAP Users. Set up quality measures, resolve reported issues, communicate with NAP Users when needed. Report NAP related statistics to the MS.
+NOTE: The organization performing the NAP Operator (NO) role may act also as Content Provider and/or Content Consumer. These roles shall be carried out in a way that avoids conflicts of interest.
```

</details>

<details><summary><b>Role National Body / Competent Authority (NB/CA)</b> – title change; substantive description change</summary>

- name → **Competent Authority/National Body (CA/NB)**

```diff
--- 
+++ 
@@ -2 +2 @@
-Provide a compliance assessment of the Content Providers (CP) and NAP operator (NO) with the Delegated Regulations and share these assessments with the CPs and NO. To operate objectively and independently from the NO and CPs.
+The CA/NB supports stakeholder in fulfilling the ITS directive and to handover accordingly self-declarations. Perform the compliance assessment of Content Providers (CP) in accordance with the Delegated Regulations and communicate the results with the CPs and NAP Operator (NO) and Member State (MS). Monitor the NAP operational performance and report to Member State (MS). Operate objectively and independently from the NO and CPs.
@@ -4 +4 @@
-Randomly and regularly check the compliance of CPs and the NO with the Delegated Regulations (data and metadata are compliant and processes of sharing the data and reporting are compliant with the rules set up by Delegated Regulations). Follow up on non-compliant results, and report results to the MS and NO. Collaborate with CP to reach a successful Compliance Assessment. Identify and contact entities obliged to publish (meta)data to the NAP.
+Identify and contact entities obliged to make their content accessible via the NAP, raising awareness of their obligations and facilitating onboarding. Randomly and regularly check the compliance of CPs with the EU law requirements (e.g., related to the content and processes of sharing data) and monitor and report operational performance of the NAP. Follow up on non-compliant results. Assist CPs to reach a successful Compliance Assessment result. Document the Compliance Assessment process, issue a report and share it with CPs, MS and NO.
```

</details>

<details><summary><b>Agreement Collaboration Agreement (NB/CA to NO)</b> – title change; editorial description change</summary>

- name → **Collaboration Agreement (CA/NB to NO)**

```diff
--- 
+++ 
@@ -1,2 +1,2 @@
-Parties: National Body / Competent Authority (NB/CA) and NAP Operator (NO).
-Objective: To address all possible issues NB/CA might have towards the NO, that are not dealt with by the law.
+Parties: National Body / Competent Authority (CA/NB) and NAP Operator (NO).
+Objective: To address all possible issues CA/NB might have towards the NO, that are not dealt with by the law.
@@ -5 +5 @@
-> NB/CA to NO:
+> CA/NB to NO:
@@ -8,2 +8,2 @@
-> NO to NB/CA:
-To fully disclose all received information/evidence to the NB/CA assisting in the assessment process.
+> NO to CA/NB:
+To fully disclose all received information/evidence to the CA/NB assisting in the assessment process.
```

</details>

<details><summary><b>Agreement EU Legal Framework (EC to MS)</b> – editorial description change</summary>


```diff
--- 
+++ 
@@ -3,2 +3 @@
-Form: the ITS Directive and Delegated Regulations
-Obligations:
+Form: the ITS Directive and Delegated Regulations Obligations:
@@ -10 +9 @@
-To establish the National Body / Competent Authority (NB/CA) in the national law; either delegate its establishment to a responsible ministry or directly state the party responsible for NB/CA operation; create a legal framework for its operation.
+To establish the National Body / Competent Authority (CA/NB) in the national law; either delegate its establishment to a responsible ministry or directly state the party responsible for CA/NB operation; create a legal framework for its operation.
```

</details>

<details><summary><b>Agreement European or national law (MS to CP)</b> – substantive description change</summary>


```diff
--- 
+++ 
@@ -2,2 +2,2 @@
-Objective: To identify CPs and set up obligations of the CPs.
-Form: National law implementing the ITS Directive and direct execution of EU Regulations and Delegated Acts.
+Objective: To identify Content Providers (CPs) and establish their legal obligations.
+Form: National Law transposing the ITS Directive and direct execution of EU Regulations including Regulations, Delegated Regulations and Implementing Regulations.
@@ -5 +5 @@
-> MS to CP: ---
+> MS to CP: None
@@ -7,5 +7,6 @@
-To ensure that data is provided in a correct format to the content consumers (CC) under fair, reasonable, and non-discriminatory (FRAND) conditions.
-To publish relevant information about data/services (e.g., Metadata) and information on the data quality at the NAP.
-To provide data compliant with the EU requirements (Provide self-declaration towards the NAP and NB/CA and assistance in case further proof of compliance is required).
-To ensure that required data is updated at the appropriate and recommended time intervals.
-To provide a description of the data, digital map, or real-time traffic information services they provide as well as the information on the quality thereof and the conditions of re-use of these data and an evidence-based declaration of compliance to the NB/CA. And to cooperate in the compliance assessment process.
+Ensure that data is available in the correct format and under fair, reasonable, and non-discriminatory (FRAND) conditions via the NAP.
+Provide the required information about data/services, including access, reuse conditions and quality related information to the NAP.
+Provide data
+/services compliant with the EU requirements and be available for the compliance assessment upon request and provide additional documentation if required.
+Provide self-declaration(s) to the NAP and/or CA/NB.
+Ensure that required data is updated at the appropriate and recommended time intervals.
@@ -13 +14 @@
-The obligations of the CP are related to the following laws:
+The obligations of the Content Provider (CP) are related to the following EU legal acts and national laws:
@@ -15,5 +15,0 @@
-886/2013 (SRTI)
-885/2013 (SSTP)
-2017/1926 (MMTIS)
-2022/670 (RTTI in force from 1. January 2025)
-2023/1804 (AFIR)
@@ -21 +17,7 @@
-2024/490 (MMTIS amendment)
+Delegated Regulation 886/2013 (SRTI)
+Delegated Regulation 885/2013 (SSTP)
+Delegated Regulation 2017/1926 (MMTIS)
+Delegated Regulation 2022/670 (RTTI in force from 1. January 2025)
+Regulation 2023/1804 (AFIR)
+Implementing Regulation 2026/253 (TEL-TSI)
+Delegated Regulation 2024/490 (MMTIS amendment)
@@ -23 +25 @@
-For the sole purposes of providing the information service, public and private road operators and/or service providers shall set up or use the means to detect events or identify conditions, and shall collect the relevant road safety-related traffic data. The deployment of these means shall comply with the conditions and requirements set out in national law. [886/2013, art. 6].
+For the sole purposes of providing the information service, public and private road operators and/or service providers shall set up or use the means to detect events or identify conditions and shall collect the relevant road safety-related traffic data. The deployment of these means shall comply with the conditions and requirements set out in national law. [886/2013, art. 6].
@@ -25 +27 @@
-Public or private parking operators and service providers shall share and exchange data referred to in paragraph 1 of art. 4 of DR 885/2013. For these purposes, they shall use DATEX II (CEN/TS 16157) format or any DATEX II compatible international machine-readable format. Data shall be accessible for exchange and reuse by any public or private information service provider and/or parking operator on a non-discriminatory basis and in accordance with access rights and procedures defined in Directive 2003/98/EC [885/2013 art. 5].
+Public or private parking operators and service providers shall share, and exchange data referred to in paragraph 1 of art. 4 of DR 885/2013. For these purposes, they shall use DATEX II (CEN/TS 16157) format or any DATEX II compatible international machine-readable format. Data shall be accessible for exchange and reuse by any public or private information service provider and/or parking operator on a non-discriminatory basis and in accordance with access rights and procedures defined in Directive 2003/98/EC [885/2013 art. 5].
@@ -30,3 +32,3 @@
-(a) on a non-discriminatory basis when provided by road authorities and road operators; [2022/670, art. 6 par 2, art. 7, par 2]
-(b) following minimum quality requirements that Member States shall agree upon in cooperation with relevant stakeholders;
-(c) within a time-frame fitting to the reliable and effective use of the data to create real-time traffic information;
+(b) on a non-discriminatory basis when provided by road authorities and road operators; [2022/670, art. 6 par 2, art. 7, par 2]
+(c) following minimum quality requirements that Member States shall agree upon in cooperation with relevant stakeholders;
+(d) within a timeframe fitting to the reliable and effective use of the data to create real-time traffic information;
@@ -34 +36 @@
-NB/CA (competent authorities of the Member States) may request from the data holders and travel information service providers the following documents: [2024/490 art. 9]
+Competent Authority / National Body (CA/NB) may request from the data holders and travel information service providers the following documents: [2024/490 art. 9]
@@ -38 +40 @@
-4 the licence or contractual agreements with travel information service providers.
+4 the license or contractual agreements with travel information service providers.
```

</details>

<details><summary><b>Agreement Metadata provision contract (NO to CP)</b> – editorial description change</summary>


```diff

```

</details>

<details><summary><b> Content provision contract/agreement (NO to CP)</b> – new object</summary>

- new **Agreement** after *Metadata provision contract (NO to CP)*
- [ ] «adheres to» links to both parties (Roles)
- candidate links: Agreement: European or national law (MS to CP); Role: NAP Content Provider (CP); Role: NAP Operator (NO); Stakeholder: Content Consumer; Stakeholder: Content Provider

```
NEW AGREEMENT
Parties: NAP operator (NO) and Content Provider (CP).
Objective: Set up operational and/or contractual obligations under which the content could be stored or proxied at/by the NAP. Set up obligations and responsibilities of the NO towards the CP, that are not regulated by law.
Form: Contract, terms and conditions.
Obligations:
> CP to NO
Provide the content to be made available through the NAP, supplying it in accordance with the agreed operational procedures or contractual obligations.
Provide, where applicable, the necessary authorization for the NAP operator to publish personal data on the NAP, limited to the scope explicitly agreed between the parties.
> NO to CP
Make the content accessible to Content Consumers (CCs) immediately after it has been provided by the CP.
Provide the necessary support and guidance for the content submission and publication on the NAP.
Respect the CP authorization to publish personal data on the NAP and ensure that the applicable data protection legislation is upheld.
Communicate clearly and in a timely manner, any detected technical issues with the provision of the data to CCs.
Provide the relevant statistics of data access on the NAP to the CP.
Ensure that the provided content is not tampered with nor altered in any way, allowing only the technical processing necessary for its publication on the NAP.
NOTE: The mandatory obligations of the CP, established by European or National Law (connected to e.g., data provision, information, quality, compliance assessment), are defined in the European or national law (MS to CP) Agreement between MS and CP.
Reference to the EU law:
NONE
```

</details>

<details><summary><b>Agreement National Law or Contract (MS to NO)</b> – editorial description change</summary>


```diff
--- 
+++ 
@@ -8 +8 @@
-To provide appropriate discovery services to NAP users / Content Consumers (CP).
+To provide appropriate discovery services to NAP users (i.e. Content Consumers (CC)).
```
- 💬 Sara Linhas: I believe this was a typo ↳ Bures, Petr: no it is not. Checked

</details>

<details><summary><b>Agreement Privacy agreement (CC to NO) and general terms and conditions</b> – editorial description change</summary>


```diff

```

</details>

