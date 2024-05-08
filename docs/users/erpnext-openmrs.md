# ERPNext-OpenMRS Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant ERPNext
        OpenMRS->>Ozone: Patients
        Ozone->>ERPNext: Customers
        OpenMRS->>Ozone: Visits
        OpenMRS->>Ozone: Drug orders
        OpenMRS->>Ozone: Lab test orders
        Ozone->>ERPNext: Quotations
        Ozone->>ERPNext: Quotation items
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|OpenMRS|Patient|→|ERPNext|Customer|
|OpenMRS|Visit|→|ERPNext|Quotation|
|OpenMRS|Billable item|⭆|ERPNext|Quotation|
|OpenMRS|Billable item|→|ERPNext|Quotation item|


!!! question "What are the OpenMRS billable items?"

    The supported billable items are:

    - OpenMRS drug orders
    - OpenMRS lab test orders

## Flows Details

### **1** &nbsp; OpenMRS Patient → ERPNext Customer

A patient in OpenMRS is synchronized as a corresponding customer in ERPNext.

``` mermaid
flowchart LR
    a["OpenMRS patient"]-- 1-to-1 -->b["ERPNext customer"]
```

!!! abstract "Options"

    <small>**_default option_**</small> &nbsp; An OpenMRS patient is synchronised as an ERPNext customer when the first billable item is ordered from OpenMRS.

    <small>_option 1_</small> &nbsp; An OpenMRS patient is always synchronised as an ERPNext customer.

### **2** &nbsp; OpenMRS Visit → ERPNext Quotation

A new draft ERPNext quotation is linked with an OpenMRS patient's visit as soon as the first billable item is ordered during that visit.

Eventually, ending a patient's visit in OpenMRS submits the draft ERPNext quotation linked with this visit.

``` mermaid
flowchart LR
    a["OpenMRS visit"]-- 1-to-1 -->b["ERPNext quotation"]
```

### **3** &nbsp; OpenMRS Billable Items ⭆ ERPNext Quotation

As soon as the first billable item is ordered for a patient in OpenMRS a draft quotation is created in ERPNext for the ERPNext customer corresponding to that patient, furthermore the quotation is linked with the OpenMRS patient's visit.

All billable items ordered for a patient within the same OpenMRS visit are added to the draft ERPNext quotation
linked with this OpenMRS visit.

``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["ERPNext quotation"]
```

### **4** &nbsp; OpenMRS Billable Item → ERPNext Quotation Item

Each billable item ordered in OpenMRS during a patient's visit is synchronized in ERPNext as a quotation item in the corresponding customer's draft quotation that is linked with the OpenMRS patient's visit.

``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["ERPNext quotation item"]
```