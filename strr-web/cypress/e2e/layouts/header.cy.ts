describe('Layout -> Header', () => {
  it('shows the header on Home Page', () => {
    cy.visit('/')
    cy.get('#bcros-main-header').should('exist')
  })

  it('shows the header on Account Select Page', () => {
    cy.visit('/account-select')
    cy.get('#bcros-main-header').should('exist')
  })
})
