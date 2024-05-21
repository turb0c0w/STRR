<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="mb-[32px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <BcrosFormSection title="Hello">
        <div class="mb-[16px] text-[14px] leading-[22px]">
          {{ t('create-account.contact.primary') }}
        </div>
      </BcrosFormSection>
      <BcrosFormSectionContactInformationContactInfo :primary="true" />
      <BcrosFormSectionContactInformationContactDetails :primary="true" />
      <BcrosFormSectionContactInformationMailingAddress :primary="true" />
    </div>
    <div class="mb-[180px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <BcrosFormSectionContactInformationContactInfo :primary="false" />
      <BcrosFormSectionContactInformationContactDetails :primary="false" />
      <BcrosFormSectionContactInformationMailingAddress :primary="false" />
    </div>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

</script>
