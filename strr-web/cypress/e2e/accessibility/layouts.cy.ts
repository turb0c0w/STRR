describe('accessibility -> Business Layout', () => {
  beforeEach(() => {
    // setup intercepts
    cy.interceptAccounts().as('accounts')
    cy.interceptNoAccounts().as('noAccounts')
    cy.interceptAccountDetails().as('accountDetails')
  })

  it('checks Account Select Page passes accessibility (logged out)', () => {
    sessionStorage.setItem('FAKE_LOGIN', '')
    cy.visit('/account-select')
    cy.injectAxe()

    // TODO: TC - change to our layout when no account
    // cy.checkA11y({ exclude: ['[data-cy=owner-change]'], include: ['[data-cy=header]'] })
  })

  it('checks Account Select Page passes accessibility (logged in, active accounts)', () => {
    sessionStorage.setItem('FAKE_LOGIN', 'true')
    cy.visit('/account-select')

    // TODO: TC - change to our api calls
    cy.wait(['@accounts', '@accountDetails'])
    cy.injectAxe()

    // TODO: TC - check out layout when someone is auth and has active accounts
    // Click example below
    // Include clicking the two buttons - create and choose - move this to AccountSelect?

    // cy.checkA11y({ exclude: ['[data-cy=owner-change]'], include: ['[data-cy=header]'] })
    // cy.get('[data-cy=logged-out-menu]').click()
    // cy.wait(250)
    // cy.checkA11y({ exclude: ['[data-cy=owner-change]'], include: ['[data-cy=header]'] })

    // footer
    // cy.checkA11y({ exclude: ['[data-cy=owner-change]'], include: ['[data-cy=footer]'] })
  })
})
