This guide is divided into three sections, corresponding to a typical approach for assessing software and tools used in digital health interventions:

``` mermaid
stateDiagram-v2
    direction LR

    classDef EvalClass fill:#FCF4E5
    classDef AdoptClass fill:#B5C5E7
    classDef DeployClass fill:#F5CAB3
    

    state "<b>1</b> &nbsp; Evaluate" as eval
    state "<b>2</b> &nbsp; Adopt" as adopt
    state "<b>3</b> &nbsp; Deploy" as deploy

    eval --> adopt
    adopt --> deploy
    deploy --> adopt

    class eval EvalClass
    class adopt AdoptClass
    class deploy DeployClass
```

!!! tip
    Use the left-hand menu to navigate the subguides and technical resources available under **Evaluate**, **Adopt**, and **Deploy**.

## **1** &nbsp; Evaluate

First and foremost, it is important to evaluate what Ozone is and explore how it may look to end users. The easiest way to do this is by exploring the **Ozone Demo**. There are three immediate options:

- Browse the online {==:oz: Pro==} demo  
- Run Ozone FOSS locally
- Run Ozone FOSS in Gitpod  

We also recommend reaching out via our website to request a guided Ozone deep dive and demo.

!!! info "About the Ozone Demo"
    The Ozone Demo is _one_ opinionated example of a typical HIS implemented with Ozone.  
    It serves to illustrate a realistic end-user experience, but does not represent the full range of outcomes and customizations possible with Ozone.

## **2** &nbsp; Adopt
Once you've confirmed Ozone is suitable for your project, the next step is to create your own customized copy (distribution) of Ozone. We provide a comprehensive toolkit to help implementers easily set up their own distribution. This custom distribution will initially inherit Ozone’s defaults, and can be progressively configured and customized to your needs while continuing to benefit from the latest features and improvements from Ozone.

## **3** &nbsp; Deploy

Once your Ozone distribution is packaged and ready, you can deploy it to your servers. Ozone includes utility scripts to streamline deployment, built-in backup and restore capabilities, and integrated monitoring.

Typically, you'll experience some iteration between "Adopt" and "Deploy"—configuring, deploying, reviewing, and refining until your environment matches your needs.

This section also provides troubleshooting tips and solutions to common deployment issues.
