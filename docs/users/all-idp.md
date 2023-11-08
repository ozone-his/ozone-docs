# Data Flows between<br/>all components and the Identity Provider <span class="small-title">&nbsp;&nbsp;{==:oz: Pro==}</span>

## Data Flows between Keycloak and OpenMRS

### OpenMRS Role → Keycloak Role

#### Summary
A role in OpenMRS is synchronized as a role in Keycloak under the 'openmrs' client.

#### Main Flow
``` mermaid
flowchart LR
    a["OpenMRS role"]-- 1-to-1 -->b["Keycloak role"]
```

#### Prerequisite Flows

None

#### Configurability

None

## <small>:construction:</small> Data Flows between Keycloak and Superset