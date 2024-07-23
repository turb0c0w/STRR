import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

const authFile = 'tests/e2e/.auth/user.json'

test.describe('Account Select Test - Layout', () => {

  test.afterEach(async ({ page }, testInfo) => {
    const a11yResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze()
    expect(a11yResults.violations).toEqual([])
  })

  test('Layout', async ({ page }) => {
    await page.goto('/account-select')

    const logo = page.getByAltText('Government of British Columbia Logo')
    const header = page.getByTestId('header')
    const footer = page.getByTestId('footer')
    const footerLinks = footer.locator('a')

    expect(logo).toBeTruthy()
    await expect(header).toBeVisible()
    await expect(footer).toBeVisible()
    await expect(header).toBeInViewport()
    await expect(footer).toContainText('A BC Online Application')
    await expect(footerLinks).toHaveCount(5)
  })
})

test.describe('Create Account Test - Existing accounts', () => {
  test.use({ storageState: authFile })
  test('Existing Accounts - Found', async ({ page }) => {
    await page.goto('/account-select')
    const h1 = await page.textContent('h1')
    expect(h1).toBe('Existing Account Found')
  })

})