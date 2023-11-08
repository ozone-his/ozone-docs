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

#### Configurability

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

#### Configurability

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

#### Configurability

:construction: tbc