# Create Your Own Distribution of Ozone HIS

## Why your own distribution?

Beyond experimenting with the Quick Start guide, implementers of Ozone HIS will soon discover the need to provide their own configurations and possibly bespoke customizations to Ozone HIS. We recommend to do so through creating and managing your own distribution of Ozone HIS.

Adopting a distribution architecture for Ozone offers several compelling advantages:

### Enhanced Packaging and Configuration Management

By creating your own distribution (e.g., using Maven Archetype), you inherit Ozone's robust packaging concepts. This approach enables proper versioning of configurations, facilitating controlled and agile deployments.

### Flexible Inheritance Structure

A distribution architecture allows for a multi-layered structure, enabling hierarchical configuration management. For instance, you can:

- Establish country-level configurations
- Inherit and customize these at the program level
- Further refine settings for specific facilities

### Seamless Upgradability

By utilizing the distribution mechanism, you incorporate the main Ozone as a dependency, building upon it rather than forking the codebase. This approach mitigates the risk of isolation and ensures easier upgrades.

### Simplified Adoption and Focus

Ozone handles complex build logic and base configurations, allowing you to concentrate on adapting the system to your specific requirements. This approach significantly reduces the learning curve and implementation time.

### Enhanced Collaboration and Community Impact

By leveraging the upstream Ozone development, all users benefit from community-driven improvements. This collaborative model makes it easier for individuals and organizations to contribute meaningfully to the Ozone ecosystem.



## Create your own "child" distribution

Ozone provides a series Apache Maven-based tools to facilitate the assembly of your own tailored HIS distribution. This starts with the _Ozone Maven Archetype_.


### The Ozone Maven Archetype


The Ozone Maven Archetype generates a foundational skeleton project, providing a customizable base for any specific implementation requirements.

!!! tip "Software Prequisites"

    - [:simple-apachemaven: Maven <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://www.baeldung.com/install-maven-on-windows-linux-mac)
    - [:simple-docker: Docker Compose <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://docs.docker.com/compose/install/)

### 1) Configure Maven

Edit your Maven `settings.xml` file (usually located at `~/.m2/settings.xml`) and add the following block to it:
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

### 2) Generate the archetype

Use Maven's archetype tools to generate a new Ozone implementation project structure:

```bash
mvn org.apache.maven.plugins:maven-archetype-plugin:3.2.1:generate \
      -DarchetypeArtifactId=maven-archetype \
      -DarchetypeGroupId=com.ozonehis 
```

This will prompt you for several key variables for your Maven project:

| Prompt variable    | Sample value     | Explanation                                                                                                                                                                                             |
|--------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `distributionName` | `Ozone Gruzinia` | A name for your distribution. For example, a reference Ozone implementation for the imaginary country of Gruzinia could be named "Ozone Gruzinia".                                                      |
| `groupId`          | `gz.moh`         | The [Maven group ID <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia" this might be something like `gz.moh`. |
| `artifactId`       | `ozone-gruzinia` | The [Maven artifact ID <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia" this might be `ozone-gruzinia`.     |
| `package`          | `gz.moh`         | A required property, but not used. To make it easy just accept the default value, which should default to be the same as the `groupId`.                                                                 |
| `version`          | `1.0.0-SNAPSHOT` | The version number for the distribution, it starts by default at `1.0.0-SNAPSHOT`.                                                                                                                      |


This will create a bare-bones Ozone implementation project that should look like this:
```bash
ozone-gruzinia/
├── README.md
├── assembly.xml
├── configs
│   └── openmrs
│       ├── frontend_config
│       └── initializer_config
└── pom.xml

```

Congratulations :clap:, you have created your child distribution of Ozone. Note that it does not configure or override anything. It is, at the moment, only plain Ozone.
Check out our next section to configure your distribution:

- [Configure Apps](./configure-apps.md) - White labeling, metadata configuration...
- [Configure Integrations](./configure-integrations.md) - Configure integration points, enable/disable integration routes...
- [Enable & Disable Apps Integrations](./enabling-apps.md) - Define which app or integration should be run.

Or if you want to try your distribution as such, jump right to [Start & Stop](./start-stop.md) page.
