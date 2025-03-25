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
        Ozone->>OpenMRS: Obs (Attachment)
```

## Flows List

| Source |Element| |Target|         Element          |
|:------:|:---:|:---:|:---:|:------------------------:|
|Orthanc |Instance|⭆|OpenMRS| Obs (Attachment) |


!!! question "What is Obs (Attachment)?"

    An Attachment is represented as an complex Obs in OpenMRS. An Attachment can have a file, image, pdf with an Attachment title and description, in case of Orthanc, an Attachment has an image and a hyperlink to view the imaging study.

## Flows Details

### **1** &nbsp; Orthanc Instance → OpenMRS Obs (Attachment)

An Orthanc ImagingStudy consists of multiple series, each containing multiple instances. Each instance image is mapped to an OpenMRS Patient Obs as an Attachment.

``` mermaid
flowchart LR
    a["Orthanc Instance"]-- many-to-1 -->b["OpenMRS Obs (Attachment)"]
```
