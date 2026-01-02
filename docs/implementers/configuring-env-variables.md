# Configuring Environment Variables

## Environment Variable Overrides in Ozone Distros

Ozone supports hierarchical overriding of environment variables for child and grandchild distros through `.env` files. This allows each distro to customize configuration while still inheriting defaults from its parent.

---

## Overriding Environment Variables for a Child Distro

To override environment variables for a **child distro of Ozone**:

1. Create a file named `<any_name>.env` inside the `scripts/` directory of the distro.
2. Rebuild the distro.

After the build completes, Ozone generates a final `concatenated.env` file in the build (target) folder. This file contains all environment variables merged together, including those defined in your custom `.env` file.

If the same variable is defined in multiple `.env` files, the value from the file applied **later** takes precedence.

---

## Environment Variable Precedence for Grandchild Distros

If your setup includes a **grandchild distro**, the **order in which `.env` files are concatenated is important**.

The concatenation order is determined by **lexicographical (dictionary) order of the filenames**.

To ensure correct precedence, the naming should follow this order:

1. Default Ozone `.env` file
2. Parent distro `.env` file
3. Grandchild distro `.env` file


This ensures that:
- Grandchild distro variables override defaults when required
- The final (grandchild) distro variables override both parent and base Ozone variables

---

## Naming Convention Example

Assume the following hierarchy:

- **Ozone** (base)
  - **Ozone-Haiti** (child)
    - **Ozone-HSC** (grandchild)

Recommended `.env` filenames:

| Distro        | `.env` Filename |
|--------------|-----------------|
| Ozone-HSC    | `distro-a.env`  |
| Ozone-Haiti  | `distro-b.env`  |
| Ozone (base) | `.env`          |

Because `distro-a.env` comes before `distro-b.env` alphabetically, the variables are applied in the correct order, ensuring that the most specific (grandchild) distro configuration is applied last and hence the ones to be finally applied.

---

## Example `.env` File Format

Syntax:
```env
<VARIABLE_NAME>=<value>
```

Example
```env
SPA_CONFIG_URLS=/openmrs/spa/configs/ozone-frontend-config.json,/openmrs/spa/configs/ozone-haiti-frontend-config.json
```
- Each line represents a single environment variable.
- Variables defined later in the concatenation process override earlier definitions with the same name.
