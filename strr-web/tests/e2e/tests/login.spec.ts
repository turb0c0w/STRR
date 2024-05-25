import { test, expect } from '@playwright/test'
import dotenv from 'dotenv'
const authFile = 'tests/e2e/.auth/user.json'

// load default env
// eslint-disable-next-line import/no-named-as-default-member
dotenv.config()
test.describe('Login Tests', () => {
  test('login', async ({ page }) => {
    await page.goto('http://localhost:3000/account-select')
    await page.getByRole('button', { name: 'Log in' }).click()
    await page.getByRole('menuitem', { name: 'BC Services Card' }).click()
    await page.getByLabel('Test with username and password').click()
    await page.getByLabel('Email or username').fill(process.env.E2E_TEST_USERNAME!)
    await page.getByLabel('Password').click()
    await page.getByLabel('Password').fill(process.env.E2E_TEST_PASSWORD!)
    await page.getByRole('button', { name: 'Continue' }).click()
    expect(page.url()).toContain('account-select')
    const h1 = await page.textContent('h1')
    expect(h1).toBe('Existing Account Found')
    await page.context().storageState({ path: authFile });
  })
})
