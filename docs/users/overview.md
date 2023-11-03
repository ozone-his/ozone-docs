# Overview

Ozone is an {==expanding suite of health information systems==},
<br/>seamlessly integrated through a {==scalable interoperability framework==}.

``` mermaid
stateDiagram-v2
    state "Ozone HIS" as ozone
    state "interoperability framework" as state2
    state "health information systems" as state1

    ozone --> state1: suite of
    ozone --> state2: run by
```

## A suite of opt in/out interoperable systems

Ozone is a ready-to-use solution, providing a pre-selected array of FOSS[^1] components that function seamlessly together.

It is a complete health information system distribution, allowing users to customize by choosing which supported components to include or exclude.

[^1]:  Free and open-source software

### Current Ozone HIS suite

| **HIS type** | **Component**            | **Version**       |
|----------|-----------------|---------------|
| EMR      | OpenMRS         | `3.0.0-beta.13` |
| LIMS     | SENAITE         | `2.1.0`             |
| ERP      | Odoo            | `14`            |
| BI       | Apache Superset | `1.5.1`         |

## An interoperability framework

Ozone brings an interoperability EIP[^eip] framework, _Ozone Platform_, that orchestrates seamless data flows between health information system components — EMR, LIMS, pharmacy, accounting, BI, and more.

[^eip]: Entreprise integration patterns

!!! example

    Clinicians' drug orders in the EMR system automatically generate items on the patient bill.

!!! example
    
    Lab results entered into the LIMS by lab staff are immediately visible to clinicians in the EMR system.

!!! example

    Data analysts can perform real-time cross-analysis of clinical and billing data on the BI platform.

## What Ozone is not

Ozone is <u>not a fork</u> of other open-source projects; it utilizes standard, untouched components.

[^lts]: Long-term support

Ozone packages the latest LTS[^lts] versions of its components 'as-is'. Therefore it is not liable for any bugs, deficiencies, or performance issues in the bundled LTS versions of its components; these fall outside the purview of Ozone.

!!! tip

    We generally do not document Ozone’s components. Instead we refer to their own official documentation as much as possible.