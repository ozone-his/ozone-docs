# Manual Setup

!!! tip

    Install Git, Maven and Docker Compose

## 1. Set up your working directory

Navigate to your preferred location, such as the home directory:
```bash
cd ~/
```

Create the Ozone working directory and store its path:
```bash
export OZONE_DIR=$PWD/ozone
mkdir -p $OZONE_DIR
cd $OZONE_DIR
```

## 2. Clone the Ozone project

```bash
git clone https://github.com/ozone-his/ozone-docker
cd ozone-docker
```

## 3. Create the public Docker network
!!! warning "Linux"

    Create the `docker` user group and add your user to it. Checkout the guide [here](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
```bash
docker network create web
```

??? warning "Linux - Docker as `sudo`"

    If Docker is run as `sudo` (which is not recommended) make sure to either export your environment variables as `su` as well, or use `sudo -E docker` to preserve the user's environment variables as `su`.

## 4. Clean up existing instances (optional)

If Ozone has been previously installed, you might need to clear your existing setup:

```bash
./destroy-demo.sh
```

## 5. Download and extract the distribution

```bash
export VERSION=1.0.0-alpha.7 && \
./mvnw org.apache.maven.plugins:maven-dependency-plugin:3.2.0:get -DremoteRepositories=https://nexus.mekomsolutions.net/repository/maven-public -Dartifact=com.ozonehis:ozone-distro:$VERSION:zip -Dtransitive=false --legacy-local-repository && \
./mvnw org.apache.maven.plugins:maven-dependency-plugin:3.2.0:unpack -Dproject.basedir=$OZONE_DIR -Dartifact=com.ozonehis:ozone-distro:$VERSION:zip -DoutputDirectory=$OZONE_DIR/ozone-distro-$VERSION
```

## 6. Set required environment variables

Ozone's Docker setup necessitates several environment variables to locate distribution assets. For the demo, export the necessary environment variables as shown:
```bash
export DISTRO_GROUP=ozone-demo; \

export DISTRO_PATH=$OZONE_DIR/ozone-distro-$VERSION;  \

export OPENMRS_CONFIG_PATH=$DISTRO_PATH/openmrs_config;  \
export OZONE_CONFIG_PATH=$DISTRO_PATH/ozone_config;  \
export OPENMRS_CORE_PATH=$DISTRO_PATH/openmrs_core;  \
export OPENMRS_MODULES_PATH=$DISTRO_PATH/openmrs_modules;  \
export EIP_PATH=$DISTRO_PATH/eip_config; \
export SPA_PATH=$DISTRO_PATH/spa;  \
export SENAITE_CONFIG_PATH=$DISTRO_PATH/senaite_config; \
export SUPERSET_CONFIG_PATH=$DISTRO_PATH/superset_config;  \

export ODOO_EXTRA_ADDONS=$DISTRO_PATH/odoo_config/addons;  \
export ODOO_CONFIG_PATH=$DISTRO_PATH/odoo_config/odoo_csv;  \
export ODOO_INITIALIZER_CONFIG_FILE_PATH=$DISTRO_PATH/odoo_config/config/initializer_config.json;  \
export ODOO_CONFIG_FILE_PATH=$DISTRO_PATH/odoo_config/config/odoo.conf;  \
export O3_FRONTEND_TAG=3.0.0-beta.13;  \
export O3_BACKEND_TAG=3.0.0-beta.13;
```

### Enabling Demo Data Service (optional)

The demo data service is optional and generates OpenMRS demo data 10 minutes post-Ozone startup, if enabled.

!!! info
    
    This service currently supports generating OpenMRS demo data only.

Activate the service and set the desired number of demo patients:
```bash
export NUMBER_OF_DEMO_PATIENTS=50
```

### Developer Note: Setting `DISTRO_PATH` (optional)

For Ozone developers working on local builds, `DISTRO_PATH` must point to your local distro directory:

```bash
export DISTRO_PATH=/your/path/to/ozone-distro/target/ozone-distro-$VERSION
```

## 7. Configure :simple-traefikproxy: Traefik Proxy (optional)

While optional, integrating Traefik as a reverse proxy is highly recommended for Ozone setups.

!!! warning

    Traefik will not work in Gitpod.

### Implementing Traefik Proxy

To utilize Traefik proxy with this project, ensure you have a running Traefik instance configured on the previously established `web` Docker network.

For convenience, use the ready-to-go Traefik setup available at [mekomsolutions/traefik-docker-compose-dev](https://github.com/mekomsolutions/traefik-docker-compose-dev) to bypass the configuration process.

Domains are recommended for Traefik. We employ the domain `traefik.me` specifically for this setup.

!!! info

    The `traefik.me` domain necessitates internet connectivity.

### Traefik hostnames

On Linux, `app-172-17-0-1.traefik.me` directly maps to Docker's host IP `172.17.0.1`. For macOS, Docker's dynamic IP requires using the host's current IP instead of `traefik.me` for configurations.

=== ":simple-linux: Linux"

    ```bash
    export O3_HOSTNAME=emr-172-17-0-1.traefik.me; \
    export ODOO_HOSTNAME=erp-172-17-0-1.traefik.me; \
    export SENAITE_HOSTNAME=lims-172-17-0-1.traefik.me; \
    export SUPERSET_HOSTNAME=analytics-172-17-0-1.traefik.me;
    ```

=== ":simple-apple: macOS"

    ```bash
    export IP="${$(ipconfig getifaddr en0)//./-}"; \
    export O3_HOSTNAME=emr-"${IP}.traefik.me"; \
    export ODOO_HOSTNAME=erp-"${IP}.traefik.me";  \
    export SENAITE_HOSTNAME=lims-"${IP}.traefik.me";  \
    export SUPERSET_HOSTNAME=analytics-"${IP}.traefik.me";  
    ```

??? bug "Apache 2 and the OpenMRS `/spahome` bug"

    Traefik addresses a common issue with Apache 2 where improper redirects to `/spahome` instead of `/spa/home` result in persistent 404 errors, which otherwise require manual URL adjustments in the browser.

## 8. Start Ozone

=== ":simple-apache: Apache 2"

    ```bash
    docker compose -f docker-compose.yml \ 
      -f docker-compose-proxy.yml \ 
      -f docker-compose-senaite.yml \ 
      -f docker-compose-odoo.yml \ 
      -f docker-compose-demo.yml \ 
      -p $DISTRO_GROUP up
    ```

=== ":simple-traefikproxy: Traefik"

    ```bash
    docker compose -f docker-compose.yml \ 
      -f docker-compose-senaite.yml \ 
      -f docker-compose-odoo.yml \ 
      -f docker-compose-demo.yml \ 
      -p $DISTRO_GROUP up
    ```

## 9. Browse Ozone

When all services are up and running, [start browsing Ozone](/#browse).