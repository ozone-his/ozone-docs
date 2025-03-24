!!! info ""

    This section of the Ozone Docs is designed for **digital health technical implementers**, focusing on how to install, configure, and run the Ozone HIS.

# Quick Start

??? question "Did you check the online demo? :thinking:"

    Before diving into the Quick Start or implementer guides, visit [our website]({{ homepage }}) and click **Try Demo** to explore the official Ozone Pro online demo.

=== ":fontawesome-solid-location-dot: Locally"

    Only three commands in a terminal:

    ```bash
    curl -s https://raw.githubusercontent.com/ozone-his/ozone/main/scripts/install-stable.sh | bash /dev/stdin
    ```

    ```bash
    cd ozone/run/docker/scripts/
    ```

    ```bash
    ./start-demo.sh
    ```

    !!! warning ""

        :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

    Then, start browsing Ozone. This requires you to log into each app of the HIS separately:

    | **App**                      | **URL**                                                                                     |
    |----------------------------------------|---------------------------------------------------------------------------------------------|
    | OpenMRS 3                              | <a href="http://localhost/openmrs/spa" target="_blank">http://localhost/openmrs/spa</a>     |
    | SENAITE                                | <a href="http://localhost:8081/senaite" target="_blank">http://localhost:8081/senaite</a>   |
    | Odoo                                   | <a href="http://localhost:8069" target="_blank">http://localhost:8069</a>                   |
    | Superset                               | <a href="http://localhost:8088" target="_blank">http://localhost:8088</a>                   |
    | Orthanc                                | <a href="http://localhost:8889/orthanc" target="_blank">http://localhost:8889/orthanc</a>   |
    | <span class='secondary'>ERPNext</span> | <a class='secondary' href="http://localhost:8082" target="_blank">http://localhost:8082</a> |

=== ":simple-gitpod: Gitpod"

    Just one click:
    
    [![](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/?autostart=true#https://github.com/ozone-his/ozone/tree/1.0.0-alpha.13)

    !!! warning ""

        :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

    Gitpod will automatically launch a new tab for OpenMRS 3.

    You can navigate to other Ozone apps of the HIS via the PORTS tab of the Gitpod window:

    ![Ozone services started](assets/images/gitpod-list-services.png)

Each app of the HIS will require you to log in separately with their own credentials:

| **App**                      | **Username**                                 | **Password**                            |
|----------------------------------------|----------------------------------------------|-----------------------------------------|
| OpenMRS 3                              | admin                                        | Admin123                                |
| SENAITE                                | admin                                        | password                                |
| Odoo                                   | admin                                        | admin                                   |
| Superset                               | admin                                        | password                                |
| Orthanc                               | orthanc                                       | orthanc                                 |
| <span class='secondary'>ERPNext</span> | <span class='secondary'>administrator</span> | <span class='secondary'>password</span> |

!!! tip "**Did you know?**"

    Ozone Pro comes with [single sign-on](/users/sso) and all its interoperability layer is secured with OAuth2.
