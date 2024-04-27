import 'cypress-axe'

Cypress.Commands.add('interceptAccounts', () => {
  cy.fixture('accounts').then((accounts) => {
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      accounts)
  })
})

Cypress.Commands.add('interceptAccountDetails', () => {
  cy.fixture('accounts').then((details) => {
    cy.fixture('businessContact').then((contact) => {
      cy.intercept(
        'GET',
        `https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/entities/${business.identifier}`,
        contact)
    })
  })
})

Cypress.Commands.add('visitHomePageWithFakeData', () => {
  cy.interceptPostsEntityApi().as('existingSIs')
  cy.interceptPayFeeApi().as('payFeeApi')
  cy.interceptBusinessContact().as('businessContact')
  cy.interceptBusinessSlim().as('businessApiCall')
  cy.visit('/')
  cy.wait(['@existingSIs', '@businessApiCall', '@payFeeApi', '@businessContact'])
})

Cypress.Commands.add('visitHomePageWithFakeDataAndAxeInject', () => {
  cy.visitHomePageWithFakeData()
  cy.injectAxe()
})

