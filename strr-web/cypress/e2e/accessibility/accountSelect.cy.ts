import 'cypress-plugin-tab'

describe('accessibility -> Account Select', () => {
  beforeEach(() => {
    cy.visitAccountSelectAuthWithActiveAccounts()
    cy.injectAxe()
  })

  it('checks page passes accessibility', () => {

    // For now, this is an example of passing checks
    cy.checkA11y('[data-cy=page-header]')
    cy.checkA11y('[data-cy=page-info-text]')
    cy.checkA11y('[data-cy=add-new-btn]')


    //TODO: TC - change to the account select layout, or use table below

    cy.fixture('individuals').then((testData) => {
      cy.get('#individual-person-full-name').type(testData.profile1.fullName)
      cy.get('[data-cy=usePreferredName').check()
      cy.get('[data-cy=testPercentOfShares]').click()
      cy.checkA11y('[data-cy=addIndividualPerson]',
        {
          rules: {
            // todo: fixme: nested-interactive should be removed/set to true after resolving it after
            //  discussion with nuxt-ui team
            // first ticket for opening discussions: https://github.com/bcgov/entity/issues/19775
            'nested-interactive': { enabled: false }
          }
        }
      )
    })

  })


  //TODO - TC - change this to use our table instead?
  it('checks the summary table passes accessibility', () => {

  //   cy.checkA11y('[data-cy=individualsSummaryTable]', { rules: { 'nested-interactive': { enabled: false } } })
    
  //   cy.get('[data-cy=popover-button]').eq(0).click()
  //   cy.wait(100)
  //   cy.checkA11y('[data-cy=summary-table-buttons]', {
  //     rules: {
  //       'nested-interactive': { enabled: false },
  //       'aria-hidden-focus': { enabled: false }
  //     }
  //   })

  //   // close the popover panel
  //   cy.get('[data-cy=popover-button]').eq(0).click()

  //   // empty table
  //   cy.get('[data-cy=popover-button]').then((buttons) => {
  //     for (let i = 0; i < buttons.length; i++) {
  //       cy.get('[data-cy=popover-button]').first().click()
  //       cy.get('[data-cy=remove-button]').click()
  //     }
  //   })
  //   cy.checkA11y('[data-cy=individualsSummaryTable]')
  // 
  })

})
