<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="w-full flex flex-col justify-between">
      <div class="shrink w-full flex flex-row mobile:flex-col justify-between">
        <div class="grow pr-[24px] mobile:pr-[0px]">
          <div class="mobile:px-[8px]">
            <BcrosTypographyH1 text="create-account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
            <BcrosStepper :active-step="activeStepIndex" :set-active-step="setActiveStep" :steps="steps" />
          </div>
          <div :key="activeStepIndex" class="grow">
            <div class="mobile:px-[8px]">
              <BcrosTypographyH2 :text="t(activeStep.title)" class="py-[32px]" />
              <p class="mb-[32px]">
                {{ t(activeStep.subtitle) }}
              </p>
            </div>
            <div class="h-[1254px] mb-[180px] bg-white rounded-[4px]">
              <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
                <p class="px-[40px] py-[15px] font-bold">
                  {{ t(activeStep.formTitle) }}
                </p>
              </div>
              <div v-for="formSection in activeStep.sections" :key="formSection.title">
                <div class="ml-[40px]">
                  <BcrosFormSection :title="formSection.title">
                    <div v-for="field in formSection.fields" :key="field.content">
                      <div class="mb-[16px]">
                        {{ t(field.content) }}
                      </div>
                    </div>
                  </BcrosFormSection>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="shrink mobile:grow">
          <BcrosFeeWidget />
        </div>
      </div>
      <BcrosStepperFooter
        :key="activeStepIndex"
        :is-first-step="activeStepIndex.valueOf() == 0"
        :set-next-step="setNextStep"
        :set-previous-step="setPreviousStep"
        :is-last-step="activeStepIndex.valueOf() == steps.length - 1"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import steps from '../page-data/create-account/steps'
import { FormPageI } from '~/interfaces/form/form-page-i'
const activeStepIndex: Ref<number> = ref(0)
const activeStep: Ref<FormPageI> = ref(steps[activeStepIndex.value])

const t = useNuxtApp().$i18n.t

const setActiveStep = (newStep: number) => {
  activeStepIndex.value = newStep
  activeStep.value = steps[activeStepIndex.value]
}

const setNextStep = () => {
  if (activeStepIndex.value < steps.length - 1) {
    const nextStep = activeStepIndex.value + 1
    activeStepIndex.value = nextStep
    activeStep.value = steps[activeStepIndex.value]
  }
}

const setPreviousStep = () => {
  if (activeStepIndex.value > 0) {
    const nextStep = activeStepIndex.value - 1
    activeStepIndex.value = nextStep
    activeStep.value = steps[activeStepIndex.value]
  }
}

definePageMeta({
  layout: 'wide'
})

</script>
