??? question "Wait, have you checked the online demo of Ozone Pro? :thinking:"

    Before diving into the Quick Start or implementer guides, visit <a href="https://www.ozone-his.com">our website</a> and click **Try Demo** to explore the official Ozone Pro online demo.

# Quick Start

=== ":fontawesome-solid-location-dot: Locally"

    Only three commands in a terminal:

    ```bash
    curl -s https://raw.githubusercontent.com/ozone-his/ozone/main/scripts/install-latest.sh | bash /dev/stdin
    ```

    ```bash
    cd ozone/run/docker/scripts/
    ./start-demo.sh
    ```

    !!! warning ""

        :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

    Then, start browsing Ozone. This requires you to log into each component separately:

    | **HIS Component** | **URL**                                                                                   |
    |-------------------|-------------------------------------------------------------------------------------------|
    | OpenMRS 3         | <a href="http://localhost/openmrs/spa" target="_blank">http://localhost/openmrs/spa</a>   |
    | SENAITE           | <a href="http://localhost:8081/senaite" target="_blank">http://localhost:8081/senaite</a> |
    | Odoo              | <a href="http://localhost:8069" target="_blank">http://localhost:8069</a>                 |
    | Superset          | <a href="http://localhost:8088" target="_blank">http://localhost:8088</a>                 |


=== ":simple-gitpod: Gitpod"

    Just one click:
    
    [![](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ozone-his/ozone/)

    !!! warning ""

        :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

    Gitpod will automatically launch a new tab for OpenMRS 3.

    You can navigate to other Ozone HIS components via the PORTS tab of the Gitpod window:

    ![Ozone services started](assets/images/gitpod-list-services.png)

Each component will require you to log in separately with their own credentials:

| **HIS Component** | **Username** | **Password** |
|-------------------|--------------|--------------|
| OpenMRS 3         | admin        | Admin123     |
| SENAITE           | admin        | password     |
| Odoo              | admin        | admin        |
| Superset          | admin        | password     |

!!! tip "**Did you know?**"

    Ozone Pro comes with [single sign-on](/users/sso) and all its interoperability layer is secured with OAuth2.
