# <small>:construction:</small> Conventions

!!! info "Coming soon:"

    * Listing our conventions, organized by the type and grouped by app/service.
    * Code Conventions.

## Naming

### EIP Service

- Should be named in the format `eip-<a>-<b>`. Where `<a>` and `<b>` are the names of the two systems being integrated, in alphabetical order. For example, `eip-erpnext-openmrs`.
- The name should be in lowercase and use hyphens to separate words.
- The preceding name should be used for (whenever possible):
    - GitHub repository name.
    - Docker Compose service.
    - Configuration directory.
    - Configuration properties file.
    - Maven artifact ID.

## Code Conventions

### Java