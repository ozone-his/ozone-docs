# <small>:construction:</small> Configuring HIS Components

You will find a `configs` folder within the skeleton project generated by the Ozone Maven Archetype. This folder is subdivided into subfolders, with each subfolder corresponding to a component of the Ozone HIS distribution. It should look something like this depending on the components available:

```bash
 configs/
    ├── erpnext
    ├── odoo
    ├── openmrs
    ├── senaite
    └── superset
```

Each component-specific subfolder can be used to provide the configuration files for that component, overriding its default configuration.

!!! warning ""

    Each component's default configuration is the responsibility of the component's open-source community.

    Ozone HIS provides these configurations "as is", they are not modified or maintained by the Ozone development team.

## Overriding the ERPNext Config

## Overriding the Odoo Config

## Overriding the OpenMRS Config

To assist implementers, the OpenMRS config is already structured with multiple subfolders that gather in one place all the essential configurations of OpenMRS 3:
```bash
   ├── openmrs
         ├── frontend_assembly
         ├── frontend_config
         └── initializer_config
```

### `frontend_assembly`

### `frontend_config`

### `initializer_config`

## Overriding the SENAITE Config

## Overriding the Superset Config