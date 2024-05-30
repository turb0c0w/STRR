<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.dateOfBirth')" :optional="dobOptional">
      <div class="flex flex-row justify-between w-full mobile:flex-col">
        <UFormGroup name="birthDay" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput
            v-model="day"
            :placeholder="t('create-account.contact-form.day')"
            aria-label="birth day"
          />
        </UFormGroup>
        <UFormGroup name="month" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
          <USelect
            v-model="month"
            :placeholder="t('create-account.contact-form.month')"
            :options="getMonths()"
            option-attribute="key"
            class="w-full"
            aria-label="birth month"
            style="color: #1a202c; /* text-gray-900 */ dark:text-white; /* Override with dark mode text color */"
          />
        </UFormGroup>
        <UFormGroup name="birthYear">
          <UInput v-model="year" :placeholder="t('create-account.contact-form.year')" aria-label="birth year" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

const {
  dobOptional
} = defineProps<{
  dobOptional?: boolean
}>()

const day = defineModel<string>('day')
const month = defineModel<string>('month')
const year = defineModel<string>('year')

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
