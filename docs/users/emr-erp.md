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

## Data Flows between OpenMRS and ERPNext

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

!!! note "Override Default Behavior"

    Take control of your settings! Override the default options by supplying your custom configurations in the `ozone/distro/configs/eip-erpnext-openmrs/application.properties` file.


| Property Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                   | Default Value |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `erpnext.openmrs.enable.patient.sync` | Controls the automatic synchronization of patients from OpenMRS to ERPNext. When this property is set to `true`, a patient record created in OpenMRS is immediately mirrored as a customer record in ERPNext. If this property is set to `false`, the default behavior is followed, which is to create a customer record in ERPNext only when the first billable item for the patient is recorded in OpenMRS. | `false`       |

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
Each billable item ordered in OpenMRS for a patient is synchronized as a quotation item in the corresponding customer's draft ERPNext quotation.

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
a draft quotation is created in ERPNext based on the Patient's Visit.
When the visit is ended, the quotation is submitted.
Following submission, the quotation is eligible for conversion into a Sales Order.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS visit"]-- 1-to-1 -->b["ERPNext quotation"]
```

#### Prerequisite Flows

- [OpenMRS patient → ERPNext customer](#openmrs-patient-erpnext-customer)

#### Options

None
