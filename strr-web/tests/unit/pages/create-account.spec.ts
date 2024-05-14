import { expect, describe, test } from 'vitest'
import { VueWrapper, mount } from '@vue/test-utils'
import { mockedI18n } from '@/tests/unit/utils/mockedi18n'
import createAccount from '@/pages/create-account.vue'

describe('Tests for Account Selection page', () => {
  let wrapper: VueWrapper<any>

  beforeEach(() => {
    wrapper = mount(createAccount, { global: { plugins: [mockedI18n] } })
  })
  afterEach(() => { wrapper.unmount() })

  test('Contains all the expected elements', () => {
    expect(wrapper.find('[data-cy="create-account-page"]').exists()).toBe(true)
    // TODO: TC - add the existing account list if there are accounts?
  })
})
