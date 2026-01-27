# Authentication and Authorisation

!!! question "What is Single Sign-On (SSO)?"
    Single Sign-On (SSO) allows users to authenticate once and access multiple applications without re-entering credentials. This improves user experience and enhances security by reducing the number of passwords users need to remember.

### Overview

Ozone manages authentication and authorization across its ecosystem using Keycloak as the central identity provider. Keycloak enables unified user management, role assignment, and access control for all integrated applications, ensuring consistent security and user experience. Depending on deployment needs, authentication and authorization can be handled centrally through Keycloak or individually by each application.

When SSO and/or Central Auth are enabled, all the requests to the Ozone ecosystem are authenticated and authorized using Keycloak. Otherwise, each application maintains its own user accounts and roles. Most features are available in both Ozone Pro and Ozone FOSS, except for the role synchronization, which is exclusive to Ozone {==:oz: Pro==}.

### Single Sign-On Protocols

SSO protocols enable secure authentication and authorization across multiple applications using a centralized identity provider. Common SSO protocols include OpenID Connect (OIDC), Security Assertion Markup Language (SAML), and OAuth 2.0. Within Ozone, OIDC is the most widely used protocol, providing seamless integration with Keycloak for user authentication and single sign-on across the ecosystem. OIDC offers a modern, secure, and flexible approach, making it the preferred choice for most Ozone deployments.

### User Management

Ozone supports user management through the Keycloak admin console. Users can be created, updated, and deleted through the admin console. Additionally, users can be assigned roles and permissions to control their access to various applications within the Ozone ecosystem. Users can also be imported from external sources, such as LDAP or Active Directory, to streamline user management. User federations are also supported, allowing users to log in using their existing identities. Users can also self-register through the Keycloak login page if enabled. Users are created in Keycloak and synced to the target application upon login.


### Role Synchronization

Roles from each integrated application are synchronized to Keycloak. This ensures that roles are available in Keycloak for assignment to users. Role synchronization is a one-way process from the applications to Keycloak. When a role is created, updated, or deleted in an application, the changes are reflected in Keycloak. 

!!! info "Note"
    The source of truth for roles is the respective application, not Keycloak. Therefore, any role changes must be made in the application itself.

### Role Assignations

Roles are assigned to users within Keycloak. When a user logs in, their roles are propagated to the target application,
which applies the appropriate permissions and access controls based on these roles. In addition, the user's role changes in Keycloak, i.e., when a user is assigned a new role, the changes are reflected in the target application upon the next login.

!!! warning "Limitations"
    - Central Auth is only available in Ozone {==:oz: Pro==}.
    - Role synchronization is not available for SENAITE yet. This will be available in future releases.
