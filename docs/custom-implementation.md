# Custom Implementation

!!! tip

    Install Git, Maven and Docker Compose

HIS systems, like Ozone, often need to be heavily customized based on local needs. Ozone facilitates implementer's providing custom implementation configurations via a series of tools built on Apache Maven. The starting-point for a custom implementation is the Ozone Maven Archetype which creates a skeleton project that serves as a base for any particular customizations an implementation needs.

## Getting Started

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
  |--config
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

To start working with your project, follow the steps in the `readme/impl-guide.md` file.
