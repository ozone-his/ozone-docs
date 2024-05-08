# OpenMRS-SENAITE Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant SENAITE
        OpenMRS->>Ozone: Patients
        Ozone->>SENAITE: Clients
        OpenMRS->>Ozone: Lab test orders
        Ozone->>SENAITE: Analysis requests
        SENAITE->>Ozone: Analyses
        Ozone->>OpenMRS: Lab results
```

## Flows List

|Source|Element| |Target|Element|
|:---:|:---:|:---:|:---:|:---:|
|OpenMRS|Patient|→|SENAITE|Client|
|OpenMRS|Lab test order|→|SENAITE|Analysis request|
|SENAITE|Analyses|⭆|OpenMRS|Lab results bundle|

!!! question "What is an OpenMRS lab results bundle?"

    Lab results are represented in OpenMRS as observations (obs). A lab results bundle is a set of OpenMRS obs that can be either numeric or coded data types.

## Flows Details

### **1** &nbsp; OpenMRS Patient → SENAITE Client

A patient in OpenMRS is synchronized as a corresponding client in SENAITE.

``` mermaid
flowchart LR
    a["OpenMRS patient"]-- 1-to-1 -->b["SENAITE client"]
```

### **2** &nbsp; OpenMRS Lab Test Order → SENAITE Analysis Request

As soon as a lab test is first ordered for a patient in OpenMRS, an analysis request is created in SENAITE for the corresponding client.

``` mermaid
flowchart LR
    a["OpenMRS lab test order"]-- many-to-1 -->b["SENAITE analysis request"]
```

### **3** &nbsp; SENAITE Analyses ⭆ OpenMRS Lab Results Bundle

When an analysis request's analyses (or lab results) have been submitted in SENAITE, the lab results bundle is saved into OpenMRS as an array of obs.

``` mermaid
flowchart LR
    a["SENAITE analyses"]-- many-to-1 -->b["OpenMRS lab results bundle"]
```