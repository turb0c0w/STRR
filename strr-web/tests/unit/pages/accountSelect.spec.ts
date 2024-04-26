import { expect, describe, test } from 'vitest'
import { VueWrapper, mount } from '@vue/test-utils'
import { mockedI18n } from '@/tests/unit/utils/mockedi18n'
import accountSelect from '@/pages/accountSelect.vue'

describe('Tests for my account selection page', () => {
  let wrapper: VueWrapper<any>

  beforeEach(() => {
    wrapper = mount(accountSelect, { global: { plugins: [mockedI18n] } })
  })
  afterEach(() => { wrapper.unmount() })

  test('Contains all the expected elements', () => {
    expect(wrapper.find('[data-cy="accountSelectTable"]').exists()).toBe(true)
    expect(wrapper.find('[data-cy="accountSelectCreate"]').exists()).toBe(true)
  })
})
