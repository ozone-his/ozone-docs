# Automated End-to-End Tests

All data flows within Ozone and the actions performed on its HIS components are rigorously validated using a comprehensive suite of automated end-to-end (E2E) tests.

This section is designed to help Ozone developers familiarize themselves with [`ozone-e2e`](https://github.com/ozone-his/ozone-e2e), the repository where all end-to-end tests for Ozone are maintained. It will guide you through the architecture of a typical end-to-end test case and provide the necessary knowledge and practical steps to develop your own test cases.

!!! info "Some facts about `ozone-e2e`"

    - We use [Playwright <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://playwright.dev/), the automation testing framework.
    - We test our data flows through the actions and effects that they have on Ozone HIS components.
    - We focus on how these actions and effects are experienced by end users.

!!! tip "Software Prequisites"

    [:simple-nodedotjs: Node.js (version 18 or higher) and :simple-npm: npm (version 10 or higher) <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

## Setting up `ozone-e2e`
Clone the Ozone E2E Repository: Execute the command<br/>
```bash
git clone https://github.com/ozone-his/ozone-e2e
```
Navigate to the Project Directory: Change into the directory with<br/>
```bash
cd ozone-e2e
```
Install Dependencies: Install the required packages<br/>
```bash
npm install
```

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

The data flows resulting from the integration between specific component pairs (e.g., between Odoo and OpenMRS) are typically tested through a designated test file for each pair (e.g., `odoo-openmrs-flows.spec.js`). All test files are located in the [`e2e/tests` directory](https://github.com/ozone-his/ozone-e2e/tree/main/e2e/tests). We encourage you to explore and review the current set of tests to understand the testing process better and evaluate the extent of their coverage.

### Project configuration

Our E2E test suite is designed to interact with three distinct Ozone environments, allowing seamless switching as needed:

|          |                                                                                                                                             |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Dev**  | Hosts the latest, bleeding-edge versions of Ozone, updated continuously as the development team commits new code to the Ozone repositories. |
| **QA**   | Used for staging Ozone prior to releases, facilitating final rounds of testing to ensure quality before launch.                             |
| **Demo** | Features the latest stable release of Ozone, readily accessible online for demonstration purposes and advertised through the Ozone website. |

Two important configuration variables govern the high-level behavior of our E2E test suite:

1. **`TEST_ENVIRONMENT`**: This variable specifies which one of the three environments — `dev`, `qa`, or `demo` — should be targeted for testing.<br/>E.g.:
```
TEST_ENVIRONMENT=dev
```

2. **`TEST_PRO`**: This toggle, set to `true` for testing Ozone Pro or `false` for Ozone FOSS, determines the flavour of Ozone HIS under test.<br/>E.g.:
```
TEST_PRO=false
```

All configuration variables are set to the desired values by editing and saving the [`.env` file <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://github.com/ozone-his/ozone-e2e/blob/main/.env) prior to running the tests.

Additionally, the `.env` file contains a range of configuration variables that specify the URLs for accessing the various HIS components in each test environment, as well as the credentials needed to execute the test cases.

## Running Tests

### Default test execution
To run all tests in the test suite, use the default command:

```
npx playwright test
```

### Running specific tests
To focus on testing data flows between specific pairs of HIS components, you can run tests contained in a specific file. For example, to test the integration data flows between Odoo and OpenMRS:

```
npx playwright test odoo-openmrs-flows
```

### Selecting your browser
Playwright supports various configurations for running tests across different browsers. Specify the browser using the `--project` flag. For instance, to run tests in Chromium:

```
npx playwright test --project=chromium
```

### Interpreting test results

- **Passed**: When all tests within the suite pass without encountering any errors, the overall result is marked as "Passed". This means that the application behaved as expected under the test conditions.

- **Failed**: If any test within the suite encounters an error or assertion failure during execution, the overall result is marked as "Failed". Determine whether the failure is specific to the test case, a particular component or feature, or the entire application. Once you've identified the root cause of the failure, implement a fix to address the issue. This may involve modifying test assertions, updating application code, or addressing environmental dependencies.

- **Skipped**: Sometimes, tests are intentionally skipped based on certain conditions or configurations. These skipped tests are not executed during the test run and are marked as "Skipped" in the test result.

## Developing Test Cases

### Naming test files

Our test cases cover the data flows between Ozone HIS components and we have taken the convention to group test cases by pairs of components. For example all data flows between OpenMRS and SENAITE are grouped together in a file named `openmrs-senaite-flows.spec.js` that lives in the `e2e/tests`. This file contains all test cases for data flows going from OpenMRS to SENAITE as well as those going from SENAITE to OpenMRS.

The naming is alphabetical per convention. The data flows going both ways between hypothetical HIS components _Foo_ and _Bar_ would live in a file named `bar-foo-flows.spec.js` and so on and so forth for all pairs of HIS components.

### Testing actions and effects

While Ozone relies on its components default behaviour and features, we do encompass in our E2E test suite the actions performed when using the user experience of the components and the effects observed throught the user experience of those components. This ensures that test are truly end-to-end with a focus on the end-user experience.

To write a test case:

- Identify the user interactions and functionalities to test between a pair of HIS components.
- Use Playwright’s API to script the actions within each test scenario, such as navigating pages, clicking buttons, filling forms, and verifying UI elements.

### Utilizing Playwright

Leverage Playwright’s comprehensive API to engage with the browser:

- Navigate to pages.
- Interact with page elements.
- Execute actions.
- Assert expected behaviors using methods like `expect`, `toEqual`, `toContain`, etc.

For detailed usage, refer to [Playwright's documentation <small>:fontawesome-solid-arrow-up-right-from-square:</small>](https://playwright.dev/docs/intro).

Once you've written your test, use the appropriate test runner to check that the test works as expected. For instance for the OpenMRS-SENAITE flows written in `openmrs-senaite-flows.spec.js`, run:
```
npx playwright test openmrs-senaite-flows
```

### Analyzing a sample test case

Again, following our example of the data flows between OpenMRS and SENAITE, let us verify that ordering a lab test for an OpenMRS patient does create the corresponding SENAITE client with an analysis request. Let us look at the sample test case code below:

```javascript
import { test, expect } from '@playwright/test';
import { OpenMRS, patientName } from '../utils/functions/openmrs';
import { SENAITE } from '../utils/functions/senaite';

let openmrs: OpenMRS;
let senaite: SENAITE;

test.beforeEach(async ({ page }) => {
  openmrs = new OpenMRS(page);
  senaite = new SENAITE(page);

  await openmrs.login();
  await expect(page).toHaveURL(/.*home/);
  await openmrs.createPatient();
  await openmrs.startPatientVisit();
});

test('Ordering a lab test for an OpenMRS patient creates the corresponding SENAITE client with an analysis request.', async ({ page }) => {
  
  // replay
  await openmrs.goToLabOrderForm();
  await page.click('button:has-text("Add")');
  await page.selectOption('#tab select', '857AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
  await openmrs.saveLabOrder();

  // verify
  await senaite.open();
  await expect(page).toHaveURL(/.*senaite/);
  await senaite.searchClient();
  const clientName = `${patientName.firstName} ${patientName.givenName}`;
  const client = await page.$('table tbody tr:nth-child(1) td.contentcell.title div span a:has-text("' + clientName + '")');
  await expect(client).toBeVisible();

});

test.afterEach(async ({ page }) => {
  await openmrs.deletePatient();
  await page.close();
});
```

We observe that the test structure is broken down between a **setup**, the actual **test case** and a **cleanup**:

**Test Setup**: Before the actual test, we perform some preliminary actions: logging into Ozone (with SSO), creating a new patient, and starting a visit for the newly created patient.

**Test Case**: The core of each test case follows the _Given-When-Then_ pattern (organised here as Setup-Replay-Verification). We highly recommend this structured approach as it clearly delineates the setup of the test ("Setup"), the end-user actions performed ("Replay"), and the assertion of outcomes as experienced by the end-user ("Verification"). In our example:

- **Setup**: Omitted here. All aspects of the setup have been performed in the `beforeEach()` method.
- **Replay**: Navigation to the lab order form, add a lab test, and save the form.
- **Verification**: Navigation to the SENAITE HIS component and search for the client by name. Verify that the client's name is visible in the clients list.

**Cleanup**: The post-test cleanup consists of deleting the test patient and closing the browser page.
