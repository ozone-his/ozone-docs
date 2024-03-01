# Ozone HIS Quick Start

=== ":fontawesome-solid-location-dot: Run locally"

    Three commands:

    ```bash
    curl -s https://raw.githubusercontent.com/ozone-his/ozone/main/scripts/install-latest.sh | bash /dev/stdin
    ```

    ```bash
    cd ozone/run/docker/scripts/
    ```

    ```bash
    ./start-demo.sh
    ```

=== ":simple-gitpod: Run in Gitpod"

    One click:
    
    [![](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ozone-his/ozone/)


!!! warning ""

    :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

=== ":fontawesome-solid-location-dot: Browse locally"

    Then, start browsing Ozone. This requires you to log into each component separately:

    | **HIS Component** | **URL**                                                        |
    |-------------------|----------------------------------------------------------------|
    | OpenMRS 3         | [http://localhost/openmrs/spa](http://localhost/openmrs/spa)   |
    | SENAITE           | [http://localhost:8081/senaite](http://localhost:8081/senaite) |
    | Odoo              | [http://localhost:8069](http://localhost:8069)                 |
    | Superset          | [http://localhost:8088](http://localhost:8088)                 |

=== ":simple-gitpod: Browse in Gitpod"

    Gitpod will automatically launch a new tab for OpenMRS 3.

    You can navigate to other Ozone HIS components via the PORTS tab of the Gitpod window:

    ![Ozone services started](assets/images/gitpod-list-services.png)

**Default Credentials**

Each component will require you to log in separately:

| **HIS Component** | **Username** | **Password** |
|-------------------|--------------|--------------|
| OpenMRS 3         | admin        | Admin123     |
| SENAITE           | admin        | password     |
| Odoo              | admin        | admin        |
| Superset          | admin        | password     |

!!! tip "**Did you know?**"

    Ozone Pro comes with [single sign-on](/users/sso) and all its interoperability layer is secured with OAuth2.
