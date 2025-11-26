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
     Enabling SSO in OpenMRS effectively disables basic authentication, so users will authenticate through the Keycloak login page rather than using traditional username and password prompts.

#### Configurations

- `oauth2.properties` - Located at `<your-distribution>/distro/configs/openmrs/properties/`. This file contains Keycloak
  server details, client ID, client secret, and other OAuth2 settings.
- Environment Variables - Set via Docker Compose environment variables in the `docker-compose-openmrs-sso.yml` file.
- `ozone-frontend-sso.json` - Located at `<your-distribution>/distro/configs/openmrs/frontend_config/`. This file
  contains frontend configurations for SSO, which configures `esm-login-app` frontend module to use OAuth2 login
  provider as well as login and logout URLs.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/openmrs/keycloak/`. Ensure that the OpenMRS client
  is defined in this file with the correct redirect URIs.
- `oauth2-login-props.xml` - Located at `distro/configs/openmrs/initializer_config/globalproperties/`. This file
  contains global properties for the OAuth2 login module. Specifically, it contains the
  `oauth2login.redirectUriAfterLogin` property, which is used to redirect users to the correct URL after login.

### Odoo (ERP)

Odoo integrates with Keycloak using [`auth_oauth`](https://github.com/OCA/server-auth/tree/18.0/auth_oidc) addon by OCA community to provide SSO support. However, you can enable it by adding the `auth_oauth` addon to the `ODOO_ADDONS`environment variable.

#### Configurations:

- `auth.oauth.provider.csv` - Located at `<your-distribution>/configs/odoo/initializer_config/auth_providers/`. This
  file is used to configure the OAuth2 provider in Odoo. It contains the Keycloak server details, client ID, client
  secret, and other OAuth2 settings.
- `ODOO_ADDONS` - Set via Docker Compose environment variables in the `docker-compose-odoo-sso.yml` file to include the
  `auth_oauth` addon. Alternatively, this can be done by setting the `ODOO_ADDONS` environment variable in the `.env`
  file.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/odoo/keycloak/`. Ensure that the Odoo client is
  defined in this file with the correct configs and redirect URIs.

### SENAITE (LIMS)

SENAITE includes native support for SSO, so no additional modules or extensions are required. However, you must configure the Keycloak server and set up the necessary client settings in both Keycloak and SENAITE.

#### Configurations

- `client.json` - Located at `<your-distribution>/distro/configs/senaite/oidc/`. This file is used to configure/enable
  SSO in SENAITE. It contains the Keycloak server details, client ID, client secret, and other OAuth2 settings.
- `ozone-realm.json` - Located at `<your-distribution>/distro/configs/senaite/keycloak/`. Ensure that the SENAITE client
  is defined in this file with the correct configs and redirect URIs. This file also contains the client ID and secret
  for the SENAITE client.

## Run with SSO

To run with SSO, you need to:

- Set the necessary environment variables. You can do this by exporting directly in your shell (e.g. `export ENABLE_SSO=true`) or set them in a `.env` file. The environment variables set in the `.env` file will be automatically picked up by Docker Compose when you run the Docker Compose files and will be available to all containers.
Below are the environment variables that you need to set:

```bash
ENABLE_SSO=true
SERVER_SCHEME=https
O3_HOSTNAME=example.com
ODOO_HOSTNAME=erp.example.com
SENAITE_HOSTNAME=lims.example.com
KEYCLOAK_HOSTNAME=auth.example.com
OPENMRS_CLIENT_ID=2210d175-7bf0-4628-a2d5-2a2370161ef6
OPENMRS_CLIENT_SECRET=8FGsdeOPUG7ct2Diisb6A9LWkEzHHxDo
ODOO_CLIENT_ID=dbe398f0-7095-4230-ba1b-736397301a1c
ODOO_CLIENT_SECRET=y8PWKgBhIXR1k0qAw8vg3yfeD0zp4FUj
SENAITE_CLIENT_ID=711a9537-2efb-4ee2-92f4-bfd321f49605
SENAITE_CLIENT_SECRET=gSeajnyaU5vakcaFrOKWi6VvYRv6W8Zk
OAUTH_CLIENT_ID=fd0f7f3b-c42f-4613-a9e7-e8ffd720c5a5
OAUTH_CLIENT_SECRET=ZCURmSmiOqkkEuGRwChcrPBDkioVr0t6
OAUTH_CLIENT_SCOPE=email,profile,openid
OAUTH_ACCESS_TOKEN_URL=https://auth.example.com/realms/ozone/protocol/openid-connect/token
```

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

To run without SSO, follow the instructions in [here](../getting-started/run-locally.md) to download and start Ozone locally but instead of `start-with-sso.sh` or `start-demo-with-sso.sh`, use `start.sh` or `start-demo.sh` scripts. These scripts will include the correct Docker Compose files, mount required configs & binaries, and set the necessary environment variables. The scripts will exclude the Docker Compose files with the suffix `-sso.yml` and disable any SSO-related configurations.

If you already have your own Ozone distribution. The steps to run without SSO are similar to running with SSO, but you need to exclude the SSO-specific Docker Compose files and ensure that the `ENABLE_SSO` environment variable is set to `false` or not set at all.

!!! question "Did you know?"
    Ozone {==:oz: Pro==} comes with Central Auth! Without central authentication, user roles from each app are not available in Keycloak. Central Auth enables synchronizing roles from all apps into Keycloak for unified access control and assignation. For more information, see [Central Auth](./enable-central-auth.md).
