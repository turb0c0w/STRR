<template>
  <div>
    <BcrosTypographyH1 text="Selected Account Details" data-cy="formTestTitle" class="mobile:pb-[20px]" />
    <p>Name: {{ selectedAccount.name }}</p><br>
    <BcrosTypographyH1 text="Test Form" data-cy="formTestTitle" class="mobile:pb-[20px]" />
    <BcrosTypographyH1 text="Primary Address" data-cy="formTestTitle" class="mobile:pb-[20px]" />
    <UForm :schema="schema" :state="primaryAddress" class="space-y-4" @submit="onSubmit">
      <UFormGroup label="Primary Street">
        <UInput
          id="primary_street"
          v-model="primaryAddress.street"
          placeholder="Type your address"
          @keypress.once="enablePrimaryAddressComplete('primary', 'CAN')"
          @click="enablePrimaryAddressComplete('primary', 'CAN')"
        />
      </UFormGroup>
      <UFormGroup label="City" name="city">
        <UInput v-model="primaryAddress.city" />
      </UFormGroup>
      <UFormGroup label="Province/State/Region" name="region">
        <UInput v-model="primaryAddress.region" />
      </UFormGroup>
      <UFormGroup label="Country" name="country">
        <UInput v-model="primaryAddress.country" />
      </UFormGroup>
      <UFormGroup label="Postal or Zip Code" name="postalCode">
        <UInput v-model="primaryAddress.postalCode" />
      </UFormGroup>
      <BcrosTypographyH1 text="Secondary Address" data-cy="formTestTitle" class="mobile:pb-[20px]" />
      <UFormGroup label="Secondary Street">
        <UInput
          id="secondary_street"
          v-model="secondaryAddress.street"
          placeholder="Type your address"
          @keypress.once="enableSecondaryAddressComplete('secondary', 'CAN')"
          @click="enableSecondaryAddressComplete('secondary', 'CAN')"
        />
      </UFormGroup>
      <UFormGroup label="City" name="city">
        <UInput v-model="secondaryAddress.city" />
      </UFormGroup>
      <UFormGroup label="Province/State/Region" name="region">
        <UInput v-model="secondaryAddress.region" />
      </UFormGroup>
      <UFormGroup label="Country" name="country">
        <UInput v-model="secondaryAddress.country" />
      </UFormGroup>
      <UFormGroup label="Postal or Zip Code" name="postalCode">
        <UInput v-model="secondaryAddress.postalCode" />
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

const { selectedAccount } = formState

const { address: primaryAddress, enableAddressComplete: enablePrimaryAddressComplete } = useCanadaPostAddress()
const { address: secondaryAddress, enableAddressComplete: enableSecondaryAddressComplete } = useCanadaPostAddress()

const schema = z.object({
  street: z.string().min(1, 'Street is required'),
  city: z.string().min(1, 'City is required'),
  region: z.string().min(1, 'Province/State/Region is required'),
  country: z.string().min(1, 'Country is required'),
  postalCode: z.string().min(1, 'Postal code or Zip code is required')
})

type Schema = z.output<typeof schema>

function onSubmit (event: FormSubmitEvent<Schema>) {
  alert(JSON.stringify(event.data))
}
</script>
