# EIP Client

## Overview

The Ozone EIP Client is a flexible Spring Boot application designed to facilitate seamless integration between different Health Information System (HIS) components. By leveraging Apache Camel routes and utilizing FHIR (Fast Healthcare Interoperability Resources) as the transport format, it acts as a powerful middleware solution. This setup ensures efficient management of data processing, routing, and transformation across systems. The application serves as a foundational platform for enabling smooth data exchange and integration between disparate HIS components.

## Technology Stack

Ozone EIP Client ergonomically combines the following technologies:

- **[:simple-springboot: Spring Boot <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://spring.io/projects/spring-boot)** (Java 17) - The core framework for the application. It provides a flexible and scalable platform for building Java applications.
- **[Apache Camel <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://camel.apache.org/)** - A powerful open source integration framework used to create routing between disparate systems. It provides a collection of libraries and components that facilitate the integration of systems. Some of the common used components include HTTP, JMS, and JDBC.
- **[:simple-hibernate: Hibernate <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://hibernate.org/)** - An object-relational mapping (ORM) library for the Java language that provides a framework for mapping an object-oriented domain model to a relational database.
- **[Testcontainers <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://testcontainers.com/)** - A Java library that provides lightweight, common databases that is, Postgres, MySQL, etc. or anything else that can run in a Docker container.
- **[:simple-junit5: JUnit 5 <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://junit.org/junit5/)** - A unit testing framework for Java programming language. It's a part of the JUnit platform that provides a rich set of features to write and run tests.

## Project Structure

The project is structured as follows:

- **`app`** - Contains the code and configurations responsible for running the camel routes. 
- **`commons`** - Contains common code and dependencies shared across the projects. This includes common utilities, models, and configurations.
- **`commons-test`** - Contains common test code and test dependencies shared across the projects. This includes common test utilities and configurations.

## Getting Started

To get started with EIP Client, you need to install the application and run it locally. Below are the steps to install and run the application:

1. Clone the repository using the following command:

    === "HTTPS"
        ```bash
        git clone https://github.com/ozone-his/eip-client.git
        ```
    
    === "GitHub CLI"
        ```bash
        gh repo clone ozone-his/eip-client
        ```

2. Navigate to the project directory:

    ```bash
    cd eip-client
    ```

3. Build the project using Maven:

    ```bash
    mvn clean install
    ```

## Running the Application

The Ozone EIP Client is ready to run right out of the box, but it's designed to be customized with your own Camel routes and configurations. Think of it as a blank canvas for your integration routes. It automatically searches for Camel routes in the `routes` directory and for configuration files in the `config` directory. Depending on your choice of setup, you can link these directories through Docker volumes or include them in the application's classpath.

Running the EIP Client is straightforward and can be done in several ways, including using the Spring Boot Maven plugin, Docker, or Docker Compose. The following sections will guide you through each method to get your application up and running.

### Spring Boot Maven Plugin

The Spring Boot Maven plugin is a powerful tool that simplifies the execution of Spring Boot applications directly from the command line. It eliminates the need for manual packaging and deployment steps, making development and testing processes more efficient.

#### Prerequisites

Before proceeding, ensure that Maven is installed and configured on your system. If you haven't installed Maven yet, follow the instructions on the [official Maven installation guide](https://maven.apache.org/install.html).

#### Running the app

To run the Ozone EIP Client application using the Spring Boot Maven plugin, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the root directory of the Ozone EIP Client project where the `pom.xml` file is located.

    ```bash
    cd path/to/eip-client/app
    ```

3. Execute the following command to run the application:

    ```bash
    mvn spring-boot:run
    ```

!!! info "Accessing the Application"
    This command will start the application on the default port (usually 8080, but this can be configured in the `application.properties` file). You can access the application health status by visiting `http://localhost:8080/actuator/health` in your web browser.

Using the Spring Boot Maven plugin is a quick and easy way to run the Ozone EIP Client application locally. It's ideal for development and testing purposes.

### Running the Application with Docker and Docker Compose

#### Pre-requisites

Before you begin, ensure you have Docker and Docker Compose installed on your system. If not, follow these steps:

1. **Install Docker:**
    - Visit the [official Docker website](https://docs.docker.com/get-docker/) and choose the installation guide for your operating system.
    - Follow the instructions to download and install Docker.

2. **Install Docker Compose:**
    - Docker Compose installation instructions can be found on the [official Docker website](https://docs.docker.com/compose/install/).
    - Follow the guide that corresponds to your operating system.

#### Understanding Docker Volumes

Docker volumes are used to persist data generated by and used by Docker containers. In the context of the Ozone EIP Client, volumes will be used to:

- _Mount the routes directory_, allowing the app to access external camel routes.
- _Mount the config directory_, enabling the app to access its external configuration files.
- _Mount the eip-home directory_, which may contain additional resources needed by the application.

#### Docker

You have two options for running the Ozone EIP Client with Docker:
building the image locally or pulling an existing image from Docker Hub.

1. **Building the Image Locally:**
    - Navigate to the project directory where the Dockerfile is located.
    - Build the Docker image using the following command:
      ```bash
      docker build -t eip-client .
      ```
    - Once the build is complete, you can run the container:
      ```bash
      docker run -p 8080:8080 -v /path/to/routes:/eip-client/routes/ -v /path/to/config:/eip-client/config/ -v /path/to/eip-home:/eip-client/eip-home/ eip-client
      ```

2. **Pulling an Existing Image from Docker Hub:**
    - If you prefer not to build the image yourself, you can pull an existing image from Docker Hub:
      ```bash
      docker pull mekomsolutions/eip-client:latest
      ```
    - Run the container with the same command as above, after pulling the image.

#### Docker Compose

Docker Compose simplifies the process of running Docker applications by using a `docker-compose.yml` file. Here's how to use it for the Ozone EIP Client:

1. Create a `docker-compose.yml` file with the following content:
   ```yaml
   services:
     eip-client:
       container_name: eip-client
       image: mekomsolutions/eip-client:latest
       ports:
         - "8080:8080"
       volumes:
         - ./routes:/eip-client/routes/
         - ./config:/eip-client/config/
         - ./eip-home:/eip-client/eip-home/
   ```
   This configuration sets up the necessary ports and volumes for the application.

    !!! info "Don't forget to replace the paths"
        Make sure to replace the paths in the `volumes` section with the actual paths to your routes, config, and eip-home directories.

2. Run the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```
   This command will start the Ozone EIP Client in a Docker container as defined in the `docker-compose.yml` file. The `-d` flag runs the container in detached mode, allowing you to continue using the terminal.

By following these steps, you can run Ozone EIP Client application using Docker and Docker Compose.

!!! info "Accessing the Application"
    Once the app is up and running, you can access application health status by visiting `http://localhost:8080/actuator/health` in your web browser.
    However, if you've configured a different port in the `application.properties` file, you should use that port number instead.

## Supporting Java DSL and XML Routes

EIP Client is designed to support both Apache Camel routes written in Java DSL and XML. This flexibility allows developers to choose the most suitable format for their integration routes.

### Java DSL Routes

For routes defined using Java DSL, you should package your routes into a JAR file. Once packaged, this JAR file needs to be placed in the `routes` directory of the EIP Client. The application will automatically detect and load these routes upon startup.

For Docker setup, directly mount the JAR file to the `/eip-client/routes` directory inside the container. This ensures that the application can access and load the Java DSL routes correctly.

### XML Routes

XML-defined routes can be directly placed in the `routes` directory. There's no need for compilation or packaging into a JAR file. Simply dropping the XML file into the directory is sufficient for the EIP Client to recognize and load these routes.

For Docker setups, mount the directory containing the XML files to the `/eip-client/routes` directory inside the container. This ensures that the application can access and load the XML routes correctly.

### Configurations

Configurations for both Java DSL and XML routes are managed through the `application.properties` file within the config directory. The `application.properties` file contains route-specific properties configured to meet the integration requirements.

For Docker and Docker Compose setup, the `config` directory should be mounted to the `/eip-client/config` directory inside the container. This ensures that the application reads the configuration properties correctly.
