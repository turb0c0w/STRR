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
            <div v-if="activeStepIndex === 0" :key="activeStepIndex">
              <BcrosFormSectionContactInformationForm
                :on-validate-page="(isValid) => setStepValid(0, isValid)"
                :full-name="userFullName"
              />
            </div>
            <div v-if="activeStepIndex === 1" :key="activeStepIndex">
              <BcrosFormSectionPropertyForm
                :on-validate-page="(isValid) => setStepValid(1, isValid)"
              />
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
        :submit="submit"
        :is-last-step="activeStepIndex.valueOf() == steps.length - 1"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import steps from '../page-data/create-account/steps'
import { FormPageI } from '~/interfaces/form/form-page-i'
import { CreateAccountFormAPII } from '~/interfaces/account-i';
const activeStepIndex: Ref<number> = ref(0)
const activeStep: Ref<FormPageI> = ref(steps[activeStepIndex.value])

const t = useNuxtApp().$i18n.t
const { currentAccount, userFullName, userFirstName, userLastName } = useBcrosAccount()

const apiURL = useRuntimeConfig().public.authApiURL

const submit = async () => {
    const formData: CreateAccountFormAPII = formStateToApi(
      formState,
      userFirstName,
      userLastName,
      userFullName,
      currentAccount.mailingAddress
    )
    
    await axios.post<CreateAccountFormAPII>(`${apiURL}/account`)
      .then((response) => {
        const data = response?.data
        if (!data) { throw new Error('Invalid AUTH API response') }
        return data
      })
      .catch((error: string) => {
        console.warn('Error creating account.')
        console.error(error);
      })
  }

const setActiveStep = (newStep: number) => {
  activeStepIndex.value = newStep
  activeStep.value = steps[activeStepIndex.value]
}

const setStepValid = (index: number, valid: boolean) => {
  steps[index].step.isValid = valid
}

const setNextStep = () => {
  if (activeStepIndex.value < steps.length - 1) {
    const nextStep = activeStepIndex.value + 1
    activeStepIndex.value = nextStep
    activeStep.value = steps[activeStepIndex.value]
    steps[activeStepIndex.value - 1].step.complete = true
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
