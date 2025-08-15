# Branding & White-labelling

## While-labelling Odoo

Odoo allows developers to extend and modify both its functionality and user interface using add-ons. In this guide, we will document how to use the [OCA `web_company_color`](https://github.com/OCA/web/tree/17.0/web_company_color) add-on to apply a custom theme to your Odoo instance.

As an example, we've used this add-on to apply the OpenMRS theme colors across the Odoo 17 UI to provide a users with a more unified experience between Ozone applications.

### What Does the Add-on Do?

The add-on applies theme colors to Odoo elements like:

- Navigation bar
- Buttons
- Links
- Menus
- Forms and status bars

It works by:

1. Defining a SCSS (CSS with variables) template containing all the UI elements.
2. Replacing variables like `%(color_navbar_bg)s` with actual color values.
3. Generating the final SCSS code that is applied to the Odoo frontend.

### SCSS Template

Here's a snippet of the SCSS template used to apply custom colors:

```python
SCSS_TEMPLATE = """
.o_main_navbar {
    background: %(color_navbar_bg)s !important;
    color: %(color_navbar_text)s !important;
    ...
}

.btn-primary:not(.disabled) {
    background-color: %(color_button_bg)s !important;
    color: %(color_button_text)s !important;
}
...
"""
```

These variables (`%(color_navbar_bg)s`, `%(color_button_bg)s`, etc.) are replaced with values using the `_scss_get_sanitized_values` method.

### Setting the Color Values

The color values are provided in Python as a dictionary. This method overrides the default color settings:

```python
def _scss_get_sanitized_values(self):
    self.ensure_one()
    values = dict(self.company_colors or {})
    values.update(
        {
            "color_navbar_bg": "#005d5d",
            "color_navbar_bg_hover": "#007070",
            "color_navbar_text": "#ffffff",
            "color_button_bg": "#005d5d",
            "color_button_bg_hover": "#007070",
            "color_button_text": "#ffffff",
            "color_link_text": "#005d5d",
            "color_link_text_hover": "#007070",
            "color_submenu_text": "#ffffff",
            "color_menu_brand": "#ffffff"
        }
    )
    return values
```

### How to Modify the Theme Colors

Let's say you want to change the navbar background color to dark blue and button background color to green.

- Locate the `res.company.py` file where the SCSS code is defined.

- Update the color values in `_scss_get_sanitized_values` method:

   ```python
   values.update(
       {
           "color_navbar_bg": "#001f3f",  # Dark blue
           "color_navbar_bg_hover": "#003366",
           "color_navbar_text": "#ffffff",
           "color_button_bg": "#28a745",  # Green
           "color_button_bg_hover": "#218838",
           "color_button_text": "#ffffff",
           "color_link_text": "#001f3f",
           "color_link_text_hover": "#003366",
           "color_submenu_text": "#ffffff",
           "color_menu_brand": "#ffffff"
       }
   )
   ```

- Restart Odoo to regenerate the SCSS and apply the new theme.

- Clear cache or do a hard reload to see the updated theme.

### Notes

- More SCSS variables and styles can be added by editing the `SCSS_TEMPLATE`.
- Manually verify your CSS/SCSS syntax because your IDE might not show the errors as the code is in Python and not HTML/CSS
- Use `!important` carefully to avoid style conflicts.


## While-labelling Keycloak

Keycloak allows you to fully customize its look, feel, and behavior by modifying its themes. Themes control how pages like login, account management, and email templates appear to users.

### Types of Keycloak Theme Pages

Keycloak has different pages and templates which can be customized:

- *Login Pages*
- *Account Pages*
- *Admin Console Pages*
- *Email templates*

!!! tip "Recommendation"

      Keycloak supports **theme inheritance**, which means you can extend an existing theme and override only the parts you need. Unless you plan to replace every single page, you should extend another theme instead of starting from scratch.

### Customization Methods

There are several ways to customize themes in Keycloak. The two most recommended methods are:

#### - Freemarker Templates (.ftl files)

**Technology**: Uses [Apache FreeMarker](https://freemarker.apache.org/)    
**Use Case**: Good for small customizations or branding changes  
**Used In**: 
- [Ozone Distro](https://github.com/ozone-his/ozone/tree/main/distro/configs/keycloak/themes/carbon/login) - A custom login screen for Ozone, implemented using FTL templates and custom CSS.
- [OpenMRS Distro HIS](https://github.com/openmrs/openmrs-distro-his/tree/main/configs/keycloak/themes/carbon/login) - Customized login screen for OpenMRS Distro HIS

**How to use**:
- Follow the official Keycloak documentation on [creating a theme](https://www.keycloak.org/docs/latest/server_development/index.html#creating-a-theme).
- Once your theme directory (e.g., `myCustomTheme`) is ready, place it inside the `configs/keycloak/themes` folder in your distribution.
- The Maven build process will automatically detect the theme and load it into Keycloak.
- After the Ozone distribution is up and running:
    - Log in to Keycloak.
    - Navigate to the Themes section.
    - Select your custom theme.
    - Restart the Keycloak container if required.
- To make this your **default** theme:
    - Duplicate the realm configuration file in your distribution.
    - Place the copy inside the `configs/keycloak/realms` folder.
- In the copied file, update the Keycloak theme name at [this location](https://www.keycloak.org/docs/latest/server_development/index.html#creating-a-theme).


#### - Keycloakify

**Technology**: React-based theme builder [Keycloakify](https://www.keycloakify.dev/)  
**Use Case**: Ideal for complex UI changes and building modern UIs  
**Used In**: 
- Ozone FAIMER Project - Used to fully customize login, reset password, and email verification pages.

**How to use**:
- Follow the Keycloakify documentation on [theme types](https://docs.keycloakify.dev/theme-types/difference-between-login-themes-and-the-other-types-of-themes).
- Make the desired cosmetic changes to your theme.
- [Build your theme JAR](https://docs.keycloakify.dev/deploying-your-theme#building-the-jar-file).
- You now have two deployment options:
    - **Mavenize the Keycloakify project** and publish the JAR to a central repository so it can be pulled into your distribution automatically.
    - **Manually deploy** by building the JAR locally and copying it into the distribution every time you make a theme change.
- In either case, ensure the following:
    - The final theme JAR is located in `distro/binaries/keycloak/themes`.
    - If manually copying, place the JAR directly inside `binaries/keycloak/themes` in your distribution.
- To make this your **default** theme:
    - Duplicate the realm configuration file in your distribution.
    - Place the copy inside `configs/keycloak/realms`.


### Additional Notes

!!! warning "Important Considerations"

      - Always test your theme against compatible Keycloak version
      - Keycloakify themes are compiled using a Node.js build toolchain
      - FTL themes are simpler to implement but offer less flexibility compared to React-based solutions

