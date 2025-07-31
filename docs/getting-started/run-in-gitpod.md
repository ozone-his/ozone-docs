Just one click:

[![](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ozone-his/ozone/)

!!! warning ""

    :fontawesome-regular-hourglass-half: It may take some time to download and setup Ozone for the first time.

Gitpod will automatically launch a new browser tab for OpenMRS 3.

You can navigate to other Ozone apps of the HIS via the `PORTS` tab of the Terminal panel in the Gitpod editor:

![Ozone services started](../assets/images/gitpod-list-services.png)

In Gitpod each app of the HIS will require you to log in separately with their own credentials:

| **HIS App**                                  | **Username**                                             | **Password**                                        |
|----------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------|
| OpenMRS 3                                          | admin                                                    | Admin123                                            |
| Odoo                                               | admin                                                    | admin                                               |
| Superset                                           | admin                                                    | password                                            |
| SENAITE                                            | admin                                                    | password                                            |
| Orthanc                                            | orthanc                                                  | orthanc                                             |
| <span class='secondary'>ERPNext</span> | <span class='secondary'>administrator</span> | <span class='secondary'>password</span> |

!!! info ""

    💡 Single Sign-On isn’t supported in Gitpod. To try it out, check the [offical demo](online-demo.md) or [run Ozone locally](run-locally.md)