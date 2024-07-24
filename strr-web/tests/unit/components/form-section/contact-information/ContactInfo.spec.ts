// @vitest-environment nuxt
import { it, expect } from 'vitest'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import { createI18n } from 'vue-i18n'

import { BcrosFormSection, BcrosFormSectionContactInformationContactInfo } from '#components'

const i18n = createI18n({
  // vue-i18n options here ...
})

it('can mount primary Contact Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const contactDetails = await mountSuspended(BcrosFormSectionContactInformationContactInfo,
    {
      global: { plugins: [i18n] },
      props: { isPrimary: true },
    })
  expect(contactDetails.find('[data-cy="form-section-contact"]').exists()).toBe(true)
  expect(contactDetails.findComponent(BcrosFormSection).text()).not.toContain(t('general.optional'))
})

it('can mount secondary Contact Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const contactDetails = await mountSuspended(BcrosFormSectionContactInformationContactInfo,
    {
      global: { plugins: [i18n] },
      props: { isPrimary: false },
    })
  expect(contactDetails.find('[data-cy="form-section-contact"]').exists()).toBe(true)
  expect(contactDetails.findComponent(BcrosFormSection).text()).toContain(t('general.optional'))
})


