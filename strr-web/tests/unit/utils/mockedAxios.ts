import { vi } from 'vitest'
import { testOrg, testUserSettings } from './mockedData'

const axiosRequestMocks = vi.hoisted(() => ({
  get: vi.fn().mockImplementation((url: string, config?: any) => {
    console.info('Mock is currently not doing anything with config', config)
    // account GET mocks
    // TODO: TC - what do we need here to test the account details lookup
    if (url.includes('orgs')) {
      return new Promise(resolve => resolve({ data: { ...testOrg } }))
    } else if (url.includes('settings')) {
      return new Promise(resolve => resolve({ data: [...testUserSettings] }))
    }
  })
}))

const axiosDefaultMock = {
  post: vi.fn(),
  get: axiosRequestMocks.get,
  delete: vi.fn(),
  put: vi.fn(),
  create: vi.fn().mockReturnThis(),
  interceptors: {
    request: {
      use: vi.fn(),
      eject: vi.fn()
    },
    response: {
      use: vi.fn(),
      eject: vi.fn()
    }
  }
}

export { axiosRequestMocks, axiosDefaultMock }
