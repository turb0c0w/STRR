<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput :on-change="changeParcelIdentifier" :placeholder="t('create-account.property-form.parcelIdentifier')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput :on-change="changeBusinessLicense" :placeholder="t('create-account.property-form.businessLicense')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="propertyType" class="pr-[16px] flex-grow">
          <UDropdown
            :items="propertyTypes"
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              :model-value="formState.propertyType"
              class="w-full"
              color="white"
              :placeholder="t('create-account.property-form.propertyType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <UDropdown
            :items="ownershipTypes"
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              :model-value="formState.ownershipType"
              class="w-full"
              color="white"
              :placeholder="t('create-account.property-form.ownershipType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'

const { formState } = defineProps<{ formState: any }>()

const propertyType = ref<string>()
const ownershipType = ref<string>()
const businessLicense = ref<string>()
const parcelIdentifier = ref<string>()

const emit = defineEmits<{
  changePropertyType: [propertyType: string],
  changeOwnershipType: [ownershipType: string],
  changeBusinessLicense: [businessLicense: string],
  changeParcelIdentifier: [parcelIdentifier: string],
}>()

const changeBusinessLicense = (inputBusinessLicense: string) => {
  businessLicense.value = inputBusinessLicense
}

const changeParcelIdentifier = (inputParcelIdentifier: string) => {
  parcelIdentifier.value = inputParcelIdentifier
}

const t = useNuxtApp().$i18n.t

const propertyTypes: DropdownItem[][] = [
  [
    {
      label: t('create-account.property-form.primaryDwelling'),
      click: () => { propertyType.value = t('create-account.property-form.primaryDwelling') }
    },
    {
      label: t('create-account.property-form.secondarySuite'),
      click: () => { propertyType.value = t('create-account.property-form.secondarySuite') }
    },
    {
      label: t('create-account.property-form.accessory'),
      click: () => { propertyType.value = t('create-account.property-form.accessory') }
    },
    {
      label: t('create-account.property-form.float'),
      click: () => { propertyType.value = t('create-account.property-form.float') }
    },
    {
      label: t('create-account.property-form.other'),
      click: () => { propertyType.value = t('create-account.property-form.other') }
    }
  ]
]

const ownershipTypes: DropdownItem[][] = [
  [
    {
      label: t('create-account.property-form.rent'),
      click: () => { ownershipType.value = t('create-account.property-form.rent') }
    },
    {
      label: t('create-account.property-form.own'),
      click: () => { ownershipType.value = t('create-account.property-form.own') }
    },
    {
      label: t('create-account.property-form.other'),
      click: () => { ownershipType.value = t('create-account.property-form.coown') }
    }
  ]
]

</script>
