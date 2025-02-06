# OpenMRS-Orthanc Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Orthanc
        Orthanc->>Ozone: ImagingStudy
        Orthanc->>Ozone: Series
        Orthanc->>Ozone: Instance
        Ozone->>OpenMRS: Observation (Attachment)
```

## Flows List

| Source |Element| |Target|         Element          |
|:------:|:---:|:---:|:---:|:------------------------:|
|Orthanc |Instance|⭆|OpenMRS| Observation (Attachment) |


!!! question "What is Observation (attachment)?"

    An attachment is represented as an complex Obs in OpenMRS. An Attachment can have a file, image, pdf with an Attachment title and description, in case of Orthanc, an attachment has an image and a hyperlink to view the imaging study.

## Flows Details

### **1** &nbsp; Orthanc Instance → OpenMRS Observation (attachment)

An Orthanc ImagingStudy has multiple series, each series has multiple instances an instance image is mapped to OpenMRS Patient Observation as an attachment.

``` mermaid
flowchart LR
    a["Orthanc Instance"]-- many-to-1 -->b["OpenMRS Observation (attachment)"]
```
