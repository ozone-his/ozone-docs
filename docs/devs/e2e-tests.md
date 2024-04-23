# Automated End-to-End Tests

All data flows within Ozone and the actions performed on its HIS components are rigorously validated using a comprehensive suite of automated end-to-end (E2E) tests.

This section is designed to help Ozone developers familiarize themselves with [`ozone-e2e`](https://github.com/ozone-his/ozone-e2e), the repository where all end-to-end tests for Ozone are maintained. It will guide you through the architecture of a typical end-to-end test case and provide the necessary knowledge and practical steps to develop your own test cases.

!!! info "Some facts about `ozone-e2e`"

    - We use [Playwright <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://playwright.dev/), the automation testing framework.
    - We test our data flows through the actions and effects that they have on Ozone HIS components.
    - We focus on how these actions and effects are experienced by end users.

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
```
e2e
 ├── tests
 |   ^ Contains test cases.
 └── utils
    ^ Contains utilities needed to set up and tear down tests,
      as well as methods required by the tests to run.
```

### Project configuration

Our E2E test suite is designed to interact with three distinct Ozone environments, allowing seamless switching as needed:

|          |                                                                                                                                             |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Dev**  | Hosts the latest, bleeding-edge versions of Ozone, updated continuously as the development team commits new code to the Ozone repositories. |
| **QA**   | Used for staging Ozone prior to releases, facilitating final rounds of testing to ensure quality before launch.                             |
| **Demo** | Features the latest stable release of Ozone, readily accessible online for demonstration purposes and advertised through the Ozone website. |

Two important configuration variables govern the high-level behavior of our E2E test suite:

1. **`TEST_ENVIRONMENT`**: This variable specifies which one of the three environments — `dev`, `qa`, or `demo` — should be targeted for testing.<br/>E.g., `TEST_ENVIRONMENT=dev`.
2. **`TEST_PRO`**: This toggle, set to `true` for testing Ozone Pro or `false` for Ozone FOSS, determines the flavour of Ozone HIS under test.<br/>E.g., `TEST_PRO=false`.

All configuration variables are set to the desired values by editing and saving the [`.env` file <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://github.com/ozone-his/ozone-e2e/blob/main/.env) prior to running the tests.

Additionally, the `.env` file contains a range of configuration variables that specify the URLs for accessing the various HIS components in each test environment, as well as the credentials needed to execute the test cases.

## Running Tests
- Run all tests: Execute all tests available in your test suite using the following command:

```bash
 npx playwright test
```

- Run tests in a specific file. If you want to focus on a particular test file, specify the file name, and only tests within that file will be executed. For example:

```bash
 npx playwright test testOdooIntegration
```

- Run tests with custom configuration. Playwright allows you to define different configurations for running tests in various browsers. You can specify the browser name (e.g., "chromium", "firefox", "webkit") using the --project flag to run tests in a specific browser. For instance:

```bash
 npx playwright test --project=chromium
```

 Interpreting Test Results

- **Passed**: When all tests within the suite pass without encountering any errors, the overall result is marked as "Passed". This means that the application behaved as expected under the test conditions.
- **Failed**: If any test within the suite encounters an error or assertion failure during execution, the overall result is marked as "Failed". Determine whether the failure is specific to the test case, a particular component or feature, or the entire application. Once you've identified the root cause of the failure, implement a fix to address the issue. This may involve modifying test assertions, updating application code, or addressing environmental dependencies.

- **Skipped**: Sometimes, tests are intentionally skipped based on certain conditions or configurations. These skipped tests are not executed during the test run and are marked as "Skipped" in the test result.

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

The core of each test case follows the Given-When-Then format (delineated here as Setup-Replay-Verification). We highly recommend this structured approach as it clearly delineates the setup of the test environment (Setup), the actions performed (Replay), and the verification of outcomes (Verification).

- **Setup**: Navigate to the lab order form, add a new lab order, and save it.
- **Replay**: Go to the SENAITE and search for the client.
- **Verification**: Verify that the client's name is visible in the clients list.

**Cleanup**: After the test, delete the patient created during the test run and close the browser page.

## Best Practices
- Write clear and descriptive test cases.
- Utilize page objects to encapsulate page-specific logic and interactions for better maintainability.
