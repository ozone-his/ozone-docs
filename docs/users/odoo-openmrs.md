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
        Ozone->>Odoo: Sale Order lines
```

## Flows List

|Source|    Element    | |Target|     Element     |
|:---:|:-------------:|:---:|:---:|:---------------:|
|OpenMRS|    Patient    |→|Odoo|    Customer     |
|OpenMRS|     Visit     |→|Odoo|    Quotation    |
|OpenMRS| Billable item |⭆|Odoo|    Quotation    |
|OpenMRS| Billable item |→|Odoo| Sale Order line |


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

Eventually, ending a patient's visit in OpenMRS submits the Odoo quotation linked with this visit.

``` mermaid
flowchart LR
    a["OpenMRS visit"]-- 1-to-1 -->b["Odoo quotation"]
```


### **3** &nbsp; OpenMRS Billable Items ⭆ Odoo Quotation

As soon as the first billable item is ordered for a patient in OpenMRS a quotation is created in Odoo for the Odoo customer corresponding to that patient, furthermore the quotation is linked with the OpenMRS patient's visit.

All billable items ordered for a patient within the same OpenMRS visit are added to the Odoo quotation linked with this OpenMRS visit.

``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["Odoo quotation"]
```

### **4** &nbsp; OpenMRS Billable Item → Odoo Quotation Item

Each billable item ordered in OpenMRS during a patient's visit is synchronized in Odoo as a sale order line in the corresponding customer's quotation that is linked with the OpenMRS patient's visit.

``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["Odoo order line"]
```

### **5** &nbsp; OpenMRS Discontinue Medication → Cancel Odoo Sale Order Line / Quotation

When an active medication is discontinued for a patient in OpenMRS corresponding quotation's sale order line is removed, if all sale order lines are removed from a quotation then the quotation is marked as cancelled.

``` mermaid
flowchart LR
    a["OpenMRS active medication"]-- 1-to-many -->b["Odoo quotation"]
```
