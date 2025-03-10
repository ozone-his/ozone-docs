# Enabling & Disabling HIS Components
!!! info ""


    This guide will run you through the process of enabling and disabling Ozone HIS components when using Docker Compose as the deployment mechanism. We assume you have already created your own distribution using the Ozone Distro Maven Archetype. If you haven't, please refer to [Ozone Distro Maven Archetype](http://localhost:8000/create-distro/)

## Ozone Deployment scenarios

In real world usage you may not necessarily want to enable all of the components. Ozone is designed to be modular and you can enable or disable components as needed. Below are some of the common scenarios you may encounter;

### Running Only the EMR
The core funcionality of Ozone is built around the EMR component so in a barebone setup you are likely going to want to run only the EMR component. At the moment Only OpenMRS 3 is supported

### Running Ozone with an ERP
In deployments where billing and stock management is needed you can run Ozone with an ERP. Ozone has 2 options for the ERP you can run Ozone with Odoo or ERPNext. Take a look at the Matrix below for how to combine Ozone the ERP of choice

### Running Ozone with a LIMS
In deployments where a Lab is available you can run Ozone a LIMS. Ozone supports SENAITE as the LIMS component. See the Matrix below for how to combine with a LIMS 

### Ozone Component Matrix

<table>
  <tr>
    <th>File</th>
    <th>O3</th>
    <th>O3</th>
    <th>Odoo</th>
    <th>O3</th>
    <th>ERPNext</th>
    <th>O3</th>
    <th>SENAITE</th>
    <th>O3</th>
    <th>Odoo</th>
    <th>SENAITE</th>
    <th>O3</th>
    <th>ERPNext</th>
    <th>SENAITE</th>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-common.yml</td>
   <td align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="3" align="center" valign="center" >&#10003;</td>
    <td colspan="3" align="center" valign="center">&#10003;</td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-openmrs.yml</td>
   <td align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="3" align="center" valign="center" >&#10003;</td>
    <td colspan="3" align="center" valign="center">&#10003;</td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-openmrs-sso.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-odoo.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" >&#10003;</td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-odoo-sso.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-erpnext.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center">&#10003;</td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-erpnext-sso.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-senaite.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center">&#10003;</td>
    <td colspan="3" align="center" valign="center" >&#10003;</td>
    <td colspan="3" align="center" valign="center">&#10003;</td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-senaite-sso.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
  <tr>
    <td align="center" valign="center">docker-compose-keycloak.yml</td>
   <td align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="2" align="center" valign="center"></td>
    <td colspan="3" align="center" valign="center" ></td>
    <td colspan="3" align="center" valign="center"></td>
  </tr>
</table>


## The  `docker-compose-files.txt`  file
This is the main configuration file used to configure the Ozone components that are available for a give Distro. It contains a list of Docker Compose files that are used to enable the Ozone HIS components. The file is located in the `scripts` directory of the distribution. Below are the files included in the Kitchen Sink Ozone His distribution


