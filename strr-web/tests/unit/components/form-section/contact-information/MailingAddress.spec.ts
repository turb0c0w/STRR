// @vitest-environment nuxt
import { it, expect } from 'vitest'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import { createI18n } from 'vue-i18n'
import { BcrosFormSectionContactInformationMailingAddress, UInput, USelect } from '#components'
import { mockFn } from '@nuxt/test-utils'

const i18n = createI18n({
  // vue-i18n options here ...
})

it('can mount primary CRA Details Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const mailingAddress = await mountSuspended(BcrosFormSectionContactInformationMailingAddress,
    {
      global: { plugins: [i18n] },
      props: {
        id: '1',
        defaultCountryIso2: 'CA',
        enableAddressComplete: mockFn
      },
    })
  expect(mailingAddress.find('[data-cy="form-section-mailing"]').exists()).toBe(true)
  expect(mailingAddress.findComponent(USelect).text()).toContain('Canada')
})

it('can mount secondary CRA Details Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const mailingAddress = await mountSuspended(BcrosFormSectionContactInformationMailingAddress,
    {
      global: { plugins: [i18n] },
      props: {
        id: '1',
        defaultCountryIso2: 'CA',
        enableAddressComplete: mockFn
      },
    })
  expect(mailingAddress.find('[data-cy="form-section-mailing"]').exists()).toBe(true)
  expect(mailingAddress.findComponent(USelect).text()).toContain('Canada')
})


