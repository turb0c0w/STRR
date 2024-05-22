<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.dateOfBirth')" :optional="dobOptional">
      <div class="flex flex-row justify-between w-full mobile:flex-col">
        <UFormGroup name="day" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="day" :placeholder="t('create-account.contact-form.day')" />
        </UFormGroup>
        <UFormGroup name="month" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="month" :placeholder="t('create-account.contact-form.month')" />
        </UFormGroup>
        <UFormGroup name="year" class="pr-[16px]">
          <UInput v-model="year" :placeholder="t('create-account.contact-form.year')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const { formState, dobOptional } = defineProps<{ formState: any, dobOptional: boolean }>();

const { dateOfBirth: { day, month, year } } = formState
const t = useNuxtApp().$i18n.t

</script>
