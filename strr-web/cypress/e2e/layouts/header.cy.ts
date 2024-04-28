describe('Layout -> Header', () => {
  it('shows header on Home Page', () => {
    cy.visit('/')
    cy.get('#bcros-main-header').should('exist')
  })

  it('shows header on Account Select Page', () => {
    cy.visit('/account-select')
    cy.get('#bcros-main-header').should('exist')
  })

  // TODO: TC - add one for logged out regarding menus

})
