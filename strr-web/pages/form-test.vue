<template>
  <div>
    <BcrosTypographyH1 text="Selected Account Details" data-cy="formTestTitle" class="mobile:pb-[20px]" />
    <p>Name: {{ selectedAccount.name }}</p><br>
    <BcrosTypographyH1 text="Test Form" data-cy="formTestTitle" class="mobile:pb-[20px]" />
    <UForm :schema="schema" :state="address" class="space-y-4" @submit="onSubmit">
      <UFormGroup label="Street" name="street">
        <UInput
          v-model="address.street"
          placeholder="Type your address"
          @keypress.once="enableAddressComplete()"
          @click="enableAddressComplete()"
        />
      </UFormGroup>
      <UFormGroup label="City" name="city">
        <UInput v-model="address.city" />
      </UFormGroup>
      <UFormGroup label="Province/State/Region" name="region">
        <UInput v-model="address.region" />
      </UFormGroup>
      <UFormGroup label="Country" name="country">
        <UInput v-model="address.country" />
      </UFormGroup>
      <UFormGroup label="Postal or Zip Code" name="postalCode">
        <UInput v-model="address.postalCode" />
      </UFormGroup>
      <UButton type="submit">
        Submit
      </UButton>
    </UForm>
  </div>
</template>

<script setup lang="ts">

import type { FormSubmitEvent } from '#ui/types'
import { z } from 'zod'
import { formState } from '@/stores/strr'
import { CanadaPostAddressI, CanadaPostResponseAddressI } from '#imports'

const { selectedAccount } = formState

// TODO: TC - this probably lives in the store?
const address = reactive<CanadaPostAddressI>({
  street: '',
  streetAdditional: '',
  city: '',
  region: '',
  postalCode: '',
  country: '',
  deliveryInstructions: ''
})

// TODO: TC - this probably lives in the store?
const schema = z.object({
  street: z.string().min(1, 'Street is required'),
  city: z.string().min(1, 'City is required'),
  region: z.string().min(1, 'Province/State/Region is required'),
  country: z.string().min(1, 'Country is required'),
  postalCode: z.string().min(1, 'Postal code or Zip code is required')
})

type Schema = z.output<typeof schema>

// TODO: TC - move the following canada post address related things to a simple composable
const createAddressComplete = (pca: any, key: string): object => {
  const fields = [
    { element: 'street', field: 'Line1', mode: pca.fieldMode.SEARCH },
    { element: 'CA', field: 'CountryName', mode: pca.fieldMode.COUNTRY }
  ]
  const options = { key }
  const addressComplete = new pca.Address(fields, options)
  addressComplete.listen('populate', addressCompletePopulate)
  return addressComplete
}

const enableAddressComplete = (): void => {
  const config = useRuntimeConfig()
  // TODO: TC - Maybe there is a better way to do this than using window like PPR :)
  const pca = (window as any).pca
  const key = config.public.addressCompleteKey
  if (!pca || !key) {
    // eslint-disable-next-line no-console
    console.log('AddressComplete not initialized due to missing script and/or key')
    return
  }
  // Destroy the old object if it exists, and create a new one.
  // TODO: TC - Maybe there is a better way to do this than using window like PPR :)
  if ((window as any).currentAddressComplete) {
    (window as any).currentAddressComplete.destroy()
  }
  (window as any).currentAddressComplete = createAddressComplete(pca, key)
}

const addressCompletePopulate = (addressComplete: CanadaPostResponseAddressI): void => {
  address.street = addressComplete.Line1 || 'N/A'
  address.city = addressComplete.City
  address.region = addressComplete.ProvinceCode
  address.postalCode = addressComplete.PostalCode
  address.country = addressComplete.CountryName
}

function onSubmit (event: FormSubmitEvent<Schema>) {
  alert(JSON.stringify(event.data))
}

</script>
