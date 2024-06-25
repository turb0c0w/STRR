<template>
  <div
    :class="
      `
        ${single ? 'flex-1': ''}
        mb-[42px] mobile:mb-[24px] justify-between flex-col
        bg-white px-[30px] mobile:px-[8px] py-[22px]
        border-[2px] border-bcGovColor-hairlinesOnWhite
      `
    "
  >
    <BcrosChip :flavour="flavour" class="mobile:hidden">
      {{ tRegistrationStatus(status) }}
    </BcrosChip>
    <div class="flex w-full justify-between">
      <slot />
      <BcrosChip :flavour="flavour" class="desktop:hidden">
        {{ tRegistrationStatus(status) }}
      </BcrosChip>
    </div>
    <div class="flex flex-row text-bcGovColor-activeBlue justify-start">
      <p class="mr-[22px] cursor-pointer">
        {{ tRegistrationStatus('view') }}
      </p>
      <p class="mr-[22px] cursor-pointer">
        {{ tRegistrationStatus('download') }}
      </p>
      <p class="cursor-pointer">
        {{ tRegistrationStatus('renewal') }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'

const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)

const {
  single,
  status,
  flavour
} = defineProps<{
  single: boolean,
  status: string,
  flavour: AlertsFlavourE
}>()
</script>
