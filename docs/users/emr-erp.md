# Data Flows between<br/>EMR Systems and ERP Systems

## Data Flows between Odoo and OpenMRS

### OpenMRS Patient → Odoo Customer

#### Summary
A patient in OpenMRS is synchronized as a customer in Odoo.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS patient"]-- 1-to-1 -->b["Odoo customer"]
```

#### Prerequisite Flows

None

#### Options

:construction: tbc

### OpenMRS Billable Items ⭆ Odoo Quotation

#### Summary
As soon as the first billable item is ordered for a patient in OpenMRS, a quotation is created in Odoo for the corresponding customer.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["Odoo quotation"]
```

#### Prerequisite Flows

- [OpenMRS patient → Odoo customer](#openmrs-patient-odoo-customer)

#### Options

None

### OpenMRS Billable Item → Odoo Quotation Line

#### Summary
Each billable item ordered in OpenMRS for a patient is synchronized as a line item in the corresponding customer's open Odoo quotation.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["Odoo quotation line"]
```

#### :construction: Billable Items

- Drug order
- Lab test order
- Service order

#### Prerequisite Flows

- [OpenMRS patient → Odoo customer](#openmrs-patient-odoo-customer)
- [OpenMRS billable item ⭆ Odoo quotation](#openmrs-billable-items-odoo-quotation)

#### Options

:construction: tbc

## Data Flows between ERPNext and OpenMRS 

### OpenMRS Patient → ERPNext Customer

#### Summary
A patient in OpenMRS is synchronized as a customer in ERPNext.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS patient"]-- 1-to-1 -->b["ERPNext customer"]
```

#### Prerequisite Flows

None

#### Options

=== "Behaviour"

    - <small>**default**</small> &nbsp; An OpenMRS patient is synchronised as an ERPNext customer when a first billable item is ordered from OpenMRS.
    - <small>_optional_</small> &nbsp; An OpenMRS patient is always synchronised as an ERPNext customer.

=== "Configuration"

    - File:<br/>`ozone/distro/configs/eip-erpnext-openmrs/application.properties`
    - Property name:<br/>`erpnext.openmrs.enable.patient.sync`
    - Possible values:<br/>`false` (<small>**default**</small>), `true`

### OpenMRS Billable Items ⭆ ERPNext Quotation

#### Summary
As soon as the first billable item is ordered for a patient in OpenMRS,
a quotation is created in ERPNext for the corresponding customer.
Billable items ordered in the same visit are added to the same quotation as quotation items.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS billable items"]-- many-to-1 -->b["ERPNext quotation"]
```

#### Prerequisite Flows

- [OpenMRS patient → ERPNext customer](#openmrs-patient-erpnext-customer)
- [OpenMRS Visit → ERPNext Quotation](#openmrs-visit-erpnext-quotation)

#### Options

None

### OpenMRS Billable Item → ERPNext Quotation Line

#### Summary
Each billable item ordered in OpenMRS for a patient is synchronized in ERPNext as a quotation item in the corresponding customer's draft quotation.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS billable item"]-- 1-to-1 -->b["ERPNext quotation Item"]
```

#### Billable Items

- Drug order
- Lab test order
- Service order

#### Prerequisite Flows

- [OpenMRS patient → ERPNext customer](#openmrs-patient-erpnext-customer)
- [OpenMRS Visit → ERPNext Quotation](#openmrs-visit-erpnext-quotation)

#### Options

None

### OpenMRS Visit → ERPNext Quotation

#### Summary
As soon as the first billable item is ordered for a patient in OpenMRS,
a draft quotation is created in ERPNext based on the patient's visit.
When the visit is ended, the quotation is submitted.
Following submission, the quotation is eligible for conversion into a sales order.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS visit"]-- 1-to-1 -->b["ERPNext quotation"]
```

#### Prerequisite Flows

- [OpenMRS patient → ERPNext customer](#openmrs-patient-erpnext-customer)

#### Options

None
