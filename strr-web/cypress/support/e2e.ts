import 'cypress-axe'

Cypress.Commands.add('interceptAccounts', () => {
  cy.fixture('accounts').then((accounts) => {
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      accounts)
  })
})

Cypress.Commands.add('interceptNoAccounts', () => {
  cy.fixture('noAccounts').then((noAccounts) => {
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      noAccounts)
  })
})

Cypress.Commands.add('interceptAccountDetails', () => {
  cy.fixture('accountDetails').then((accountDetails) => {
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/orgs/123',
      accountDetails)
  })
})

Cypress.Commands.add('visitAccountSelectWithNoAuth', () => {
  cy.visit('/account-select')
})

Cypress.Commands.add('visitAccountSelectAuthWithNoAccounts', () => {
  cy.interceptAccounts().as('noAccounts')
  cy.visit('/account-select')
  cy.wait(['@accounts', '@accountDetails'])
})

Cypress.Commands.add('visitAccountSelectAuthWithActiveAccounts', () => {
  cy.interceptAccounts().as('accounts')
  cy.interceptAccountDetails().as('accountDetails')
  cy.visit('/account-select')
  cy.wait(['@accounts', '@accountDetails'])
})


