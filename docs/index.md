# Quick Start

## Run Ozone

=== ":fontawesome-solid-location-dot: locally"

    Three lines in a terminal:

    Download and install Ozone 1.0.0-SNAPSHOT.
    ```bash
    curl -s https://raw.githubusercontent.com/ozone-his/ozone/main/scripts/install.sh | bash /dev/stdin 1.0.0-SNAPSHOT
    ```

    Run
    ```
    cd ozone/run/docker/scripts/
    ./start-demo.sh
    ```

    !!! warning ""

        :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

=== ":simple-gitpod: Gitpod"

    One click here:

    [![](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ozone-his/ozone/)

    !!! info ""

        When ready Gitpod will launch the browser tab for OpenMRS 3.


## <a href="#browse">Browse Ozone</a>

Then, start browsing Ozone. This requires you to log into each component separately:

=== ":simple-apache: Apache 2 (default)"

    | HIS Component     | URL                            | Username | Password |
    |-------------------|--------------------------------|----------|----------|
    | OpenMRS 3         | http://localhost/openmrs/spa   | admin    | Admin123 |
    | SENAITE           | http://localhost:8081/senaite  | admin    | password |
    | Odoo              | http://localhost:8069          | admin    | admin    |
    | Superset          | http://localhost:8088          | admin    | password |

=== ":simple-traefikproxy: Traefik"

    | HIS Component     | URL                                       | Username | Password |
    |-------------------|-------------------------------------------|----------|----------|
    | OpenMRS 3         | https://emr-172-17-0-1.traefik.me         | admin    | Admin123 |
    | SENAITE           | https://lims-172-17-0-1.traefik.me        | admin    | password |
    | Odoo              | https://erp-172-17-0-1.traefik.me         | admin    | admin    |
    | Superset          | https://analytics-172-17-0-1.traefik.me   | admin    | password |

!!! tip "**Did you know?**"

    Ozone Pro comes with [single sign-on and](/users/sso) all its interoperability layer is secured with OAuth2.