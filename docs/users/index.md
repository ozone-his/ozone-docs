!!! info ""

    This section of the Ozone Docs is tailored for **digital health decision-makers and business analysts**, detailing Ozone's functionalities and highlighting its benefits for end users of health information systems and integrated digital health software.

# Overview

Ozone is an easy-to-install {==growing suite of digital health apps==},
<br/>integrated by a {==scalable interoperability framework==}
<br/>delivering a complete health information system experience.

``` mermaid
stateDiagram-v2
    state "Ozone HIS" as ozone
    state "digital health apps" as state1
    state "interoperability framework" as state2

    state1 --> ozone
    state2 --> ozone
```

## **1** &nbsp; A suite of opt in/out digital health apps

Ozone is a ready-to-use solution, providing a pre-selected array of FOSS[^foss] apps that function seamlessly together.

[^foss]:  Free and open-source software

It is a complete health information system allowing users to customize it by choosing which supported digital health software to include or exclude:

### Ozone HIS apps

**<small>:fontawesome-solid-tag:</small> `1.0.0-alpha.13`**

|Area|App|Version in Ozone|Maturity in Ozone|
|:---:|:---:|:---:|:---:|
|EMR|:openmrs: OpenMRS|`3.2.1`|:material-diamond-stone: Core|
|LIMS|SENAITE|`2.5.0`|:material-diamond-stone: Core|
|ERP|Odoo|`14`|:material-diamond-stone: Core|
|ERP|:erpnext: ERPNext|`15.12.2`|:material-timer-pause-outline: Legacy|
|BI|:superset: Apache Superset|`3.1.0`|:material-diamond-stone: Core|
|IdP|:keycloak: JBos Keycloak|`22.0.5`|:material-diamond-stone: Core|
|PACS|Orthanc|`1.0.0`|:material-diamond-stone: Core|

### Maturity levels in Ozone

- **:material-diamond-stone: Core** – Core apps are fully supported in Ozone. They are regularly upgraded with new Ozone versions, with their data flows within the HIS maintained to ensure seamless upgrades and backward compatibility.
- **:material-timer-pause-outline: Legacy** – Legacy apps and their data flows were introduced in a specific version of Ozone but are no longer actively maintained beyond that version. They remain available "as is" for continued use without further updates.

!!! tip "Ozone Pro markers"

    Features and sections exclusive to Ozone Pro are marked with &nbsp;&nbsp;{==:oz: Pro==}.

### Criteria for inclusion

As Ozone continues to expand its suite of software apps, several criteria must be met for an app to be included in the Ozone ecosystem. Below, we outline these requirements by order of importance:

|Criterion|Requirement| |
|:---:|:---:|:---:|
|:fontawesome-brands-osi: Open-source|{==**Must**==}|Ozone is FOSS under MPL 2.0. Closed-source software is accommodated within the Pro edition of Ozone or through custom developments.|
|:fontawesome-solid-tag: Released version|{==**Must**==}|Ozone supports HIS flows between versioned software apps with stable and, ideally, well-documented APIs.|
|:fontawesome-solid-shield-halved: OAuth 2|{==**Must**==}|OAuth2 is required for enhanced security and to implement SSO within the Ozone HIS.|
|:fontawesome-solid-lock: Security updates|{==**Must**==}|Must undergo regular security audits (e.g. pen tests) and have a clear process for broadcasting the availability of security updates.|
|:fontawesome-brands-docker: Docker image|**Should**|Docker, while not the sole deployment mechanism supported, is currently the default one in Ozone HIS.|
|:material-cog: Automated configurability|**Should**|Apps should be configurable through deployment processes, allowing for automated setup and initialization (specifically of master data) by placing configuration files in the appropriate locations.|
|:fontawesome-solid-heart-pulse: Health check|**Should**|It is crucial that each app includes a web endpoint to let Ozone verify it is operational within the HIS.|
|:fontawesome-solid-scale-balanced: Privacy & Legal Compliance|**Should**|Should comply with relevant privacy, domestic, and applicable international laws. This may include data protection regulations.|
|:simple-prometheus: Prometheus metrics|**Should**|Providing Prometheus metrics is recommended to enhance monitoring and ensure effective system performance management.|
|:fontawesome-solid-timeline: Backup & restore|**Should**|Automated backup and restore capabilities ensure data integrity and system resilience in production use.|
|:fontawesome-solid-globe: Internationalization|**Should**|Internationalization should be a first class citizen for any software. It ensures that it can be easily adapted to various languages and regions, making it accessible and usable by a global audience.|
|:material-puzzle: Modularity|**Should**|Modularitiy enables potential enhancements or modifications to be made via modules, plugins, or addons without affecting the core software of the app.|
|:fhir: HL7 FHIR API|**Should**|Providing HL7 FHIR API reduces development overhead for point-to-point apps routes within the Ozone HIS.|
|:fontawesome-solid-sitemap: Event bus|Could|An event bus offers a more efficient method of dispatching information as it becomes available, eliminating the need for polling.|

## **2** &nbsp; An interoperability framework

Ozone is powered by an interoperability EIP[^eip] framework that orchestrates seamless data flows between health information system apps — EMR, LIMS, pharmacy, accounting, BI, and more.

[^eip]: Entreprise integration patterns

!!! example "Sample data flows"

    _Clinicians' drug orders in the EMR system automatically generate items on the patient bill._

    _Lab results entered into the LIMS by lab staff are immediately visible to clinicians in the EMR system._

    _Data analysts can perform real-time cross-analysis of clinical and billing data on the BI platform._

## What Ozone is not

{==Ozone is not a fork==} of other open-source projects; it utilizes standard and officially released software apps from various open-source communities.

[^lts]: Long-term support

Ozone packages the latest LTS[^lts] versions of its apps 'as-is'. Therefore it is not liable for any bugs, deficiencies, or performance issues in the bundled LTS versions of its apps; these fall outside the purview of Ozone itself.

!!! tip

    We generally do not document Ozone’s apps. Instead we refer to their own official documentation as much as possible.
