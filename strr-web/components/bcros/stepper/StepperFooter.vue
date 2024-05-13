<template>
  <div
    class="
      bg-white h-[120px] flex items-center
      d:w-screen d:absolute d:left-[-55px] d:bottom-[-75px] d:pl-[70px] d:bottom-[0px]
      m:relative m:px-[8px]
    "
    data-cy="stepper-footer"
  >
    <BcrosButtonsPrimary
      :text="t('general.back')"
      :action="setPreviousStep"
      icon="i-mdi-chevron-left"
      :trailing="false"
      variant="outline"
      :class-name="`${isFirstStep ? 'hidden': ''} mr-[20px] mobile:mr-[8px]`"
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
