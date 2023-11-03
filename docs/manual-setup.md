# Manual Setup

!!! tip

    Install Git, Maven and Docker Compose

!!! warning "Linux"

    Create the `docker` user group and add your user to it. Checkout the guide [here](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

!!! warning "Linux"

    If Docker is run as `sudo` (which is not recommended) make sure to either export your environment variables as `su` as well, or use `sudo -E docker` to preserve the user's environment variables as `su`.


## 1. Create your working directory

Move to the location of your choice, e.g., your home folder:

```bash
cd ~/
```

Then create the Ozone working directory and save the path:
```bash
export OZONE_DIR=$PWD/ozone && \
mkdir -p $OZONE_DIR && cd $OZONE_DIR
```
## 2. Clone the ozone-docker project

```bash
git clone https://github.com/ozone-his/ozone-docker
```

```bash
cd ozone-docker
```

## 3. Create the public Docker network
```bash
docker network create web
```

## 4. Destroy the running instance containers
!!! warning

    If you have already set up Ozone before you may need to clean up your local environment first:<br/>

```bash
./destroy-demo.sh
```

## 5. Download and extract the distribution

```bash
export VERSION=1.0.0-alpha.7&& \
./mvnw org.apache.maven.plugins:maven-dependency-plugin:3.2.0:get -DremoteRepositories=https://nexus.mekomsolutions.net/repository/maven-public -Dartifact=com.ozonehis:ozone-distro:$VERSION:zip -Dtransitive=false --legacy-local-repository && \
./mvnw org.apache.maven.plugins:maven-dependency-plugin:3.2.0:unpack -Dproject.basedir=$OZONE_DIR -Dartifact=com.ozonehis:ozone-distro:$VERSION:zip -DoutputDirectory=$OZONE_DIR/ozone-distro-$VERSION
```

## 6. Export all needed environment variables

The Ozone Docker project relies on a number of environment variables (env vars) to document where the distro assets are expected to be found.
For the sample demo you can export the following env vars:
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
### How to activate demo data generation

The generation of demo data is handled by a separate service that can be opted in or out. This service is configured with an EIP route that takes care of generating demo data 10 minutes after Ozone has started.

!!! info

    The demo data service currently only handles _OpenMRS_ demo data.

To set the number of demo patients to be generated:
```bash
export NUMBER_OF_DEMO_PATIENTS=50
```
### For developers: Override of `DISTRO_PATH`

If you are doing development on Ozone and are building the Ozone distro in your local environment, then you would need to override `DISTRO_PATH` to point to your distro build folder. For example if your working folder is `/your/path/to/ozone-distro` for the distro then you would want to do something like this:
```bash
export DISTRO_PATH=/your/path/to/ozone-distro/target/ozone-distro-$VERSION
```

## 7. Set up Traefik

This step is optional but recommended since Traefik brings many benefits as a reverse proxy for your Ozone project. 

Traefik solves a known URL redirection issue that will show up when using Apache 2. Incorrect `/spahome` redirections occur (instead of of the correct `/spa/home` path), leading to disrupting 404 errors that need to be corrected manually by changing the incorrect URL in the browser's address bar.

!!! warning

    Traefik will not work in Gitpod.

### Using Traefik proxy

When you select to use Traefik as the proxy for this project, it requires a properly configured Traefik reverse proxy that is already running in the `web` Docker network that was created earlier.
To make things easier for development purposes, you can use a pre-configured Traefik reverse proxy that is provided at [mekomsolutions/traefik-docker-compose-dev](https://github.com/mekomsolutions/traefik-docker-compose-dev). This saves you the time and effort required to set up and configure a new Traefik reverse proxy from scratch.

It is better to use domains with Traefik and we will rely on the special domain `traefik.me` for this purpose.

!!! info

    The special domain `traefik.me` requires access to the Internet.

### Traefik hostnames on macOS

In Linux, the domain `app-172-17-0-1.traefik.me` will resolve the Docker host IP `172.17.0.1` without any special considerations. However, Docker desktop for macOS does not provide a static IP address, which makes it challenging to use the `traefik.me` domain in the same way.

The only way to use the `traefik.me` domain with Docker on macOS is to use the IP address assigned to the host. This means that instead of using `app-172-17-0-1.traefik.me`, you would need to use the IP address of the Docker host machine in your configuration.

The default hostnames below will only work on Linux:
```bash
export O3_HOSTNAME=emr-172-17-0-1.traefik.me; \
export ODOO_HOSTNAME=erp-172-17-0-1.traefik.me; \
export SENAITE_HOSTNAME=lims-172-17-0-1.traefik.me; \
export SUPERSET_HOSTNAME=analytics-172-17-0-1.traefik.me;
```
On macOS you need the extra step to set the IP to your ethernet IP like this:
```bash
export IP="${$(ipconfig getifaddr en0)//./-}"; \
export O3_HOSTNAME=emr-"${IP}.traefik.me"; \
export ODOO_HOSTNAME=erp-"${IP}.traefik.me";  \
export SENAITE_HOSTNAME=lims-"${IP}.traefik.me";  \
export SUPERSET_HOSTNAME=analytics-"${IP}.traefik.me";  
```

## 8. Start Ozone
### With Apache 2

```bash
docker compose -f docker-compose.yml -f docker-compose-proxy.yml -f docker-compose-senaite.yml -f docker-compose-odoo.yml -f docker-compose-demo.yml -p $DISTRO_GROUP up
```
### With Traefik

```bash
docker compose -f docker-compose.yml -f docker-compose-senaite.yml -f docker-compose-odoo.yml -f docker-compose-demo.yml -p $DISTRO_GROUP up
```

## 9. Browse Ozone
Ozone FOSS requires you to log into each component separately:

| HIS Component     | Apache 2 URL                  | Traefik (Linux) URL                       | Username | Password |
|-------------------|-------------------------------|-------------------------------------------|----------|----------|
| OpenMRS 3         | http://localhost/openmrs/spa  | https://emr-172-17-0-1.traefik.me         | admin    | Admin123 |
| OpenMRS Legacy UI | http://localhost/openmrs      | https://emr-172-17-0-1.traefik.me/openmrs | admin    | Admin123 |
| SENAITE           | http://localhost:8081/senaite | https://lims-172-17-0-1.traefik.me        | admin    | password |
| Odoo              | http://localhost:8069         | https://erp-172-17-0-1.traefik.me         | admin    | admin    |
| Superset          | http://localhost:8088         | https://analytics-172-17-0-1.traefik.me   | admin    | password |

??? warning "Traefik on macOS"

    With Traefik on macOS the IP coordinates of Ozone's components will be different and you will have to replace "`172-17-0-1`" with your host IP.
    <br/>For example if your host IP is `192.168.200.197`, then `https://emr-172-17-0-1.traefik.me` will have to become `https://emr-192-168-200-197.traefik.me`.
