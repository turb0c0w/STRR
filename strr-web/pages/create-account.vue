<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="w-full h-full flex flex-row mobile:flex-col">
      <div class="grow pr-[24px] mobile:pr-[0px]">
        <BcrosTypographyH1 text="create-account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
        <BcrosStepper :active-step="activeStep" :set-active-step="setActiveStep" :steps="steps" />
      </div>
      <div class="shrink mobile:grow">
        <BcrosFeeWidget />
      </div>
    </div>
    <BcrosStepperFooter
      :key="activeStep"
      :is-first-step="activeStep.valueOf() == 0"
      :set-next-step="setNextStep"
      :set-previous-step="setPreviousStep"
      :is-last-step="activeStep.valueOf() == steps.length - 1"
    />
  </div>
</template>

<script setup lang="ts">
import steps from '../page-data/create-account/steps'
const activeStep: Ref<number> = ref(0)

const setActiveStep = (newStep: number) => {
  activeStep.value = newStep
}

const setNextStep = () => {
  if (activeStep.value < steps.length - 1) {
    const nextStep = activeStep.value + 1
    activeStep.value = nextStep
  }
}

const setPreviousStep = () => {
  if (activeStep.value > 0) {
    const nextStep = activeStep.value - 1
    activeStep.value = nextStep
  }
}

definePageMeta({
  layout: 'wide'
})

</script>
