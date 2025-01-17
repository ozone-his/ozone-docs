import mkdocs_gen_files
import requests
import os

# GitHub raw URL for application.properties
GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-odoo-openmrs/01da79a5f6c5a250b2f7800d1c78a516f4c4c0a5/odoo-openmrs/src/main/resources/config/application.properties"

def process_mkdocs_input(input_string):
    # Split input string by lines
    lines = input_string.split('\n')

    # Create a list to store the processed lines
    result_lines = []

    for line in lines:
        # Check if line starts with # /mkdocs
        if line.strip().startswith('# /mkdocs'):
            # Replace '# /mkdocs' with the new format
            line = line.replace('# /mkdocs-start', '----------------------------------\n')\
                       .replace('# /mkdocs-config-enabled:', '**Enabled:** ')\
                       .replace('# /mkdocs-config-name:', '**Name:** ')\
                       .replace('# /mkdocs-config-description:', '**Description:** ')\
                       .replace('# /mkdocs-config-location:', '**Location:** ')\
                       .replace('# /mkdocs-config-possible-values:', '**Possible Values:** ')\
                       .replace('# /mkdocs-config-default-value:', '**Default Value:** ')\
                       .replace('# /mkdocs-end', '----------------------------------\n')\
            # Append to the result list
            result_lines.append('\n'+line)

    return '\n'.join(result_lines)

try:
    response = requests.get(GITHUB_URL)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    with mkdocs_gen_files.open("auto-eip-config-points.md", "w") as f:
        print(process_mkdocs_input(response.text), file=f)
except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")