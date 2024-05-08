# <small>:construction:</small> Configuration Points

In this section, we provide a comprehensive list of configuration points available in Ozone, organized by EIP services and thereby grouped by pairs of components.

## Keycloak-Superset Flows

###### `superset.polling-interval`

- _Location:_<br/>
`ozone/distro/configs/eip-keycloak-superset/properties/application.properties`
- _Possible values:_<br/>
The time in milliseconds. Defaults to 30000 – Controls the polling interval for the `eip-keycloak-superset` service, which regularly fetches the set of roles from Superset to synchronize them with Keycloak.

!!! tip "Sample configuration:"
    
    ```java
    superset.polling-interval=30000
    ```

## ERPNext-OpenMRS Flows

###### `erpnext.openmrs.enable.patient.sync`

- _Location:_<br/>
`ozone/distro/configs/eip-erpnext-openmrs/application.properties`
- _Possible values:_
    * [x] `false` – An OpenMRS patient is synchronised as an ERPNext customer when a first billable item is ordered from OpenMRS.
    * [ ] `true` – An OpenMRS patient is always synchronised as an ERPNext customer.

!!! tip "Sample configuration:"
    
    ```java
    erpnext.openmrs.enable.patient.sync=false
    ```

## Odoo-OpenMRS Flows