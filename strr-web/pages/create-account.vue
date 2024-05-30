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
                ref="contactForm"
                :full-name="userFullName"
                :add-secondary-contact="addSecondaryContact"
                :toggle-add-secondary="toggleAddSecondary"
              />
            </div>
            <div v-if="activeStepIndex === 1" :key="activeStepIndex">
              <BcrosFormSectionPropertyForm />
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
import steps from '../page-data/create-account/steps'
import { FormPageI } from '~/interfaces/form/form-page-i'

const addSecondaryContact: Ref<boolean> = ref(false)
const activeStepIndex: Ref<number> = ref(0)
const activeStep: Ref<FormPageI> = ref(steps[activeStepIndex.value])
const contactForm = ref();

const t = useNuxtApp().$i18n.t
const {
  currentAccount,
  userFullName,
  userFirstName,
  userLastName
} = useBcrosAccount()

const toggleAddSecondary = () => { addSecondaryContact.value = !addSecondaryContact.value }

const submit = () => submitCreateAccountForm(
  userFirstName,
  userLastName,
  userFullName,
  currentAccount.mailingAddress,
  addSecondaryContact.value
)

const setActiveStep = (newStep: number) => {
  activeStepIndex.value = newStep
  activeStep.value = steps[activeStepIndex.value]
}

const setStepValid = (index: number, valid: boolean) => {
  steps[index].step.isValid = valid
}

watch(formState.primaryContact, () => {
  if (contactSchema.safeParse(formState.primaryContact).success) {
    setStepValid(0, true)
  }
})

watch(formState.secondaryContact, () => {
  if (contactSchema.safeParse(formState.secondaryContact).success) {
    setStepValid(0, true)
  }
})

watch(formState.propertyDetails, () => {
  const parsed = propertyDetailsSchema.safeParse(formState.propertyDetails)
  if (parsed.success) {
    setStepValid(1, true)
  } else {
    //example
    console.log(parsed.error.flatten().fieldErrors);
    console.log(formState.propertyDetails)
  }
})

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
    if (nextStep == 0) {
      //example
      console.log(contactForm)
      contactForm.value.validate()
    }
  }
}

definePageMeta({
  layout: 'wide'
})

</script>
