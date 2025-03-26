# OpenMRS-Orthanc Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Orthanc
        Orthanc->>Ozone: Imaging study
        Orthanc->>Ozone: Series
        Orthanc->>Ozone: Instance
        Ozone->>OpenMRS: Attachment
```

## Flows List

| Source |Element| |Target|         Element          |
|:------:|:---:|:---:|:---:|:------------------------:|
| Orthanc |ImagingStudy | → | OpenMRS | Attachment |
| Orthanc |Series | ⭆ | OpenMRS | Attachment |
| Orthanc |Instance | ⭆ | OpenMRS | Attachment |


!!! question "What is an OpenMRS attachment?"

    In OpenMRS, an **attachment** is any file associated with a patient’s medical record. Attachments typically include files such as images or PDFs to which users can add titles and descriptions. Internally, attachments are managed as a special type of observation (`Obs` in the OpenMRS data model) that stores complex data (generally the binaries of the file itself).


## Flows Details

An Orthanc imaging study consists of multiple series of image instances. In this lightweight integration, one image instance from the study is selected to serve as a simplified reference within OpenMRS. The selected instance is then saved as an attachment in OpenMRS.

Its description contains a direct link to the complete imaging study hosted in Orthanc.

### **1** &nbsp; Orthanc Imaging Study → OpenMRS Attachment

This data flow synchronizes each Orthanc imaging study to an attachment (`Obs`) in the patient's OpenMRS record. Each attachment includes a soft reference to the originating imaging study by storing the study's URL in its description (the attachment's file caption).

``` mermaid
flowchart LR
    a["Orthanc imaging study"]-- 1-to-1 -->b["OpenMRS attachment"]
```

### **2** &nbsp; Orthanc Series ⭆ OpenMRS Attachment

In this implicit secondary flow, the image instance used for the OpenMRS attachment is selected from the first series within the Orthanc imaging study.

``` mermaid
flowchart LR
    a["Orthanc series"]-- many-to-1 -->b["OpenMRS attachment"]
```

### **3** &nbsp; Orthanc Instance ⭆ OpenMRS Attachment

In this implicit secondary flow, the first image instance from the first series of the Orthanc imaging study is selected for use as the OpenMRS attachment.

``` mermaid
flowchart LR
    a["Orthanc Instance"]-- many-to-1 -->b["OpenMRS attachment"]
```
