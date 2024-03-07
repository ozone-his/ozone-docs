# Create Your Own Distribution of Ozone HIS

## Why your own distribution?

Beyond experimenting with the Quick Start guide, implementers and integrators of Ozone HIS will soon discover the need to provide their own configurations and possibly bespoke customizations to Ozone HIS. We recommend to do so through creating and managing your own distribution of Ozone HIS.

Ozone provides a series Apache Maven-based tools to facilitate the assembly of your own tailored HIS distribution. This starts with the _Ozone Maven Archetype_.

## The Ozone Maven Archetype

!!! tip "Prequisites"

    Install [Git](https://github.com/git-guides/install-git), [Maven](https://www.baeldung.com/install-maven-on-windows-linux-mac) and [Docker Compose](https://docs.docker.com/compose/install/)

The Ozone Maven Archetype generates a foundational skeleton project, providing a customizable base for any specific implementation requirements.

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
mvn org.apache.maven.plugins:maven-archetype-plugin:3.2.1:generate -DarchetypeArtifactId=maven-archetype -DarchetypeGroupId=com.ozonehis 
```

This will prompt you for several key variables for your Maven project:

| Prompt variable    | Sample value     | Explanation                                                                                                                                                                                             |
|--------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `distributionName` | `Ozone Gruzinia` | A name for your distribution. For example, a reference Ozone implementation for the imaginary country of Gruzinia could be named "Ozone Gruzinia".                                                      |
| `groupId`          | `gz.moh`         | The [Maven group ID](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia" this might be something like `gz.moh`. |
| `artifactId`       | `ozone-gruzinia` | The [Maven artifact ID](https://maven.apache.org/guides/mini/guide-naming-conventions.html) that will be used for the implementation artifact. For "Ozone Gruzinia" this might be `ozone-gruzinia`.     |
| `package`          | `gz.moh`         | A required property, but not used. To make it easy just accept the default value, which should default to be the same as the `groupId`.                                                                 |
| `version`          | `1.0.0-SNAPSHOT` | The version number for the distribution, it starts by default at `1.0.0-SNAPSHOT`.                                                                                                                      |


This will create a bare-bones Ozone implementation project that should look like this:
```bash
ozone-gruzinia/
├── README.md
├── config
│     └── openmrs
│         ├── frontend_config
│         └── initializer_config
├── pom.xml
├── readme
│     └── impl-guide.md
└── scripts
    ├── mvnw
    ├── mvnw.cmd
    ├── mvnwDebug
    └── mvnwDebug.cmd
```

## Available commands

|Goal|Command|Explanation|
|:----|:----|:----|
|**Build** the distribution|<pre>./scripts/mvnw clean package</pre>|Assembles and packages your distribution, incorporating any configurations and customizations you've applied.|
|Access start/stop/destroy commands|<pre>source target/go-to-scripts-dir.sh</pre>|Navigates to the directory containing the scripts for starting, stopping, and destroying the distribution, making these commands readily accessible.|
|**Start** the distribution|<pre>./start-demo.sh</pre>|Initiates and launches all components of the Ozone HIS, bringing up the system.|
|**Stop** the distribution|<pre>./stop-demo.sh</pre>|Gracefully halts all Ozone HIS services, effectively shutting down the system.|
|**Destroy** the distribution|<pre>./destroy-demo.sh</pre>|Completely removes the distribution, clearing all its components and data, ideal for resetting the system or rectifying persistent issues ahead of a restart or a rebuild and restart.|

You are now ready to tailor Ozone to fit your specific requirements. Proceed to the following page for guidance on how to override default configurations.
