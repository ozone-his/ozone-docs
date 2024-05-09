!!! info ""

    This section of the Ozone Docs is tailored for **digital health decision-makers and business analysts**, detailing Ozone's functionalities and highlighting its benefits for end users of health information systems and integrated digital health software.

# Overview

Ozone is an easy-to-install {==growing suite of digital health software==},
<br/>integrated by a {==scalable interoperability framework==}
<br/>delivering a complete health information system experience.

``` mermaid
stateDiagram-v2
    state "Ozone HIS" as ozone
    state "digital health software" as state1
    state "interoperability framework" as state2

    state1 --> ozone
    state2 --> ozone
```

## **1** &nbsp; A suite of opt in/out digital health software

Ozone is a ready-to-use solution, providing a pre-selected array of FOSS[^foss] components that function seamlessly together.

[^foss]:  Free and open-source software

It is a complete health information system allowing users to customize it by choosing which supported digital health software to include or exclude.

### Criteria to enter Ozone HIS' suite

As Ozone continues to expand its suite of software components, several criteria must be met for a software component to be included in the Ozone HIS ecosystem. Below, we outline these requirements:

|Criterion|Requirement| |
|:---:|:---:|:---:|
|:fontawesome-brands-osi: Open-source|{==**Must**==}|Ozone is FOSS under MPL 2.0. Closed-source software is accommodated within the Pro edition of Ozone or through custom developments.|
|:fontawesome-solid-tag: Released version|{==**Must**==}|Ozone supports HIS flows between versioned components with stable and, ideally, well-documented APIs.|
|:fontawesome-solid-shield-halved: OAuth 2|{==**Must**==}|OAuth2 is required for enhanced security and to implement SSO within the Ozone HIS.|
|:fontawesome-brands-docker: Docker image|{==**Must**==}|Docker, while not the sole deployment mechanism supported, is currently the default one in Ozone HIS.|
|:fontawesome-solid-heart-pulse: Health check|**Should**|It is crucial that each component includes a web endpoint to let Ozone verify it is operational within the HIS.|
|:simple-prometheus: Prometheus metrics|**Should**|Providing Prometheus metrics is recommended to enhance monitoring and ensure effective system performance management.|
|:fontawesome-solid-timeline: Backup & restore|**Should**|Each component should include automated backup and restore capabilities to ensure data integrity and system resilience.|
|:fhir: HL7 FHIR API|**Should**|Providing HL7 FHIR API reduces development overhead for peer-to-peer HIS components routes within Ozone.|
|:fontawesome-solid-sitemap: Event bus|Could|Providing an event bus could offer a more efficient method of dispatching information as it becomes available, eliminating the need for polling.|

### Suite as of Ozone HIS `1.0.0-alpha.9`

|HIS type|Component|Version in Ozone HIS|
|:---:|:---:|:---:|
|EMR|:openmrs: OpenMRS|`3.0.0-beta.16`|
|LIMS|SENAITE|`2.1.0`|
|ERP|Odoo|`14`|
|ERP|:erpnext: ERPNext|`15.12.2`|
|BI|:superset: Apache Superset|`1.5.1`|
|IdP|:keycloak: JBoss Keycloak|`22.0.0`|

!!! tip "Ozone Pro markers"

    Features and sections exclusive to Ozone Pro are marked with &nbsp;&nbsp;{==:oz: Pro==}.

## **2** &nbsp; An interoperability framework

Ozone is powered by an interoperability EIP[^eip] framework that orchestrates seamless data flows between health information system components — EMR, LIMS, pharmacy, accounting, BI, and more.

[^eip]: Entreprise integration patterns

!!! example "Sample data flows"

    _Clinicians' drug orders in the EMR system automatically generate items on the patient bill._

    _Lab results entered into the LIMS by lab staff are immediately visible to clinicians in the EMR system._

    _Data analysts can perform real-time cross-analysis of clinical and billing data on the BI platform._

## What Ozone is not

{==Ozone is not a fork==} of other open-source projects; it utilizes standard and officially released software components from various open-source communities.

[^lts]: Long-term support

Ozone packages the latest LTS[^lts] versions of its components 'as-is'. Therefore it is not liable for any bugs, deficiencies, or performance issues in the bundled LTS versions of its components; these fall outside the purview of Ozone itself.

!!! tip

    We generally do not document Ozone’s components. Instead we refer to their own official documentation as much as possible.