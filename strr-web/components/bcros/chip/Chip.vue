<template>
  <div
    :class="
      `
        ${flavourClass}
        mb-[24px] font-bold px-[12px] py-[4px] flex-shrink flex h-fit w-fit rounded
      `
    "
  >
    <slot />
  </div>
</template>

<script setup lang="ts">

import { AlertsFlavourE } from '~/enums/alerts-e'

const { flavour } = defineProps<{
  flavour: {
    alert: AlertsFlavourE,
    text: string
  }
}>()

const flavourClass = ref('')

switch (flavour.alert) {
  case AlertsFlavourE.ALERT:
    flavourClass.value = 'text-red-500 bg-red-100'
    break
  case AlertsFlavourE.SUCCESS:
    flavourClass.value = 'bg-green-100'
    break
  case AlertsFlavourE.WARNING:
    flavourClass.value = 'text-[#6c4a00] bg-[#f9f1c6]'
    break
  case AlertsFlavourE.INFO:
    flavourClass.value = 'text-orange-500 bg-yellow-50'
    break
  case AlertsFlavourE.APPLIED:
    flavourClass.value = 'text-[#313132] bg-[#d9eaf7]'
    break
  case AlertsFlavourE.MESSAGE:
    flavourClass.value = ''
    break
}

</script>
