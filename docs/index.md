# Quick Start

## Run Ozone in Gitpod

Running Ozone in Gitpod is a button click away:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ozone-his/ozone-docker)

!!! info ""

    When ready Gitpod will launch the browser tab for OpenMRS 3.


## Run Ozone locally
Type in the following in a terminal:

```bash
git clone https://github.com/ozone-his/ozone-docker
cd ozone-docker
./start-demo.sh
```

!!! warning ""

    It may take some time to download and setup Ozone for the first time.

Then, start browsing Ozone. This requires you to log into each component separately:

| HIS Component     | URL                            | Username | Password |
|-------------------|--------------------------------|----------|----------|
| OpenMRS 3         | http://localhost/openmrs/spa  | admin    | Admin123 |
| OpenMRS Legacy UI | http://localhost/openmrs      | admin    | Admin123 |
| SENAITE           | http://localhost:8081/senaite | admin    | password |
| Odoo              | http://localhost:8069         | admin    | admin    |
| Superset          | http://localhost:8088         | admin    | password |

!!! tip "**Did you know?**"

    Ozone **Pro** :star2: comes with SSO[^sso] and all its integration layer is secured with OAuth2.

[^sso]: Single sign-on