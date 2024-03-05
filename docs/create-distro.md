# Create Your Own Distribution

!!! tip

    Install Git, Maven and Docker Compose

HIS systems, like Ozone, often need to be heavily customized based on local needs. Ozone facilitates implementer's work by providing custom implementation configurations via a series of tools built on Apache Maven. The starting-point for a custom implementation is the Ozone Maven Archetype which creates a skeleton project that serves as a base for any particular customizations an implementation needs.

## Maven Archetype


#### Configure Maven

Edit your Maven `settings.xml` file (often located in `~/.m2/settings.xml`) and add the following block to it:
```xml
  <profiles>
    <profile>
      <id>ozone</id>
      <repositories>
        <repository>
          <id>archetype</id>
          <url>https://nexus.mekomsolutions.net/repository/maven-public</url>
          <releases>
            <enabled>true</enabled>
            <checksumPolicy>fail</checksumPolicy>
          </releases>
          <snapshots>
            <enabled>true</enabled>
            <checksumPolicy>warn</checksumPolicy>
          </snapshots>
        </repository>
      </repositories>
    </profile>
  </profiles>

  <activeProfiles>
    <activeProfile>ozone</activeProfile>
  </activeProfiles>
```


#### Generate the Archetype

To get started, use Maven's archetype tools to generate a new Ozone implementation project. The command for doing this is:

```bash
 mvn archetype:generate -DarchetypeArtifactId=maven-archetype -DarchetypeGroupId=com.ozonehis
```

This will prompt you for several key variables for your implementation:

* **distributionName:** A user-friendly name for your distribution. For example, an Ozone implementation for the country of Gruzinia might use "Gruzinia" as the distribution name.
* **groupId:** This is the [Maven groupId](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia", this might be: `gz.moh`.
* **artifactId:** This is the [Maven artifactId](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia", this might be: `ozone-grunzia`.
* **package:** This is a required property, but not used. Just accept the default value, which should be the same as the **groupId**.
* **version:** This is the version number for the distribution, which defaults to `1.0.0-SNAPSHOT`.

This will create a bare-bones Ozone implementation project, which should look like this:

```
<project root>
  |
  |--configs
  |    |
  |    |--openmrs
  |    |    |
  |    |    |--frontend_config
  |    |    |--initializer_config
  |--readme
  |    |--impl-guide.md
  |--scripts
  |--.gitignore
  |--.gitpod.yml
  |--pom.xml
  |--README.md
```

From this point on, your can run your new Ozone distribution with the following commands:

## Build & Run
```bash
./scripts/mvnw clean package
```

```bash
source target/go-to-scripts-dir.sh
./start-demo.sh
```

## (optional) Stop & Destroy
```bash
./stop-demo.sh
```

```bash
./destroy-demo.sh
```

Next is to customize Ozone to your needs. Check out to next page to override inherited configurations.
