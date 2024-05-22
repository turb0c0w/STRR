<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.internetListingDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="urlOne" class="pr-[16px] flex-grow">
          <UInput v-model="urlOne" placeholder="Platform URL" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="urlTwo" class="pr-[16px] flex-grow">
          <UInput v-model="urlTwo" placeholder="Platform URL 2" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const {
  listingDetails: {
    urlOne,
    urlTwo
  }
} = formState
const t = useNuxtApp().$i18n.t

</script>
