import { test, expect } from '@playwright/test'
import { finalizeData, registrationData, getRandomNumber } from '@/tests/e2e/utils/mockedData'
import path from 'path'
const authFile = 'tests/e2e/.auth/user.json'

test.describe('Create SBC Account and Complete Registration - Check an application can be submitted ', () => {
  const sbcRandomNum = getRandomNumber() 
  const regRandomNum = getRandomNumber()
  test.use({ storageState: authFile })
  
  test('Create SBC Account & Registration', async ({ page }) => {
    // Increase the test timeout to 60 seconds
    test.setTimeout(60000)
    // start with new account if not using existing one
    if (finalizeData.useExisting) {
      await page.goto('/create-account')
      await page.getByRole('button', { name: ' B ' + process.env.E2E_TEST_BCSC_ACCOUNT! }).click()
      await page.getByRole('menuitem', { name: ' ' + process.env.E2E_TEST_SBC_ACCOUNT! }).click()
    } else {
      await page.goto('/account-select', { waitUntil: 'load', timeout: 10000})
      const fullNameDiv = page.getByTestId('al-username')
      const fullName = await fullNameDiv.textContent()
      expect(fullName).toBe(process.env.E2E_TEST_BCSC_ACCOUNT!)
      await page.getByRole('button', { name: 'Create account' }).click()
      await page.waitForURL('**/finalization')
      const h1 = await page.textContent('h1')
      expect(h1).toBe('Service BC Account Creation')
      await page.fill('input[name="name"]', finalizeData.accountName + sbcRandomNum)
      await page.fill('input[name="phone"]', finalizeData.phone)
      await page.fill('input[name="extension"]', finalizeData.extension)
      await page.fill('input[name="email"]', finalizeData.email)
      await page.getByRole('button', { name: 'Save & Start Registration' }).click()
      await page.waitForURL('**/terms-of-service')
      await page.getByRole('button', { name: 'Accept Terms' }).click()
    }      
    await page.waitForURL('**/create-account')

    //check registration page looks correct - account names and fees
    const feeAmountDiv = page.getByTestId('fee-amount')
    await page.waitForSelector(`text="$21.50"`, { timeout: 10000 })
    const feeAmount = await feeAmountDiv.textContent()
    expect(feeAmount).toBe('$21.50')
    const sbcAccountSetDiv = page.getByTestId('al-account-name')
    const sbcAccount = await sbcAccountSetDiv.textContent()
    if (finalizeData.useExisting) {
      expect(sbcAccount).toBe(process.env.E2E_TEST_SBC_ACCOUNT)
    } else {
      expect(sbcAccount).toBe(finalizeData.accountName + sbcRandomNum)
    }

    // form fill - step 1
    await page.fill('input[name="birthDay"]', registrationData.contactBirthDay)
    await page.selectOption('select[name="month"]', registrationData.contactBirthMonth)
    await page.fill('input[name="birthYear"]', registrationData.contactBirthYear)
    await page.fill('input[name="socialInsuranceNumber"]', registrationData.contactSocialInsuranceNumber)
    await page.fill('input[name="preferredName"]', registrationData.contactSocialInsuranceNumber)
    await page.fill('input[name="extension"]', registrationData.contactExtension)
    await page.fill('input[name="faxNumber"]', registrationData.contactPhoneNumber)
    await page.fill('input[name="emailAddress"]', registrationData.contactEmailAddress)
    await page.selectOption('select[name="country"]', registrationData.contactCountry)
    await page.fill('input[name="address"]', registrationData.contactAddress)
    await page.fill('input[name="city"]', registrationData.contactCity)
    await page.fill('input[name="province"]', registrationData.contactProvince)
    await page.fill('input[name="postalCode"]', registrationData.contactPostalCode)
    await page.getByRole('button', { name: 'Next' }).click()
    // form fill - step 2
    await page.fill('input[name="nickname"]', registrationData.unitNickname + regRandomNum)
    await page.selectOption('select[name="country"]', registrationData.unitCountry)
    await page.fill('input[name="Address"]', registrationData.unitAddress)
    await page.fill('input[name="city"]', registrationData.unitCity)
    await page.fill('input[name="postalCode"]', registrationData.unitPostalCode)
    await page.selectOption('select[name="propertyType"]', registrationData.unitPropertyType)
    await page.selectOption('select[name="ownershipType"]', registrationData.unitOwnershipType)
    await page.fill('input[name="url"]', registrationData.unitUrl)
    await page.getByRole('button', { name: 'Next' }).click()
    // form fill - step 3
    await page.locator('label:has-text("Yes, my property has a principal residence requirement")').click()
    if (registrationData.isPrincipalResidence) {
      await page.check('input[name="declaration"]')
    }
    const filePath = path.resolve(__dirname, '../utils', '1.pdf')
    await page.setInputFiles('input[type="file"][aria-label="Supporting document file upload"]', filePath)
    await page.getByRole('button', { name: 'Next' }).click()
    // form fill - step 4
    if (registrationData.agreedToRentalAct) {
      await page.locator('label:has-text("I confirm")').click()
    }
    // check for no existance of errors
    const altText = 'Step did not pass validation'
    const errorImage = page.locator(`img[alt="${altText}"]`)
    await expect(errorImage).not.toBeVisible()
    await page.getByRole('button', { name: 'Submit and Pay' }).click()
    await page.waitForURL('**/scripts/payment/**', { waitUntil: "networkidle" } )
    // pay
    await page.getByLabel('Card Number').fill(process.env.E2E_TEST_CC_NUMBER!)
    await page.selectOption('select[name="trnExpMonth"]', process.env.E2E_TEST_CC_EXPIRY_MONTH!)
    await page.selectOption('select[name="trnExpYear"]', process.env.E2E_TEST_CC_EXPIRY_YEAR!)
    await page.getByLabel('Card CVD').fill(process.env.E2E_TEST_CC_CVD!)
    // Click the "Submit Payment" button
    await page.getByRole('button', { name: 'Submit Payment' }).click()
    await page.waitForURL('**/success/**/invoice/**', { waitUntil: 'load', timeout: 10000 })
    expect(page.url()).toMatch(/\/success\/\d+\/invoice\/\d+/)
    // Confirm submission
    await page.waitForSelector('h1:has-text("Application Submitted")', { timeout: 5000 })
    const submittedH1 = await page.textContent('h1')
    expect(submittedH1).toBe('Application Submitted')
    // check for adddress that matches on confirmation page
    const addressLocator = page.locator(`p.font-bold:has-text("${registrationData.unitAddress}")`)
    await expect(addressLocator).toHaveCount(1)
    // get reg id from the success page
    const url = page.url()
    const match = url.match(/\/success\/(\d+)\/invoice\/\d+/)
    const regId = match ? match[1] : null
    expect(regId).not.toBeNull()
    const baseUrl = new URL(url).origin
    // click on dashboard link
    await page.click('a:has-text("View your application status")')
    await page.waitForURL('**/application-status', { waitUntil: 'load' })
    // check for state/address in list
    const nickNameLocator = page.locator(`p.font-bold:has-text("${registrationData.unitNickname + regRandomNum}")`)
    await expect(nickNameLocator).toHaveCount(1)
    // navigate to the registration and perform checks
    const newUrl = `${baseUrl}/application-details/${regId}`
    await page.goto(newUrl, { waitUntil: 'load'})
    // verify filing history 
    const paymentLocator = page.locator(`p.font-bold:has-text('Payment Confirmed')`)
    await expect(paymentLocator).toHaveCount(1)
    // verify files
    const fileLocator = page.locator(`p:has-text('1.pdf')`)
    await expect(fileLocator).toHaveCount(1)
  })

  test('Create SBC Account & Registration - Check an empty registration cannot be submitted', async ({ page }) => {
    await page.goto('/create-account')
    await page.getByRole('button', { name: 'Next' }).click()
    await page.getByRole('button', { name: 'Next' }).click()
    await page.getByRole('button', { name: 'Next' }).click()
    await page.getByRole('button', { name: 'Submit and Pay' }).click()
    // check for existance of errors
    const altText = 'Step did not pass validation'
    const errorImage = page.locator(`img[alt="${altText}"]`).first()
    await expect(errorImage).toBeVisible()
    const confirmLabel = page.locator('label:has-text("I confirm")')
    await expect(confirmLabel).toBeVisible()
  })
})