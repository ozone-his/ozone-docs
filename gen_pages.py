import mkdocs_gen_files
import requests
import os

# GitHub raw URL for application.properties
GITHUB_URL = "https://raw.githubusercontent.com/ozone-his/eip-odoo-openmrs/main/odoo-openmrs/src/main/resources/config/application.properties"

def process_string(input_string):
    lines = input_string.splitlines()

    show_lines = False  # Flag to start showing lines after finding the target text
    target_text = "OpenMRS FHIR EIP Configuration"
    result_lines = []

    for line in lines:
        stripped_line = line.strip()

        # Check for the target text
        if target_text in stripped_line:
            show_lines = True

        # Skip lines that start with '#'
        if stripped_line.startswith('#'):
            continue

        # Start collecting lines after finding the target text
        if show_lines:
            result_lines.append(line)

        # Stop collecting lines after the first '---------' following the target text
        if show_lines and stripped_line == '---------':
            break

    # Output the result
    return '\n'.join(result_lines)

try:
    response = requests.get(GITHUB_URL)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    with mkdocs_gen_files.open("foo.md", "w") as f:
        print(process_string(response.text), file=f)
except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")