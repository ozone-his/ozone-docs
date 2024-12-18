# Keycloak-Odoo Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant Odoo
        participant Ozone
        participant Keycloak
        Odoo->>Ozone: Roles
        Ozone->>Keycloak: Roles
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|Odoo|Role|→|Keycloak|Role|
|Odoo|Roles|⊝|Keycloak|{--Role--}|


## Flows Details

### **1** &nbsp; Odoo Role → Keycloak Role

A role in Odoo is synchronized as a role in Keycloak under the 'odoo' client.

``` mermaid
flowchart LR
    a["Odoo role"]-- 1-to-1 -->b["Keycloak role"]
```

### **2** &nbsp; Odoo Roles ⊝ Keycloak Role

Keycloak roles under the 'odoo' client that do not exist in Odoo are periodically deleted.

``` mermaid
flowchart LR
    a["Odoo roles"]-- delete -->b["Keycloak role"]
```
