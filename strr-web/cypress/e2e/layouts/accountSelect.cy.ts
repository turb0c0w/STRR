import accounts from '../../fixtures/accounts.json'
import accountDetails from '../../fixtures/accountDetails.json'

describe('Layout -> Account Select (No Active Accounts)', () => {
  it('shows correct values', () => {
    // TODO: TC - are these required just to do validation?
    // setup intercepts
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      accounts)
    cy.intercept(
      'GET',
      `https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/orgs/${account.id}`,
      accountDetails).as('accountDetails')

    // TODO: TC do we need fake login for this?

    cy.visit('/account-select')
    cy.wait(['@accounts', '@accountDetails'])

    // TODO: TC - existing-account-list should not exist
    // Check for other header
  })
})

describe('Layout -> Account Select (No Active Accounts)', () => {
  it('shows correct values', () => {
    // setup intercepts
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      accounts)
    cy.intercept(
      'GET',
      `https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/orgs/${account.id}`,
      accountDetails).as('accountDetails')

    // TODO: TC do we need fake login for this?

    cy.visit('/account-select')
    cy.wait(['@accounts', '@accountDetails'])

    // TODO: TC - existing-account-list should not exist
    // Check for other header
  })
})

describe('Layout -> Account Select (Active Accounts)', () => {
  it('shows correct values', () => {
    // setup intercepts
    cy.intercept(
      'GET',
      'https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/users/testSub/settings',
      accounts)
    cy.intercept(
      'GET',
      `https://auth-api-dev.apps.silver.devops.gov.bc.ca/api/v1/orgs/${account.id}`,
      accountDetails).as('accountDetails')

    // TODO: TC do we need fake login for this?

    cy.visit('/account-select')
    cy.wait(['@accounts', '@accountDetails'])

    // TODO: TC - existing-account-list should exist
    // Check for correct header based on account list, and check for details inside the existing-account-list

    // cy.get('#bcros-business-details').should('exist')
    // cy.get('[data-cy=business-details-name]').should('contain.text', 'Test')
  })
})
