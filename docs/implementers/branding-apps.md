# Branding & White-labelling

## White-labelling Odoo

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


## White-labelling Keycloak

Keycloak controls how several pages look and behave, like the login page, the account page, admin console, and email templates. You can change all of these by using Keycloak themes.

### Types of Keycloak theme pages

Keycloak has different pages and templates you can customize:

- *Login pages*
- *Account pages*
- *Admin console pages*
- *Email templates*

!!! tip "Always extend, don't start from scratch"

    Keycloak supports **theme inheritance**. A theme can set a `parent`, and it automatically gets everything from that parent theme. You only need to add the small bits you actually want to change. Unless you plan to replace every single page, extend an existing theme instead of building a new one from scratch.

### Ozone's built-in login theme

Ozone ships its own login theme, called `ozone`, at [`distro/configs/keycloak/themes/ozone`](https://github.com/ozone-his/ozone/tree/main/distro/configs/keycloak/themes/ozone). It only changes branding: colors, the logo, the font, and the "powered by" logos row. Everything else, like page layout, forms, and error pages, comes straight from Keycloak's own built-in `keycloak.v2` theme, so it keeps working when Keycloak is upgraded.

Every Ozone child distribution already uses this theme by default. In most cases, you don't need to build a Keycloak theme at all. Your own theme just needs a `theme.properties` file that says:

```properties
parent=ozone
```

This means your theme automatically gets everything from `ozone` (colors, logo, font, powered by logos, all its layout fixes) unless you override it. To customize something, add only the file or property for that one thing. Everything you don't touch keeps coming from `ozone`.

#### Change the brand color and logo

Add your own `login/resources/css/branding.css` file, and update your theme's `theme.properties` to include it:

```properties
styles=css/styles.css vendor/patternfly-v5/patternfly.min.css vendor/patternfly-v5/patternfly-addons.css css/branding.css
```

```css
/* login/resources/css/branding.css */
:root {
  --pf-v5-global--primary-color--100: #YOUR-COLOR;
  --keycloak-card-top-color: #YOUR-COLOR;
  --keycloak-logo-url: url("../img/logo.png");
}

.pf-v5-c-button {
  --pf-v5-c-button--m-primary--BackgroundColor: #YOUR-COLOR;
}
```

Then put your own `logo.png` in `login/resources/img/`.

Keycloak doesn't merge the `styles` list across parent themes, so you need to repeat the full list and add your own CSS file at the end. Putting it last means your colors win over the ones already set in `ozone`.

#### Change the "powered by" logos

This one is the easiest. You don't need any CSS or template file at all. Just add this line to your theme's `theme.properties`:

```properties
poweredByLogos=your-logo.png:An Organization, another-logo.svg:Another App
```

Each logo is written as `filename:Alt Text`, separated by commas. Put the actual image files in `login/resources/img/`.

To hide the "powered by" row completely, set it to an empty value:

```properties
poweredByLogos=
```

#### Change the login page text

Add a `login/messages/messages_en.properties` file, and only include the keys you want to change, for example:

```properties
poweredBy=Brought to you by
```

Any key you don't mention still comes from the `ozone` theme, or from Keycloak itself.

!!! warning "Don't copy the theme's files"

    Don't copy `ozone`'s `footer.ftl`, `theme.properties`, or `branding.css` into your own theme and edit the copy. You will lose future fixes made to the `ozone` theme, and it defeats the point of inheriting from it. Only add the small file or property for the one thing you want to change.

### Building a theme from scratch (advanced)

If you need to change more than branding, for example the page structure or the fields on a form, you can build a full custom Keycloak theme. There are two common ways to do this.

#### Freemarker templates (.ftl files)

**Technology**: [Apache FreeMarker](https://freemarker.apache.org/)  
**Use case**: Small customizations, or full control over the page HTML  
**Used in**:

- Ozone's own [`ozone` theme](https://github.com/ozone-his/ozone/tree/main/distro/configs/keycloak/themes/ozone)
- [OpenMRS Distro HIS](https://github.com/openmrs/openmrs-distro-his/tree/main/configs/keycloak/themes/carbon/login)

**How to use it**:

1. Follow the official Keycloak documentation on [creating a theme](https://www.keycloak.org/docs/latest/server_development/index.html#creating-a-theme). Set `parent=keycloak.v2` (or `parent=ozone`, see above) so you only need to override what you actually want to change.
2. Place your theme folder inside `configs/keycloak/themes` in your distribution.
3. Rebuild your distribution. Your theme will be picked up automatically.
4. To use it, set it as the `loginTheme` in your realm file. In Ozone's own realm file, this is at [this location](https://github.com/ozone-his/ozone/blob/main/distro/configs/keycloak/realms/ozone-realm.json#L1917). If you don't want to edit the main realm file directly, copy it into your own distribution's `configs/keycloak/realms` folder and change the copy instead.

!!! tip "Alternative: set the theme from the admin console"

    Instead of editing the realm file, you can also set the theme from the Keycloak Admin Console:

    1. Log in to the Keycloak Admin Console and pick Ozone realm.
    2. Go to **Realm settings > Themes**.
    3. Choose your theme from the **Login theme** dropdown.
    4. Click **Save**.

    This is a quick way to try out a theme without rebuilding your distribution. But it only changes what is stored in Keycloak's database. If your realm file ever gets re-imported (for example on a fresh install, or in another environment), that import will not know about this change. To make your theme the real default everywhere, still set `loginTheme` in your realm file as well.

!!! warning "Avoid full page rewrites"

    Don't override a whole page template, like `template.ftl` or `login.ftl`, unless you truly need to change its structure. A full rewrite only styles the one page you wrote, so every other Keycloak page (register, forgot password, errors) can end up looking broken or inconsistent. Change only the small piece you need instead, like one CSS file, one message, or the `footer.ftl` file.

#### Keycloakify

**Technology**: React-based theme builder, [Keycloakify](https://www.keycloakify.dev/)  
**Use case**: Complex UI changes, or building a fully custom, modern UI  
**Used in**: Ozone FAIMER Project, to fully customize the login, reset password, and email verification pages.

**How to use it**:

1. Follow the Keycloakify documentation on [theme types](https://docs.keycloakify.dev/theme-types/difference-between-login-themes-and-the-other-types-of-themes).
2. Make your changes, then [build your theme JAR](https://docs.keycloakify.dev/deploying-your-theme#building-the-jar-file).
3. Add the JAR to your distribution in one of two ways:
    - **Mavenize the Keycloakify project** and publish the JAR so it gets pulled into your distribution automatically.
    - **Copy the JAR manually** into `distro/binaries/keycloak/themes` each time you make a change.
4. To use it, set it as the `loginTheme` in your realm file, the same way as described above.

### A few things to keep in mind

!!! warning "Important considerations"

    - Always test your theme against the Keycloak version you are running. Themes can break between major versions.
    - Keycloakify themes need a Node.js build step.
    - FTL themes are simpler to build, but give you less flexibility than a React based theme.
