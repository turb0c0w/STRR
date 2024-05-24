<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="mb-[180px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <UForm :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress :form-state="formState.propertyDetails" />
        <BcrosFormSectionPropertyDetails :form-state="formState.propertyDetails" />
        <BcrosFormSectionPropertyListingDetails :form-state="formState.propertyDetails" />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

</script>
