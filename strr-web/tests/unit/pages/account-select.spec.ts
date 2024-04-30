import { expect, describe, test } from 'vitest'
import { VueWrapper, mount } from '@vue/test-utils'
import { mockedI18n } from '@/tests/unit/utils/mockedi18n'
import accountSelect from '@/pages/account-select.vue'

describe('Tests for Account Selection page', () => {
  let wrapper: VueWrapper<any>

  beforeEach(() => {
    wrapper = mount(accountSelect, { global: { plugins: [mockedI18n] } })
  })
  afterEach(() => { wrapper.unmount() })

  test('Contains all the expected elements', () => {
    expect(wrapper.find('[data-cy="account-select-page"]').exists()).toBe(true)
    // TODO: TC - add the existing account list if there are accounts?
  })
})
