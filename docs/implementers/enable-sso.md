# Enabling and Disabling Single Sign-On (SSO)

Ozone HIS provides support for Single Sign-On (SSO), enabling users to authenticate once and seamlessly access all integrated applications without repeated logins. SSO is powered by [Keycloak](https://www.keycloak.org), which serves as the central Identity Provider (IDP) for managing authentication and authorization throughout the Ozone ecosystem.

With SSO enabled, all authentication requests are routed through Keycloak. It replaces each application's individual login page with a unified Keycloak login page for all users. This provides a consistent login experience across all integrated applications. For branding or user experience customization, you can modify the Keycloak login page, see [Customizing the Keycloak Login Page](../implementers/branding-apps.md#white-labelling-keycloak) for more details.

## SSO Implementation per App

Each application in Ozone HIS integrates with Keycloak using different mechanisms.

!!! info "ozone-realm.json"
    The `ozone-realm.json` file configures Keycloak by defining all client applications that will use Keycloak for authentication. Make sure each application (OpenMRS, Odoo, SENAITE...) has a corresponding client entry in this file, including the correct redirect URIs and required settings.

### OpenMRS

OpenMRS integrates with Keycloak for SSO using the [OpenMRS OAuth2 Login Module](https://github.com/openmrs/openmrs-module-oauth2login#openmrs-oauth-20-login-module). This module is included by default but is initially disabled, you can enable it by setting the `oauth2.enabled` property to true in the `oauth2.properties` file.

!!! warning "Basic auth is disabled"
     Enabling SSO in OpenMRS effectively disables basic authentication, so users will authenticate through the Keycloak login page rather than using traditional username and password prompts. No basic authentication will be allowed.

#### Configurations

- `oauth2.properties`: Located at `<your-distribution>/distro/configs/openmrs/properties/`. This file contains Keycloak
  server details, client ID, client secret, and other OAuth2 settings.
- Environment Variables: Set via Docker Compose environment variables in the `docker-compose-openmrs-sso.yml` file.
- `ozone-frontend-sso.json`: Located at `<your-distribution>/distro/configs/openmrs/frontend_config/`. This file
  contains frontend configurations for SSO, which configures `esm-login-app` frontend module to use OAuth2 login provider as well as login and logout URLs.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/openmrs/keycloak/`. Ensure that the OpenMRS client is defined in this file with the correct redirect URIs.
- `oauth2-login-props.xml` - Located at `distro/configs/openmrs/initializer_config/globalproperties/`. This file contains global properties for the OAuth2 login module. Specifically, it contains the `oauth2login.redirectUriAfterLogin` property, which is used to redirect users to the correct URL after login.

### Odoo

Odoo integrates with Keycloak using [`auth_oauth`](https://github.com/OCA/server-auth/tree/18.0/auth_oidc) addon by OCA community to provide SSO support. However, you can enable it by adding the `auth_oauth` addon to the `ODOO_ADDONS`environment variable.

#### Configurations:

- `auth.oauth.provider.csv` - Located at `<your-distribution>/configs/odoo/initializer_config/auth_providers/`. This file is used to configure the OAuth2 provider in Odoo. It contains the Keycloak server details, client ID, client secret, and other OAuth2 settings.
- `ODOO_ADDONS` - Set via Docker Compose environment variables in the `docker-compose-odoo-sso.yml` file to include the `auth_oauth` addon. Alternatively, this can be done by setting the `ODOO_ADDONS` environment variable in the `.env` file.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/odoo/keycloak/`. Ensure that the Odoo client is defined in this file with the correct configs and redirect URIs.

### SENAITE

SENAITE includes native support for SSO, so no additional modules or extensions are required. However, you must configure the Keycloak server and set up the necessary client settings in both Keycloak and SENAITE.

#### Configurations

- `client.json` - Located at `<your-distribution>/distro/configs/senaite/oidc/`. This file is used to configure/enable SSO in SENAITE. It contains the Keycloak server details, client ID, client secret, and other OAuth2 settings.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/senaite/keycloak/`. Ensure that the SENAITE client is defined in this file with the correct configs and redirect URIs. This file also contains the client ID and secret for the SENAITE client.

## Run Ozone with SSO

To run your distribution with SSO, you need to:

- Set the necessary environment variables. You can do this by exporting directly in your shell (e.g. `export ENABLE_SSO=true`) or set them in a `.env` file. The environment variables set in the `.env` file will be automatically picked up by Docker Compose when you run the Docker Compose files and will be available to all containers.
Below are the environment variables that you need to set:

| Environment Variable     | Example value                                                         | Description                                                   |
|--------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------|
| `ENABLE_SSO`             | `true`                                                                | Toggle SSO, enable or disable.                                |
| `SERVER_SCHEME`          | `https`                                                               | Scheme used in generated URLs (`http` or `https`).            |
| `O3_HOSTNAME`            | `example.com`                                                         | Hostname for the OpenMRS application.                         |
| `ODOO_HOSTNAME`          | `erp.example.com`                                                     | Hostname for the Odoo application.                            |
| `SENAITE_HOSTNAME`       | `lims.example.com`                                                    | Hostname for the SENAITE application.                         |
| `KEYCLOAK_HOSTNAME`      | `auth.example.com`                                                    | Hostname for the Keycloak identity provider.                  |
| `OPENMRS_CLIENT_ID`      | `dfcbd981-6c46-46f8-8688-8e99166148fa`                                | Keycloak client ID for OpenMRS.                               |
| `OPENMRS_CLIENT_SECRET`  | `3335594e-57ec-4211-832d-774ce20ace58`                                | Keycloak client secret for OpenMRS.                           |
| `ODOO_CLIENT_ID`         | `9170108c-fdf0-4d7e-ad0a-f485c98a3390`                                | Keycloak client ID for Odoo.                                  |
| `ODOO_CLIENT_SECRET`     | `362b43fe-6c80-41c9-9c0b-a60326480d60`                                | Keycloak client secret for Odoo.                              |
| `SENAITE_CLIENT_ID`      | `61a4c136-3658-4563-a986-415830551ea3`                                | Keycloak client ID for SENAITE.                               |
| `SENAITE_CLIENT_SECRET`  | `b70bcd8a-f75d-4598-8ff1-8be5db855fb6`                                | Keycloak client secret for SENAITE.                           |
| `OAUTH_CLIENT_ID`        | `56ac6ccf-004e-441f-a98b-8de7159f6ce9`                                | Generic OAuth client ID used by frontend auth modules.        |
| `OAUTH_CLIENT_SECRET`    | `043c6292-4f9b-4c8e-85ed-3172f43ae4ff`                                | Generic OAuth client secret.                                  |
| `OAUTH_CLIENT_SCOPE`     | `email,profile,openid`                                                | OAuth scopes requested during authentication.                 |
| `OAUTH_ACCESS_TOKEN_URL` | `https://auth.example.com/realms/ozone/protocol/openid-connect/token` | Token endpoint URL for obtaining access tokens from Keycloak. |

!!! note
    The above values are examples. Replace them with your actual domain names and client credentials.

!!! warning
    If Git or any version control is enabled for your project, ensure that sensitive files such as `.env` (containing secrets or credentials) are excluded from version control to protect sensitive information. This is to avoid accidental exposure of sensitive information.

- Use Docker Compose files that include the required SSO configurations. In Ozone, this means using the dedicated Keycloak file (`docker-compose-keycloak.yml`) along with application-specific files ending in `*-sso.yml` (for example, `docker-compose-openmrs-sso.yml` for OpenMRS). These files are provided in the Ozone package under `<your-distribution>/run/docker/`.
- First, navigate to the correct directory (`<path-to-your-distribution>/run/docker/`), or ensure you provide full paths to the Docker Compose files. Then, run Docker Compose with the required files. For example:
```bash
cd <path-to-your-distribution>/run/docker/

docker-compose -f docker-compose-common.yml -f docker-compose-keycloak.yml -f docker-compose-openmrs.yml -f docker-compose-openmrs-sso.yml -f docker-compose-odoo.yml -f docker-compose-odoo-sso.yml -f docker-compose-senaite.yml -f docker-compose-senaite-sso.yml up -d
```

Alternatively, use the `start-with-sso.sh` or `start-demo-with-sso.sh` scripts provided in the project. Follow the instructions in [Run Locally](../getting-started/run-locally.md) to download and start Ozone locally with SSO enabled. The scripts will set the necessary environment variables and include the appropriate Docker Compose files, which mount the required SSO binaries and configuration files as volumes.

## Run Without SSO

To run your distribution without SSO, simply set the `ENABLE_SSO` environment variable to `false` or leave it unset. Then, use the standard Docker Compose files without the SSO-specific files (any file with `-sso` suffix). For example:

```bash
docker-compose -f docker-compose-common.yml -f docker-compose-openmrs.yml -f docker-compose-odoo.yml -f docker-compose-senaite.yml up -d
```

By not including the SSO-specific Docker Compose files, the applications will use their default authentication mechanisms instead of Keycloak for authentication. This means users will log in directly to each application using their individual login pages. Ozone allows you to easily switch between SSO and non-SSO modes by adjusting the `ENABLE_SSO` environment variable and the Docker Compose files used to start the services. The applications will adapt accordingly based on the presence or absence of SSO configurations.

Ozone comes with default values for all the required environment variables to run without SSO. However, you can still set custom values for other environment variables (like hostnames and passwords) as needed.

Using the provided `start.sh` or `start-demo.sh` scripts will automatically run Ozone without SSO by default. These scripts set the necessary environment variables and include the standard Docker Compose files without SSO configurations. 

It is important to note that Ozone does not support enabling or disabling SSO on-the-fly while the services are running. Changes to the SSO configuration require a rebuild of the distribution with the appropriate settings, then rerun the Docker Compose setup to apply the changes. This doesn't only apply to enabling or disabling SSO but also to any changes in the distribution.

!!! question "Did you know?"
    Ozone {==:oz: Pro==} comes with Central Auth! Without central authentication, user roles from each app are not available in Keycloak. Central Auth enables synchronizing roles from all apps into Keycloak for unified access control and assignation. For more information, see [Central Auth](./enable-central-auth.md).
