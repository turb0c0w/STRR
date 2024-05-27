<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput
            v-model="parcelIdentifier"
            :placeholder="t('create-account.property-form.parcelIdentifier')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput
            v-model="businessLicense"
            :placeholder="t('create-account.property-form.businessLicense')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="propertyType" class="pr-[16px] flex-grow">
          <USelect
            v-model="propertyType"
            :placeholder="t('create-account.property-form.propertyType')"
            :options="propertyTypes"
            option-attribute="name"
            class="w-full"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <USelect
            v-model="ownershipType"
            :placeholder="t('create-account.property-form.ownershipType')"
            :options="ownershipTypes"
            option-attribute="name"
            class="w-full"
          />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

const propertyType = defineModel<string>('propertyType')
const ownershipType = defineModel<string>('ownershipType')
const businessLicense = defineModel<string>('businessLicense')
const parcelIdentifier = defineModel<string>('parcelIdentifier')

const {
  propertyTypes,
  ownershipTypes
} = defineProps<{
  propertyTypes: string[],
  ownershipTypes: string[]
}>()
</script>
