import { fileURLToPath } from 'node:url'
import { defineVitestConfig } from '@nuxt/test-utils/config'
import { configDefaults } from 'vitest/config'

export default defineVitestConfig({
  test: {
    dir: 'tests',
    // coverage: {
    //     reportsDirectory: 'coverage',
    // },

    coverage: {
      exclude: [
        "*.config.ts",
        "enums/*",
        "interfaces/*",
        "*.d.ts",
        ".nuxt/*"
      ],
    },
    environment: 'nuxt',
    environmentOptions: {
      nuxt: {
        rootDir: fileURLToPath(new URL('./', import.meta.url)),
        domEnvironment:
          (process.env.VITEST_DOM_ENV as 'happy-dom' | 'jsdom') ?? 'happy-dom'
      }
    },
    // setupFiles: ['./tests/setup/mocks.ts'],
    globals: true
  }
})
