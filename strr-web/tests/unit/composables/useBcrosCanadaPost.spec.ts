// @vitest-environment nuxt
import { it, expect } from 'vitest'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import { createI18n } from 'vue-i18n'
import { BcrosTypographyH1 } from '#components'

const i18n = createI18n({
  // vue-i18n options here ...
})

it('begins with empty address', async () => {
  const {
    activeAddressField,
    address,
    enableAddressComplete
  } = useCanadaPostAddress()

  expect(address.street).toEqual('')
  expect(address.streetAdditional).toEqual('')
  expect(address.city).toEqual('')
  expect(address.region).toEqual('')
  expect(address.postalCode).toEqual('')
  expect(address.country).toEqual('')
  expect(address.deliveryInstructions).toEqual('')
})

it('sets the active address field', async () => {
  const {
    activeAddressField,
    enableAddressComplete
  } = useCanadaPostAddress()

  const id = 'id'
  const countryIso2 = 'CA'
  const countrySelect = true

  enableAddressComplete(id, countryIso2, countrySelect)

  expect(activeAddressField.value).toEqual(id)
})
