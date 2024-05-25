import { fileURLToPath } from 'node:url'
import { defineConfig, devices } from '@playwright/test'
import type { ConfigOptions } from '@nuxt/test-utils/playwright'

const devicesToTest = [
    'Desktop Chrome'
  ] satisfies Array<string | typeof devices[string]>
  
  export default defineConfig<ConfigOptions>({
    testDir: './tests/e2e',
    reporter: 'line',
    forbidOnly: !!process.env.CI,
    retries: 3, 
    use: {
      nuxt: {
        rootDir: fileURLToPath(new URL('.', import.meta.url))
      },
      actionTimeout: 0,
      baseURL: 'http://localhost:3000',
      trace: 'on-first-retry',
      screenshot: 'off',
      headless: true
    },
    projects: devicesToTest.map(p => typeof p === 'string' ? ({ name: p, use: devices[p] }) : p),
    webServer: {
      command: 'pnpm run dev'
    }
  })