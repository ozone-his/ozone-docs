import mkdocs_gen_files
import requests
import os
import re

# GitHub raw URL for application.properties
ODOO_OPENMRS_GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-odoo-openmrs/7773cdb2783c2b7a5310e49ec79e979a65f2c1e0/odoo-openmrs/src/main/resources/config/application.properties"
OPENMRS_ORTHANC_GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-openmrs-orthanc/45b2c6361da5afcb0bf281229f484e8bec7ae0f2/openmrs-orthanc/src/main/resources/config/application.properties"
KEYCLOCK_SUPERSET_GITHUB_URL = ""
OPENMRS_SENAITE_GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-openmrs-senaite/7184244ee52db4df85efab9fed9c63a2d993cbe1/senaite-openmrs/src/main/resources/config/application.properties"
ERPNEXT_OPENMRS_GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-erpnext-openmrs/789020a15dbbb10f0bd5b2c994a1de2e82cf7ae7/erpnext-openmrs/src/main/resources/config/application.properties"

mkdocs_config_points = {'mkdocs-config-name': 'Name', 'mkdocs-config-description': 'Description',
                        'mkdocs-config-location': 'Location', 'mkdocs-config-possible-values': 'Possible Values',
                        'mkdocs-config-default-value': 'Default Value'}

mkdocs_block_end_identifier = '# /mkdocs-end'

app_github_dict = {'Odoo-OpenMRS Flows': ODOO_OPENMRS_GITHUB_URL, 'OpenMRS-SENAITE Flows': OPENMRS_SENAITE_GITHUB_URL,
                   'ERPNext-OpenMRS Flows': ERPNEXT_OPENMRS_GITHUB_URL,'OpenMRS-Orthanc Flows': OPENMRS_ORTHANC_GITHUB_URL}


def mk_example(example_heading, example_text):
    component = '!!! example "' + example_heading + '" \n\n' + '    ```java\n    ' + example_text + '\n    ```'
    return component


mkdocs_components = {'mkdocs_component-mk-example': mk_example}


def process_application_properties(text):
    # Split input string by lines
    lines = text.split('\n')
    result_lines = []

    for line in lines:
        if mkdocs_block_end_identifier in line.strip():
            line = line.replace(mkdocs_block_end_identifier, mk_seperator_line())
            result_lines.append('\n' + line)
        if 'mkdocs' in line.strip():
            for key, value in mkdocs_config_points.items():
                line = line.replace('# /' + key + ':', mk_bold(value + ': '))
            if 'mkdocs_component' in line:
                for key, value in mkdocs_components.items():
                    line = line.replace(line, populate_mk_docs_components(value, line))
            result_lines.append('\n' + line)

    return '\n'.join(result_lines)


def main():
    result_lines = []
    result_lines.append(page_heading(mk_emoji_construction() + ' EIP Configuration Points'))
    result_lines.append(mk_newline())
    result_lines.append(
        'In this section, we provide a comprehensive list of configuration points available in Ozone, organized by EIP services and thereby grouped by pairs of apps.')
    result_lines.append(mk_newline())
    result_lines.append(mk_seperator_line())
    for key, value in app_github_dict.items():
        result_lines.append(mk_title(key))
        result_lines.append(process_application_properties(get_application_properties(value)))
    generate_file(result_lines, "auto-eip-config-points.md")


def get_application_properties(url):
    response = requests.get(url)
    return response.text


def generate_file(lines, filename):
    with mkdocs_gen_files.open(filename, "w") as f:
        print(''.join(lines), file=f)


def populate_mk_docs_components(func, text):
    print('kajsfdkhadsf ' + text)
    values = re.findall(r"mk-arg\d+=(.*?)(?=\s*mk-arg\d+=|$)", text)  # Looks for mk-arg1, mk-arg2 etc
    print(f"Expected at least 2 arguments for {func.__name__}, but got {len(values)}: {values}")
    return func(*values)


def page_heading(heading):
    return '# ' + heading


def mk_emoji_construction():
    return '<small>:construction:</small>'


def mk_title(text):
    return '## ' + text + '\n'


def mk_heading(text):
    return '# ' + text + '\n'


def mk_ozone_pro_tag():
    component = '!!! info inline end ""\n' + '\n    {==:oz: Pro==}\n'
    return component


def mk_syntax_highlight(text):
    return '`' + text + '`'


def mk_bold(text):
    return '**' + text + '**'


def mk_italics(text):
    return '_' + text + '_'


def mk_bullet_check(text):
    component = '    * [x] `' + text + '`'
    return component


def mk_bullet_uncheck(text):
    component = '    * [] `' + text + '`'
    return component


def mk_seperator_line():
    return '\n----------------------------------\n'


def mk_newline():
    return '\n'


main()
