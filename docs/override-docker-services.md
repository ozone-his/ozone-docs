## Overriding configs in a custom Ozone distribution

- Creat a custom Ozone distribution following [this](https://docs.ozone-his.com/create-distro/) guide.
- Add the custom docker compose override configurations and make sure they're copied to the right directory.
- Add the build step in the `pom.xml`file for the custom configs:

```
    <execution>
      <!-- Copy over the Docker Compose override file -->
        <id>Copy docker-compose-override.yml</id>
        <phase>process-resources</phase>
        <goals>
          <goal>copy-resources</goal>
        </goals>
        <configuration>
          <outputDirectory>
            ${project.build.directory}/${project.artifactId}-${project.version}/run/docker/
          </outputDirectory>
          <overwrite>true</overwrite>
          <resources>
            <resource>
              <directory>${project.basedir}/scripts</directory>
              <includes>
                <include>docker-compose-override.yml</include>
              </includes>
              <filtering>true</filtering>
            </resource>
          </resources>
        </configuration>
      </execution>
```

- Build the project by running `./scripts/mvnw clean package`
- Start the Ozone services by running: 
```
source target/go-to-scripts-dir.sh
./start-demo.sh
```

## Disabling components in Ozone distribution

Ozone distribution comes with O3, Odoo, Senaite and Superset as the default components. If you may want to disable any of them, here are the steps to follow:

 - Start Ozone using [quick start](https://docs.ozone-his.com/) guide.

 - Stop the service by running `destroy-demo.sh`. In the scripts directory `target/ozone/run/docker/scripts/`, remove the manifest in `docker-compose-files.txt` for the component you want to disable. For example if you want to disable SENAITE component, remove `docker-compose-senaite.yml`.
 - Restart Ozone by running `./start-demo.sh`.

## Swap Odoo integration with ERPNext

 Ozone distribution comes with Odoo as the default ERP component. You can swap Odoo with ERPNext component using the following the steps:

  - After starting Ozone, go to the scripts directory `target/ozone/run/docker/scripts/` and replace the manifest for Odoo with that of ERPNext component, i.e., `docker-compose-erpnext.yml` in the `docker-compose-files.txt` file.
  - Restart Ozone by running `./start-demo.sh`.

!!! info "Coming soon:"

    * Using the Ozone Maven Archetype.
    * Using the Maven parent.
