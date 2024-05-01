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

## 1) A suite of opt in/out digital health software

Ozone is a ready-to-use solution, providing a pre-selected array of FOSS[^foss] components that function seamlessly together.

It is a complete health information system allowing users to customize it by choosing which supported digital health software to include or exclude.

[^foss]:  Free and open-source software

### Current Ozone HIS suite

| **HIS type** | **Component**   | **Version**     |                |
|--------------|-----------------|-----------------|----------------|
| EMR          | OpenMRS         | `3.0.0-beta.16` |                |
| LIMS         | SENAITE         | `2.1.0`         |                |
| ERP          | Odoo            | `14`            |                |
| ERP          | ERPNext         | `15.12.2`       |                |
| BI           | Apache Superset | `1.5.1`         |                |
| IdP          | JBoss Keycloak  | `22.0.0`        | {==:oz: Pro==} |

!!! tip "Ozone Pro markers"

    Features and sections exclusive to Ozone Pro are marked with &nbsp;&nbsp;{==:oz: Pro==}.

## 2) An interoperability framework

Ozone is powered by an interoperability EIP[^eip] framework that orchestrates seamless data flows between health information system components — EMR, LIMS, pharmacy, accounting, BI, and more.

[^eip]: Entreprise integration patterns

!!! example

    Clinicians' drug orders in the EMR system automatically generate items on the patient bill.

!!! example
    
    Lab results entered into the LIMS by lab staff are immediately visible to clinicians in the EMR system.

!!! example "Example &nbsp;&nbsp; {==:oz: Pro==}"

    Data analysts can perform real-time cross-analysis of clinical and billing data on the BI platform.

## What Ozone is not

Ozone is <u>not a fork</u> of other open-source projects; it utilizes standard, officially released and untouched software components.

[^lts]: Long-term support

Ozone packages the latest LTS[^lts] versions of its components 'as-is'. Therefore it is not liable for any bugs, deficiencies, or performance issues in the bundled LTS versions of its components; these fall outside the purview of Ozone.

!!! tip

    We generally do not document Ozone’s components. Instead we refer to their own official documentation as much as possible.
