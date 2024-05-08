!!! info inline end ""

    {==:oz: Pro==}

# Keycloak-Superset Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant Superset
        participant Ozone
        participant Keycloak
        Superset->>Ozone: Roles
        Ozone->>Keycloak: Roles
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|Superset|Role|→|Keycloak|Role|
|Superset|Roles|⊝|Keycloak|{--Role--}|


## Flows Details

### **1** &nbsp; Superset Role → Keycloak Role

A role in Superset is synchronized as a role in Keycloak under the 'superset' client.

``` mermaid
flowchart LR
    a["Superset role"]-- 1-to-1 -->b["Keycloak role"]
```

### **2** &nbsp; Superset Roles ⊝ Keycloak Role

Keycloak roles under the 'superset' client that do not exist in Superset are periodically deleted.

``` mermaid
flowchart LR
    a["Superset roles"]-- delete -->b["Keycloak role"]
```