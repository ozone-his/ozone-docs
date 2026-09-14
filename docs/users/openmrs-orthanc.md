# OpenMRS-Orthanc Flows

## Flows Overview

``` mermaid
    sequenceDiagram
        participant OpenMRS
        participant Ozone
        participant Orthanc
        Ozone->>OpenMRS: Read ServiceRequest
        Ozone->>OpenMRS: Query Task based on ServiceRequest
        alt Task.status = accepted
            Ozone->>Orthanc: Create modality worklist entry
        else Task not accepted
            Ozone-->>EIP_Orthanc: Do not create worklist entry
        end
        Orthanc->>Ozone: Study
        Orthanc->>Ozone: Series
        Orthanc->>Ozone: Instance
        Ozone->>OpenMRS: Attachment
```

## Flows List

| Source |Element| |Target|         Element          |
|:------:|:---:|:---:|:---:|:------------------------:|

| OpenMRS | Accepted FHIR Task | → | Orthanc | modality Worklist Entry |
| Orthanc | StructuredReport Title | → | OpenMRS | Result |
| Orthanc | Study | → | OpenMRS | Attachment |
| Orthanc | Series | ⭆ | OpenMRS | Attachment |
| Orthanc | Instance | ⭆ | OpenMRS | Attachment |


!!! question "What is an OpenMRS attachment?"

    In OpenMRS, an **attachment** is any file associated with a patient’s medical record. Attachments typically include files such as images or PDFs to which users can add titles and descriptions. Internally, attachments are managed as a special type of observation (`Obs` in the OpenMRS data model) that stores complex data (generally the binaries of the file itself).


!!! question "What is the FHIR Task used for?"

    The FHIR 'Task' represents the payment state associated with a radiology 'ServiceRequest'. 
Ozone only reads this 'Task'. It contains no Odoo-specific payment logic.



## Flows Details

An Orthanc imaging study consists of multiple series of image instances. In this lightweight integration, one image instance from the study is selected to serve as a simplified reference within OpenMRS. The selected instance is then saved as an attachment in OpenMRS.

Its description contains a direct link to the complete imaging study hosted in Orthanc.

### **1** &nbsp; Orthanc Study → OpenMRS Attachment

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

### **4** &nbsp; OpenMRS Order → Orthanc Worklist

``` mermaid
flowchart LR
    a["OpenMRS<br/>FHIR Task + Order passed"] -- 2-to-1 --> b["Orthanc<br/>Modality Worklist"]
```


!!! question "Is there a native FHIR mapping between Orthanc and OpenMRS?"

    Orthanc's own official FHIR plugin exposes exactly two resource types: 'Patient' and 'ImagingStudy'. Of these, only 'Patient' overlaps with OpenMRS's own FHIR2 module. Within the 'Patient' resource type, only 4 of its 14 supported search parameters ('family', 'given', 'identifier', 'birthdate') match between the two. 

    This overlap is already functionally usable today with no extra integration work:
    Since 'RadiologyOrderWorklistProcessor' already writes the OpenMRS patient UUID into the DICOM 'PatientID' tag when creating a worklist entry. A simple Orthanc FHIR API query with 'Patient?identifier=<openmrs-patient-uuid>' correctly returns that same patient. 'Patient.id' was correctly matching the OpenMRS UUID exactly. 

    There is no native FHIR equivalent for the 'Task'/'ServiceRequest' resources at the origin of the payment gating or worklist creation described above. The EIP bridges are consequently still required. 
