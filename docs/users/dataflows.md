# HIS Data Flows Guide

!!! info

    The subsequent pages detail the data flows orchestrated by Ozone HIS across its supported components.
    <br/>This page serves as a guide on how to navigate and understand the information presented in the following sections.

#### **Title**

A concise directional wording for the data flow.

!!! example "Example: one to one (**→**)"

    Odoo invoice line **→** openIMIS claim item

!!! example "Example: many to one (**⭆**)"

    Odoo invoice lines **⭆** openIMIS claim

#### **Summary**

The summary provides a plain English description of the data flow, outlining its significance in the context of business processes.

!!! example

    _A customer medical invoice in Odoo synchronises as an insuree claim in openIMIS._

#### **Main Flow**

A simple flow chart is provided to illustrate the data's journey between components.

There are **1-to-1** data flows between a component and another.

!!! example

    ``` mermaid
    flowchart LR
        a["Odoo invoice line"]-- 1-to-1 -->b["openIMIS claim item"]
    ```

There are also **many-to-1** data flows between a component and another.

!!! example

    ``` mermaid
    flowchart LR
        a["Odoo invoice lines"]-- many-to-1 -->b["openIMIS claim"]
    ```

#### **Prerequisite Flows**

Certain data flows are dependent on preceding ones, known as _prerequisite flows_. While these initial flows must occur first, they typically execute automatically and don't require manual activation before the main flow begins. This section will be used to enumerate prerequisite flows, if any.

#### **Options**

This section enumerates the available options for the documented data flow and describes how to configure them.