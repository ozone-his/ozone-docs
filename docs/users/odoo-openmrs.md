# Odoo-OpenMRS Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Odoo
        OpenMRS->>Ozone: Patients
        Ozone->>Odoo: Customers
        OpenMRS->>Ozone: Drug orders
        OpenMRS->>Ozone: Lab test orders
        Ozone->>Odoo: Quotations
        Ozone->>Odoo: Order lines
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|OpenMRS|Patient|→|Odoo|Customer|
|OpenMRS|Billable item|⭆|Odoo|Quotation|
|OpenMRS|Billable item|→|Odoo|Order line|


!!! question "What are the OpenMRS billable items?"

    The supported billable items are:

    - OpenMRS drug orders
    - OpenMRS lab test orders

## Flows Details

### **1** &nbsp; OpenMRS Patient → Odoo Customer

A patient in OpenMRS is synchronized as a corresponding customer in Odoo.

``` mermaid
flowchart LR
    a["OpenMRS patient"]-- 1-to-1 -->b["Odoo customer"]
```

!!! abstract "Options"

    <small>**_default option_**</small> &nbsp; An OpenMRS patient is synchronised as an Odoo customer when the first billable item is ordered from OpenMRS.

    <small>_option 1_</small> &nbsp; An OpenMRS patient is always synchronised as an Odoo customer.

### **2** &nbsp; OpenMRS Billable Items ⭆ Odoo Quotation

As soon as the first billable item is ordered for a patient in OpenMRS a draft quotation is created in Odoo for the Odoo customer corresponding to that patient.

``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["Odoo quotation"]
```

### **3** &nbsp; OpenMRS Billable Item → Odoo Quotation Item

Each billable item ordered for an OpenMRS patient is synchronized in Odoo as an order line in the corresponding customer's quotation.

``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["Odoo order line"]
```