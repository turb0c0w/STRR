import { test, expect } from '@playwright/test';

const authFile = 'tests/e2e/.auth/user.json'

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