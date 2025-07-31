# Enabling & Disabling HIS Components

Ozone uses Docker by default and its Docker Compose setup is stated as a dependency of the distribution by relying on the Ozone Docker Compose project:

```xml
<dependency>
  <groupId>com.ozonehis</groupId>
  <artifactId>ozone-docker-compose</artifactId>
  <type>zip</type>
</dependency>
```

!!! question "What if Docker can't be used?"
    
    Ozone's default deployment mechanism could be changed by depending on another deployment mechanism project than Ozone Docker Compose. Such alternatives, that are yet to be developed, could leverage Kubernetes, bare metal installation, Puppet, Vagrant, etc.

!!! info ""

    This guide will run you through the process of enabling and disabling Ozone HIS components when using Docker Compose as the deployment mechanism.

## Introducing `docker-compose-files.txt`

This key configuration file in the Ozone Docker Compose project serves as the default inventory of the various Docker Compose files that will be run when launching Ozone HIS. Its default content may look like this:

```text
docker-compose-common.yml
docker-compose-odoo.yml
docker-compose-openmrs.yml
docker-compose-senaite.yml
```

* The `docker-compose-common.yml` file defines shared services and configurations that are used across the entire Ozone HIS Docker Compose setup. It includes common settings and dependencies needed by multiple components.
* The `docker-compose-odoo.yml` file handles spinning up Odoo, `docker-compose-openmrs.yml` takes care of OpenMRS, and `docker-compose-senaite.yml` is responsible for SENAITE.

!!! info ""

    There will be a default Docker Compose file provided by Ozone for each supported component of the Ozone HIS FOSS ecosystem.

## Overriding `docker-compose-files.txt`

It is possible to define another setup than the Ozone default with your own version of `docker-compose-files.txt` that you would place here, where "`ozone-gruzinia`" is the top level folder of your distribution Maven project:

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