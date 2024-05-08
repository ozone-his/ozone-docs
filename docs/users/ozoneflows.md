# Ozone Flows Guide

The following pages describe the data flows orchestrated by Ozone HIS among its supported components. These flows are fundamental to Ozone's functionality, as they leverage and integrate existing software components to provide enhanced features that are not available when these components are used independently.

Flows are documented by {==pairs of components==}, such as:

- Flows between ERPNext and OpenMRS.
- Flows between OpenMRS and SENAITE.
- Etc.

## Flows Documentation Structure

The structure of each flows documentation page is typically organized as follows (unless unnecessary or impractical), for each pair of components: flows overview, flows list and flows details.

### **1** &nbsp; Flows Overview

This section includes a sequence diagram that illustrates the high-level exchanges between two components that are facilitated through Ozone. Eg.:

``` mermaid
    sequenceDiagram
        participant Odoo
        participant Ozone
        participant openIMIS
        Odoo->>Ozone: Invoices lines
        Ozone->>openIMIS: Claim Items
        openIMIS->>Ozone: Payments
        Ozone->>Odoo: Payments
```

### **2** &nbsp; Flows List

A table that presents an inventory of all the flows between source data elements and target data elements, including the type of relatonship between the source data element and the target data element for each flow. Eg.:

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|Odoo|Customers|⭆|openIMIS|Household|
|Odoo|Invoice line|→|openIMIS|Claim item|
|openIMIS|Payment|→|Odoo|Payment|

!!! tip "Types of flows"

    * one-to-one &nbsp; **→**
    * many-to-one &nbsp; **⭆**
    * deletion  &nbsp; **⊝**

### **3** &nbsp; Flows Details

In this section, each flow is described in detail, providing plain English explanations of the functional intent and outlining the various options available for each flow, where applicable.