<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.dateOfBirth')" :optional="dobOptional">
      <div class="flex flex-row justify-between w-full mobile:flex-col">
        <UFormGroup name="birthDay" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput :model-value="day" :placeholder="t('create-account.contact-form.day')" />
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
              :model-value="month"
              class="w-full"
              color="white"
              trailing-icon="i-heroicons-chevron-down-20-solid"
              :placeholder="t('create-account.contact-form.month')"
            />
          </UDropdown>
        </UFormGroup>
        <UFormGroup name="birthYear">
          <UInput :model-value="year" :placeholder="t('create-account.contact-form.year')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'

const t = useNuxtApp().$i18n.t

const { 
  day,
  month,
  year,
  months,
  dobOptional
} = defineProps<{
  day: number | undefined,
  month: string | undefined,
  year: number | undefined
  months: DropdownItem[][],
  dobOptional?: boolean
}>()


const emit = defineEmits<{
  setDay: [day: number],
  setMonth: [month: string],
  setYear: [day: number],
}>()

</script>
