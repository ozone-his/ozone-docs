# E2E Tests

## Introduction
    E2E testing is a critical aspect of Ozone HIS that ensures all the workflows work as expected.

## Prerequisites
    Before running Ozone E2E tests, ensure you have Node.js and npm installed on your machine.

## Setup Instructions
    Clone Ozone E2E repository: git clone https://github.com/ozone-his/ozone-e2e.
    Navigate to the project directory: cd ozone-e2e.
    Install dependencies: yarn install.

## Test Case Documentation
    Test Scenario: Patient with drug order becomes customer in Odoo.
    Steps:
        Login to O3, create a patient and start a visit.
        Make a drug order.
        Navigate to Odoo using Single Sign-On (SSO).
    Expected Outcome: Patient is synced as a customer in Odoo.

## Test Suite Structure
    Test suite is organized into folders based on functionality.
    ```
    e2e
    |__ tests
    |   ^ Contains test cases.
    |__ utils
    |   ^ Contains utilities needed to set up and tear down tests,
    |     as well as methods required by the tests to run.
    ```

## Configuration Options
    Environment Settings: Use `.env` file to configure test environment (e.g., E2E_BASE_URL).
    Browser Selection: Use the `--browser` flag to specify the browser (e.g., chrome, firefox).

## Running Tests
    Run all tests: npm playwright tests.
    Run tests in a specific file: npm playwright test <file name>.
    Run tests with custom configuration: npm playwright test --project=<browser name>.

## Interpreting Test Results
    Passed: All tests passed without any errors.
    Failed: One or more tests have failed during test execution.
    Skipped: Test was skipped due to a conditional directive or configuration.

## Writing New Test Scripts
    Create test.spec.js file in `e2e/test`` folder.
    Write test scenarios using Playwright's API.
    Use Playwright's API to interact with the browser, navigate to pages, interact with elements, perform actions, and make assertions.

## Best Practices
    Write clear and descriptive test cases.
    Use page objects to encapsulate page-specific logic and interactions for better maintainability.

## References and Resources
    Playwright Testing Framework: https://playwright.dev
    Ozone Community Forum: https://talk.openmrs.org/c/software/ozone-his
