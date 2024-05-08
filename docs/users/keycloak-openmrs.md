!!! info inline end ""

    {==:oz: Pro==}

# Keycloak-OpenMRS Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Keycloak
        OpenMRS->>Ozone: Roles
        Ozone->>Keycloak: Roles
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|OpenMRS|Role|→|Keycloak|Role|
|OpenMRS|Roles|⊝|Keycloak|{--Role--}|


## Flows Details

### **1** &nbsp; OpenMRS Role → Keycloak Role

A role in OpenMRS is synchronized as a role in Keycloak under the 'openmrs' client.

``` mermaid
flowchart LR
    a["OpenMRS role"]-- 1-to-1 -->b["Keycloak role"]
```

### **2** &nbsp; OpenMRS Roles ⊝ Keycloak Role

Keycloak roles under the 'openmrs' client that do not exist in OpenMRS are periodically deleted.

``` mermaid
flowchart LR
    a["OpenMRS roles"]-- delete -->b["Keycloak role"]
```