describe('Layout -> Footer', () => {
  it('shows the footer on Home Page', () => {
    cy.visit('/')
    cy.get('#bcros-main-footer').should('exist')
  })

  it('shows the footer on Account Select Page', () => {
    cy.visit('/account-select')
    cy.get('#bcros-main-footer').should('exist')
  })
})
