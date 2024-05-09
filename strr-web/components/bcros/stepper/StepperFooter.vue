<template>
  <div class="absolute w-screen left-[-55px] bottom-[-75px] bg-white h-[120px] flex items-center pl-[70px]">
    <BcrosButtonsPrimary
      :text="t('general.back')"
      :action="setPreviousStep"
      icon="i-mdi-chevron-left"
      :trailing="false"
      variant="outline"
      :class-name="`${isFirstStep ? 'hidden': ''} mr-[20px]`"
    />
    <BcrosButtonsPrimary
      :text="isLastStep ? t('general.submit') : t('general.next')"
      :action="setNextStep"
      :icon="isLastStep ? '': 'i-mdi-chevron-right'"
      :trailing="true"
    />
  </div>
</template>

<script setup lang="ts">

const {
  isFirstStep,
  isLastStep,
  setNextStep,
  setPreviousStep
} = defineProps<{
  isFirstStep: boolean,
  isLastStep: boolean,
  setNextStep:() => void,
  setPreviousStep:() => void
}>()

const t = useNuxtApp().$i18n.t

</script>
