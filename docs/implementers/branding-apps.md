# Branding Applications

## Customise Odoo Theme Color Using Add-On

### Overview

Odoo allows developers to extend and modify both its **functionality** and **user interface (UI)** using **add-ons**. In this guide, we will document how to use the [OCA `web_company_color`](https://github.com/OCA/web/tree/17.0/web_company_color) add-on to apply a custom theme to your Odoo instance.

We've used this add-on to apply **OpenMRS theme colors** across the Odoo 17 UI.

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

Let's say you want to change the **navbar background color** to dark blue and **button background color** to green.

- **Locate the Add-on Code**
   The logic is inside `res.company.py` model.

- **Modify the Color Dictionary**
   Update the color values in `_scss_get_sanitized_values`:

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

- **Restart the Odoo Server**
   Restart Odoo to regenerate the SCSS and apply the new theme.

- **Clear Browser Cache**
   Clear cache or do a hard reload to see the updated theme.

### Notes

- More SCSS variables and styles can be added by editing the `SCSS_TEMPLATE`.
- Validate CSS/SCSS syntax.
- Use `!important` carefully to avoid style conflicts.
