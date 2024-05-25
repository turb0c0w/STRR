import { test, TestInfo, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright'

const authFile = 'tests/e2e/.auth/user.json'

test.describe('Create Account Test - Layout', () => {

  test.afterEach(async ({ page }, testInfo) => {
    const a11yResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze()
    expect(a11yResults.violations).toEqual([])
  })

  test('Layout', async ({ page }) => {
    await page.goto('/create-account')

    const logo = page.getByAltText('Government of British Columbia Logo')
    const header = page.getByTestId('header')
    const footer = page.getByTestId('footer')
    const footerLinks = footer.locator('a')

    expect(logo).toBeTruthy()
    await expect(header).toBeVisible();
    await expect(footer).toBeVisible();
    await expect(header).toBeInViewport()
    await expect(footer).toContainText('A BC Online Application')
    await expect(footerLinks).toHaveCount(5)
  })
});

test.describe('Create Account Test - Edge Case', () => {
  //Test before with not storage state, expect no name for now as a test
  test('Create Account - Full Name Test', async ({ page }) => {
    await page.goto('/create-account')
    const fullNameDiv = page.getByTestId('full-name');
    const fullName = await fullNameDiv.textContent();
    expect(fullName).toBe('- ')
  })
});

test.describe('Create Account Test - Happy Case', () => {
  //Test after storage state, expect a name for now as a test
  test.use({ storageState: authFile });
  test('Create Account - Full Name Test', async ({ page }) => {
    await page.goto('/create-account')
    const fullNameDiv = page.getByTestId('full-name');
    const fullName = await fullNameDiv.textContent();
    expect(fullName).toBe('BCREGTEST Delbert TWENTYFIVE')
  })

});