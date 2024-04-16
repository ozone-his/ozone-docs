# Automated End-to-End Tests

All data flows within Ozone and the actions performed on its HIS components are rigorously validated using a comprehensive suite of automated end-to-end (E2E) tests.

This section is designed to help Ozone developers familiarize themselves with `ozone-e2e`, the repository where all end-to-end (E2E) tests for Ozone are maintained. It will guide you through the architecture of a typical E2E test case and provide the necessary knowledge and practical steps to develop your own test cases.

!!! question "Which automation testing framework?"

    `ozone-e2e` uses [Playwright <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://playwright.dev/)


!!! tip "Prequisites"

    Install **Node.js** version 18 or higher and **npm** version 10 or higher, see [here <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

## Setting up `ozone-e2e`
1. Clone the Ozone E2E Repository: Execute the command<br/>
`git clone https://github.com/ozone-his/ozone-e2e`

2. Navigate to the Project Directory: Change into the directory with<br/>
`cd ozone-e2e`

3. Install Dependencies: Install the required packages:<br/>
`npm install`

### Project structure
The actual E2E tests live in the `e2e` subfolder that is organised as follows:
```bash
e2e
 ├── tests
 |   ^ Contains test cases.
 └── utils
    ^ Contains utilities needed to set up and tear down tests,
      as well as methods required by the tests to run.
```

### Configuration Options

- **Environment Settings**: Use the `.env` file to configure test environment variables (e.g., E2E_BASE_URL).
- **Browser Selection**: Utilize the `--browser` flag to specify the browser (e.g., chrome, firefox).

## Running Tests
- Run all tests: `npx playwright test`
- Run tests in a specific file: `npx playwright test <file name>`
- Run tests with custom configuration: `npx playwright test --project=<browser name>`

## Interpreting Test Results
- **Passed**: All tests passed without any errors.
- **Failed**: One or more tests have failed during test execution.
- **Skipped**: Test was skipped due to a conditional directive or configuration.

## Developing New Test Cases
1. Create a `fileName.spec.js` file in the `e2e/tests` folder.
2. Write test scenarios using Playwright's API.
3. Utilize Playwright's API to interact with the browser, navigate to pages, interact with elements, perform actions, and make assertions.

### Example

**Test Purpose**: Verify that ordering lab test for an OpenMRS patient creates the corresponding SENAITE client with analysis request.

```javascript
import { test, expect } from '@playwright/test';
import { HomePage } from '../utils/functions/testBase';
import { patientName } from '../utils/functions/testBase';

let homePage: HomePage;

test.beforeEach(async ({ page }) => {
  homePage = new HomePage(page);
  await homePage.initiateLogin();
  await expect(page).toHaveURL(/.*home/);
  await homePage.createPatient();
  await homePage.startPatientVisit();
});

test('Ordering lab test for an OpenMRS patient creates the corresponding SENAITE client with analysis request', async ({ page }) => {
  // setup
  homePage = new HomePage(page);
  await homePage.goToLabOrderForm();
  await page.click('button:has-text("Add")');
  await page.selectOption('#tab select', '857AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
  await homePage.saveLabOrder();

  // replay
  await homePage.goToSENAITE();
  await expect(page).toHaveURL(/.*senaite/);

  // verify
  await homePage.searchClientInSENAITE();
  const clientName = `${patientName.firstName} ${patientName.givenName}`;
  const client = await page.$('table tbody tr:nth-child(1) td.contentcell.title div span a:has-text("' + clientName + '")');
  await expect(client).toBeVisible();
});

test.afterEach(async ({ page }) => {
  homePage = new HomePage(page);
  await homePage.deletePatient();
  await page.close();
});
```

#### Simplified Explanation

**Test Setup**: Before the test, login to O3, create a new patient, and start a visit.

**Test Case**:

- **Setup**: Navigate to the lab order form, add a new lab order, and save it.
- **Replay**: Go to the SENAITE and search for the client.
- **Verification**: Verify that the client's name is visible in the clients list.

**Cleanup**: After the test, delete the patient created during the test run and close the browser page.

## Best Practices
- Write clear and descriptive test cases.
- Utilize page objects to encapsulate page-specific logic and interactions for better maintainability.