| File | Details |
|--|--|
|docker-compose-common.yml  | This file defines shared services and configurations that are used across the entire Ozone HIS Docker Compose setup. It includes common settings and dependencies needed by multiple components. |
|docker-compose-openmrs.yml| This file defines the OpenMRS backend , OpenMRS Frontend, extra MySQL configurations required by OpenMRS (Volumes and ENV variables) and ENV substitution service configuration for OpenMRS|
|docker-compose-openmrs-sso.yml|This file contains extra configuration needed to enable Single Sign On for OpenMRS it contains overrides for the OpenMRS,the OpenMRS frontend and the ENV substitution service|
|docker-compose-odoo.yml|This file defines Odoo , [Odoo FHIR](https://github.com/ozone-his/fhir-odoo) , Odoo OpenMRS EIP client to sync data from OpenMRS to Odoo, PostgreSQL overrides for Odoo , MySQL overrides for Odoo OpenMRS EIP client and the ENV substitution service overrides|
|docker-compose-odoo-sso.yml|This file contains extra configuration needed to enable Single Sign On for Odoo it contains SSO overrides for the Odoo, and the ENV substitution service , Odoo OpenMRS EIP client and the ENV substitution|
|docker-compose-erpnext.yml|This file defines the ERPNext backend and supporting services , ERPNext OpenMRS EIP client and extra MySQL configurations required by ERPNext OpenMRS EIP client|
|docker-compose-erpnext-sso.yml|This file contains extra configuration needed to enable Single Sign On for ERPNext it contains overrides for ERPNext and ERPNext OpenMRS EIP client|
|docker-compose-senaite.yml|This file defines the SENAITE service, The OpenMRS SENAITE EIP client, PostgreSQL overrides for SENAITE and MySQL overrides for OpenMRS SENAITE EIP client|
|docker-compose-senaite-sso.yml|This file contains extra configuration needed to enable Single Sign On for SENAITE it contains SSO overrides for SENAITE , OpenMRS SENAITE EIP client and ENV substitution |
|docker-compose-keycloak.yml|This file defines the Keycloak which is the IDP used for SSO, PostgreSQL overrides for Keycloak and ENV substitution overrides for Keycloak|



## Overriding the `docker-compose-files.txt` file

Ozone uses Docker by default and its Docker Compose setup is stated as a dependency of the distribution by relying on the Ozone Docker Compose project:

```xml
<dependency>
  <groupId>com.ozonehis</groupId>
  <artifactId>ozone-docker-compose</artifactId>
  <type>zip</type>
</dependency>
```

Following the Ozone Matrix above you can define your own version of `docker-compose-files.txt` to replace the default one. Take for example the distribution "`ozone-gruzinia`" you can create a new `docker-compose-files.txt` in the scripts folder as shown below:

```bash
ozone-gruzinia
    └── scripts
           └── docker-compose-files.txt
```

When doing so, it will be your override file located in the `scripts` directory that will be taken into account, rather than the default file provided by Ozone Docker Compose. This allows you to enable or disable the HIS components of your choice by modifying your version of `docker-compose-files.txt`.

For instance, the following setup would disable Odoo and use ERPNext as the ERP system within Ozone HIS:

!!! tip "Changing the default ERP system to ERPNext in `docker-compose-files.txt`"
    ```text
    docker-compose-common.yml
    {==docker-compose-erpnext.yml==}
    docker-compose-openmrs.yml
    docker-compose-senaite.yml
    ```

This was achieved by removing `docker-compose-odoo.yml` (disabling Odoo) and adding `docker-compose-erpnext.yml` (enabling ERPNext).

!!! example "OpenMRS Distro HIS with ERPNext"

    The OpenMRS Distro HIS is a starter distribution of OpenMRS that demonstrates integration with other digital health software, such as an ERP system. It uses ERPNext instead of Odoo, which is Ozone's default ERP component. To achieve this, it overrides `docker-compose-files.txt` as described above.

    See [here <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://github.com/openmrs/openmrs-distro-his/blob/379f0b600493dac04b46b8283f97bc5d9e7aa089/scripts/docker-compose-files.txt) how this is done.

## Further customizing Docker Compose files with `docker-compose-override.yml`

It is also possible to provide an additional `docker-compose-override.yml`[^override] to tweak the default Docker Compose files provided by Ozone Docker Compose without modifying them directly. This pattern is crucial for ensuring that implementers can utilize the default Docker Compose files provided by Ozone as much as possible before needing to maintain their own versions of them.

[^override]: The YAML file name doesn't matter and can be chosen freely. Additionally, you can have as many additional Docker Compose files as desired.

!!! tip "Adding a `docker-compose-override.yml` in `docker-compose-files.txt`"
    ```text
    docker-compose-common.yml
    docker-compose-odoo.yml
    docker-compose-openmrs.yml
    docker-compose-senaite.yml
    {==docker-compose-override.yml==}
    ```

### Examples of customizations with `docker-compose-override.yml`

!!! example "Adding OpenMRS frontend configuration files"

    The OpenMRS Distro HIS requires to run its own configuration of the OpenMRS frontend. See [here <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://github.com/openmrs/openmrs-distro-his/blob/379f0b600493dac04b46b8283f97bc5d9e7aa089/scripts/docker-compose-override.yml#L5) how this can be done.

!!! example "Bespoke initialisation of OpenMRS' MySQL database"

    This bespoke configuration ensures that the MySQL service starts with specific settings tailored for the KenyaHMIS project. It also initializes the database with necessary SQL scripts that update and configure the database schema and data according to the project’s requirements.

    See [here <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://github.com/palladiumkenya/kenyahmis/blob/b24503fd623d6b9c06a94d1af3588c15b463abf6/scripts/docker-compose-override.yml) how this can be done.



