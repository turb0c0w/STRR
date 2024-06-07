import { fileURLToPath } from 'node:url'
import { defineConfig, devices, selectors } from '@playwright/test'
import type { ConfigOptions } from '@nuxt/test-utils/playwright'

const devicesToTest = [
  'Desktop Chrome'
] satisfies Array<string | typeof devices[string]>

export default defineConfig<ConfigOptions>({
  testDir: './tests/e2e',
  reporter: [['html', { outputFolder: 'test-results', open: 'never' }]],
  forbidOnly: !!process.env.CI,
  retries: 3, 
  use: {
    testIdAttribute: 'data-cy',
    actionTimeout: 0,
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'off',
    video: 'on',
    headless: true
  },
  projects: devicesToTest.map(p => typeof p === 'string' ? ({ name: p, use: devices[p] }) : p),
  webServer: {
    command: 'pnpm run dev', 
    url: 'http://localhost:3000', 
    timeout: 30 * 1000, // Timeout to wait for the server to start (in milliseconds)
    reuseExistingServer: !process.env.CI, // Reuse existing server if not in CI environment
  }
})