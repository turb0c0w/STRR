import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright'

const authFile = '@/tests/e2e/.auth/user.json';

test.describe('Account Select Test', () => {

  test.afterEach(async ({ page }) => {
    const a11yResults = await new AxeBuilder({ page })
      .analyze()
    expect(a11yResults.violations).toEqual([])
  })

  test('Layout', async ({ page }) => {
    const logo = page.getByAltText('Government of British Columbia Logo')
    const header = page.getByTestId('bcros-main-header')
    const footer = page.getByTestId('bcros-main-footer')
    const footerLinks = footer.locator('a')
    expect(logo).toBeTruthy()
    expect(header).toBeInViewport()
    expect(footer).toBeInViewport()
    expect(footer).toContainText('A BC Online Application')
    expect(footerLinks).toHaveCount(5)
  })

  //Test before with not storage state, expect no list
  test('Edge Case', async ({ page }) => {
    const h1 = await page.textContent('h1')
    expect(h1).toBe('Please Login')
  })

  //Test after storage state, expect a list
  test.use({ storageState: authFile });
  test('Happy Path', async ({ page }) => {
    const h1 = await page.textContent('h1')
    expect(h1).toBe('Existing Accounts')
  })

});