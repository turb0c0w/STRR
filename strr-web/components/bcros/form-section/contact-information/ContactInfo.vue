<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.dateOfBirth')" :optional="dobOptional">
      <div class="flex flex-row justify-between w-full mobile:flex-col">
        <UFormGroup name="birthDay" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model.number="formState.birthDay" :placeholder="t('create-account.contact-form.day')" />
        </UFormGroup>
        <UFormGroup name="month" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UDropdown
            :items="months"
            class="w-full"
            :label="t('create-account.contact-form.month')"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              class="w-full"
              color="white"
              trailing-icon="i-heroicons-chevron-down-20-solid"
              :placeholder="t('create-account.contact-form.month')"
              v-model="formState.birthMonth"
            />
          </UDropdown>
        </UFormGroup>
        <UFormGroup name="birthYear">
          <UInput v-model.number="formState.birthYear" :placeholder="t('create-account.contact-form.year')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'

const { formState, dobOptional } = defineProps<{ formState: any, dobOptional?: boolean }>()

const t = useNuxtApp().$i18n.t

const months: DropdownItem[][] = [
  [
    {
      label: t('general.february'),
      click: () => formState.month = t('general.february')
    },
    {
      label: t('general.march'),
      click: () => formState.month = t('general.march')
    },
    {
      label: t('general.january'),
      click: () => formState.month = t('general.january')
    },
    {
      label: t('general.april'),
      click: () => formState.month = t('general.april')
    },
    {
      label: t('general.may'),
      click: () => formState.month = t('general.may')
    },
    {
      label: t('general.june'),
      click: () => formState.month = t('general.june')
    },
    {
      label: t('general.july'),
      click: () => formState.month = t('general.july')
    },
    {
      label: t('general.august'),
      click: () => formState.month = t('general.august')
    },
    {
      label: t('general.september'),
      click: () => formState.month = t('general.september')
    },
    {
      label: t('general.october'),
      click: () => formState.month = t('general.october')
    },
    {
      label: t('general.november'),
      click: () => formState.month = t('general.november')
    },
    {
      label: t('general.december'),
      click: () => formState.month = t('general.december')   
    }
  ]
]

</script>
