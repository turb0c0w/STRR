// @vitest-environment nuxt
import { it, expect } from 'vitest'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import { createI18n } from 'vue-i18n'
import { BcrosFormSectionContactInformationCraInfo, UInput } from '#components'

const i18n = createI18n({
  // vue-i18n options here ...
})

it('can mount primary CRA Details Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const craInfo = await mountSuspended(BcrosFormSectionContactInformationCraInfo,
    {
      global: { plugins: [i18n] },
      props: { isPrimary: true },
    })
  expect(craInfo.find('[data-cy="form-section-cra-info"]').exists()).toBe(true)
  expect(craInfo.find(`[placeholder="${t('create-account.contact-form.socialInsuranceNumber')}"]`).exists()).toBe(true)
})

it('can mount secondary CRA Details Form Section component', async () => {
  const t = useNuxtApp().$i18n.t
  const craInfo = await mountSuspended(BcrosFormSectionContactInformationCraInfo,
    {
      global: { plugins: [i18n] },
      props: { isPrimary: false },
    })
  expect(craInfo.find('[data-cy="form-section-cra-info"]').exists()).toBe(true)
  expect(craInfo.find(`[placeholder="${t('create-account.contact-form.socialInsuranceNumberOptional')}"]`).exists()).toBe(true)
})


