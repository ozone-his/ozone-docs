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
        OpenMRS->>Ozone: Radiology ServiceRequest
        Ozone->>Odoo: Quotations
        Ozone->>Odoo: Order Lines
        Odoo->>Ozone: Products
        Ozone->>OpenMRS: Drugs
        Ozone->>OpenMRS: Create/update FHIR Task
```

## Flows List

|Source|    Element    | |Target|     Element     |
|:---:|:-------------:|:---:|:---:|:---------------:|
|OpenMRS|    Patient    |→|Odoo|    Customer     |
|OpenMRS|     Visit     |→|Odoo|    Quotation    |
|OpenMRS| Billable item |⭆|Odoo|    Quotation    |
|OpenMRS| Billable item |→|Odoo| Order line |
|Odoo| Products |→|OpenMRS| Drugs |
|Odoo| Payment status |→|OpenMRS| FHIR 'Task' status |

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

### **4** &nbsp; OpenMRS Billable Item → Odoo Order Line

Each billable item ordered in OpenMRS during a patient's visit is synchronized in Odoo as an order line in the corresponding customer's quotation that is linked with the OpenMRS patient's visit.

When a drug or lab test order is discontinued for a patient in OpenMRS, the corresponding order line is removed from the related Odoo quotation.

If all order lines are removed from a quotation, the quotation is marked as cancelled.

``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["Odoo order line"]
```

### **5** &nbsp; Odoo Product → OpenMRS Drug

Products in Odoo that belong to the drugs category and have an associated concept dictionary mapping are automatically synchronized into OpenMRS as drug entries.

``` mermaid
flowchart LR
    a["Odoo product (in drug category)"]-- 1-to-1 -->b["OpenMRS Drugs"]
```

### **6** &nbsp; Odoo Payment Status → OpenMRS 'Task' FHIR status

The Odoo payment orders and the payment states are queried and associated to one 'status' value in OpenMRS 'Task' FHIR resource. 

``` mermaid
flowchart LR
    a["Odoo<br/>Sale Order + Invoice"]-- 2-to-1 -->b["OpenMRS<br/>FHIR Task"]
```
!!! question "What is exactly the processing logic?"

The processing logic is the following: 

    Every polling cycle the processor fetches 'ServiceRequest' resources (that regroups a time window of 7days) from OpenMRS (this is required as the payment confirmation happens in Odoo and never touches the ServiceRequest's own '_LastUpdated'). It then filters it client-side for 'status==ACTIVE' and the radiology concept code. 

    Whether the Task already existed is checked by comparing the Tesk's 'basedOn' reference. 
    The Odoo sale line search is scoped both by patient and by the specific visit (via 'client_order_ref') and excludes any line created before the ServiceRequest's own 'authoredOn' timestamp (a short tolerance was added for clock skew)
    
    Those two additions prevent a payment for one order to from being mistaken for payment of this one. Unless the sale.order state is 'cancel' (Task marked as 'rejected'), the account.move is queried for a fully paid invoice ('payment_state=paid' and 'amount_residual=0'); Once found, the Task is created and/or updated accordingly. 

    
``` mermaid
flowchart TD
    A["Active radiology<br/>ServiceRequest"]
    --> B["Find Odoo<br/>sale.order.line"]

    B --> C["Read linked<br/>sale.order"]

    C -->|state = cancel| D["Task.status = rejected"]

    C -->|not cancelled| E["Search account.move"]

    E -->|Fully paid| F["Task.status = accepted"]
    E -->|Not yet paid| G["Task.status = requested"]
    E -->|Check unavailable| G
```