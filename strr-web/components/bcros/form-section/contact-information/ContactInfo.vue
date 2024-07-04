<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.dateOfBirth')" :optional="!isPrimary">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="birthDay" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput
            v-model="day"
            :placeholder="t('create-account.contact-form.day')"
            aria-label="birth day"
          />
        </UFormGroup>
        <UFormGroup name="month" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]" :error="monthError">
          <USelect
            v-model="month"
            :placeholder="t('create-account.contact-form.month')"
            :options="getMonths()"
            option-attribute="key"
            class="w-full"
            aria-label="birth month"
            style="color: #1a202c; /* text-gray-900 */ dark:text-white; /* Override with dark mode text color */"
            @blur="isPrimary ? emit('validateMonths'): null"
            @change="isPrimary ? emit('validateMonths'): null"
          />
        </UFormGroup>
        <UFormGroup name="birthYear">
          <UInput v-model="year" :placeholder="t('create-account.contact-form.year')" aria-label="birth year" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="socialInsuranceNumber" class=" flex-grow">
          <UInput
            v-model="socialInsuranceNumber"
            type="text"
            aria-label="social insurance number"
            :placeholder="t('create-account.contact-form.socialInsuranceNumber')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mobile:flex-col">
        <UFormGroup name="businessNumber" class=" flex-grow">
          <UInput
            v-model="businessNumber"
            type="text"
            aria-label="business number"
            :placeholder="t('create-account.contact-form.businessNumber')"
          />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

const {
  isPrimary,
  monthError
} = defineProps<{
  isPrimary?: boolean
  monthError?: string
}>()

const day = defineModel<string>('day')
const month = defineModel<string>('month')
const year = defineModel<string>('year')
const socialInsuranceNumber = defineModel<string>('socialInsuranceNumber')
const businessNumber = defineModel<string>('businessNumber')

watch(socialInsuranceNumber, (input: string | undefined) => {
  if (input) {
    console.log(input.length)
    if (input.length >= 3 && !(input.length >= 7)) { 
      socialInsuranceNumber.value = `${input.slice(0, 3)} ` 
    }
    if (input.length >= 7) { 
      socialInsuranceNumber.value = `${input.slice(0, 3)} ${input.slice(3, 8)} ${input.slice(8, 11)}`
    }
  }
})

const emit = defineEmits(['validateMonths'])

const months: string[] = [
  t('general.january'),
  t('general.february'),
  t('general.march'),
  t('general.april'),
  t('general.may'),
  t('general.june'),
  t('general.july'),
  t('general.august'),
  t('general.september'),
  t('general.october'),
  t('general.november'),
  t('general.december')
]

const getMonths = (): { key: string, value: string }[] => months.map((month: string, index: number) => ({
  value: (index + 1).toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false }),
  key: month
}))

</script>
