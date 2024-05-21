<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection title="Date of Birth">
      <div class="flex flex-row justify-between w-full">
        <UFormGroup name="day" class="pr-[16px] flex-grow">
          <UInput v-model="day" placeholder="Day" />
        </UFormGroup>
        <UFormGroup name="month" class="pr-[16px] flex-grow">
          <UInput v-model="month" placeholder="Month" />
        </UFormGroup>
        <UFormGroup name="year" class="pr-[16px]">
          <UInput v-model="year" placeholder="Year" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const { dateOfBirth: { day, month, year } } = formState
const t = useNuxtApp().$i18n.t

</script>
