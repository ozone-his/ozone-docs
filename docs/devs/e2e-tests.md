# End-to-End (E2E) Testing Documentation

## Introduction
E2E testing is a crucial aspect of Ozone HIS, ensuring that all system workflows function as intended.

## Prerequisites
Before running Ozone E2E tests, ensure the following are installed:
- Node.js version 18 or higher
- npm version 10 or higher

## Setup Instructions
1. Clone the Ozone E2E repository: `git clone https://github.com/ozone-his/ozone-e2e`.
2. Navigate to the project directory: `cd ozone-e2e`.
3. Install dependencies: `npm install`.

## Test Suite Structure
The test suite is organized as follows:
	```
	e2e
	├── tests
	|   ^ Contains test cases.
	└── utils
	    ^ Contains utilities needed to set up and tear down tests,
	      as well as methods required by the tests to run.
	```

## Configuration Options

- **Environment Settings**: Use the `.env` file to configure test environment variables (e.g., E2E_BASE_URL).
- **Browser Selection**: Utilize the `--browser` flag to specify the browser (e.g., chrome, firefox).

## Running Tests
- Run all tests: `npx playwright test`.
- Run tests in a specific file: `npx playwright test <file name>`.
- Run tests with custom configuration: `npx playwright test --project=<browser name>`.

## Interpreting Test Results
- **Passed**: All tests passed without any errors.
- **Failed**: One or more tests have failed during test execution.
- **Skipped**: Test was skipped due to a conditional directive or configuration.

## Developing New Test Scripts
1. Create a `test.spec.js` file in the `e2e/test` folder.
2. Write test scenarios using Playwright's API.
3. Utilize Playwright's API to interact with the browser, navigate to pages, interact with elements, perform actions, and make assertions.

## Example of a Test Script

**Test Purpose**: Verify that a patient with a lab order is synced as a client with analysis request in SENAITE.

	```javascript
	import { test, expect } from '@playwright/test';
	import { HomePage } from '../utils/functions/testBase';
	import { patientName } from '../utils/functions/testBase';
	import { E2E_BASE_URL, E2E_SENAITE_URL } from '../utils/configs/globalSetup';

	test.beforeEach(async ({ page }) => {
	  const homePage = new HomePage(page);
	  await homePage.initiateLogin();
	  await expect(page).toHaveURL(/.*home/);
	  await homePage.createPatient();
	  await homePage.startPatientVisit();
	});

	test('Patient with lab order becomes client with analysis request in SENAITE', async ({ page }) => {
	  const homePage = new HomePage(page);
	  // Set up
	  await homePage.goToLabOrderForm();
	  await page.click('button:has-text("Add")');
	  await page.selectOption('#tab select', '857AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
	  await homePage.saveLabOrder();
	  // Replay
	  await homePage.goToSENAITE();
	  await expect(page).toHaveURL(/.*senaite/);
	  // Verify
	  await homePage.searchClientInSENAITE();
	  const clientName = `${patientName.firstName} ${patientName.givenName}`;
	  const client = await page.$('table tbody tr:nth-child(1) td.contentcell.title div span a:has-text("' + clientName + '")');
	  await expect(client).toBeVisible();
	});

	test.afterEach(async ({ page }) => {
	  const homePage = new HomePage(page);
	  await homePage.deletePatient();
	  await page.close();
	});
	```

**Simplified Explanation**:

**Test Setup**: Before each test, login to O3, create a new patient, and start a visit.

**Test Case**:
- **Setup**: Navigate to the lab order form, add a new lab order, and save it.
- **Replay**: Go to the SENAITE application and search for the client.
- **Verification**: Verify that the client's name is visible in the clients list.

**Cleanup**: After each test, delete the patient created during the test run and close the browser page.

## Best Practices
- Write clear and descriptive test cases.
- Utilize page objects to encapsulate page-specific logic and interactions for better maintainability.

## References and Resources
- [Playwright Testing Framework](https://playwright.dev)
- [Ozone Community Forum](https://talk.openmrs.org/c/software/ozone-his)