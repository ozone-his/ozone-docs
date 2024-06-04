# Odoo-OpenMRS Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Odoo
        OpenMRS->>Ozone: Patients
        Ozone->>Odoo: Customers
        OpenMRS->>Ozone: Visits
        OpenMRS->>Ozone: Drug orders
        OpenMRS->>Ozone: Lab test orders
        Ozone->>Odoo: Quotations
        Ozone->>Odoo: Quotation items
```

## Flows List

|Source|    Element    | |Target|     Element     |
|:---:|:-------------:|:---:|:---:|:---------------:|
|OpenMRS|    Patient    |→|Odoo|    Customer     |
|OpenMRS|     Visit     |→|Odoo|    Quotation    |
|OpenMRS| Billable item |⭆|Odoo|    Quotation    |
|OpenMRS| Billable item |→|Odoo| Quotation item |


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

### **2** &nbsp; OpenMRS Visit → Odoo Quotation

A new Odoo quotation is linked with an OpenMRS patient's visit as soon as the first billable item is ordered during that visit.

``` mermaid
flowchart LR
    a["OpenMRS visit"]-- 1-to-1 -->b["Odoo quotation"]
```

### **3** &nbsp; OpenMRS Billable Items ⭆ Odoo Quotation

As soon as the first billable item is ordered for a patient in OpenMRS, a quotation is created in Odoo for the Odoo customer corresponding to that patient. Furthermore the quotation is linked with the OpenMRS patient's visit.

All billable items ordered for a patient within the same OpenMRS visit are added to the Odoo quotation linked with this OpenMRS visit.

``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["Odoo quotation"]
```

### **4** &nbsp; OpenMRS Billable Item → Odoo Quotation Item

Each billable item ordered in OpenMRS during a patient's visit is synchronized in Odoo as a quotation item in the corresponding customer's quotation that is linked with the OpenMRS patient's visit.

When a drug / lab order is discontinued for a patient in OpenMRS, the corresponding quotation item is removed from the corresponding Odoo quotation.

If all quotation items are removed from a quotation, the quotation is then marked as cancelled.

``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["Odoo order line"]
```
