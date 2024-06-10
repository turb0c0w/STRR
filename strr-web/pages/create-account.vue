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
              <p v-if="activeStep.subtitle" class="mb-[32px]">
                {{ t(activeStep.subtitle) }}
              </p>
            </div>
            <div v-if="activeStepIndex === 0" :key="activeStepIndex">
              <BcrosFormSectionContactInformationForm
                ref="contactForm"
                :full-name="userFullName"
                :add-secondary-contact="addSecondaryContact"
                :toggle-add-secondary="toggleAddSecondary"
                :is-complete="activeStep.step.complete"
                :second-form-is-complete="activeStep.step.complete"
              />
            </div>
            <div v-if="activeStepIndex === 1" :key="activeStepIndex">
              <BcrosFormSectionPropertyForm :is-complete="activeStep.step.complete" />
            </div>
            <div v-if="activeStepIndex === 2" :key="activeStepIndex">
              <BcrosFormSectionPrincipalResidenceForm :is-complete="steps[activeStepIndex].step.complete" />
            </div>
            <div v-if="activeStepIndex === 3" :key="activeStepIndex">
              <BcrosFormSectionReviewForm :secondary-contact="addSecondaryContact" @toggle-valid="toggleValid" />
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
const tPrincipalResidence = (translationKey: string) => t(`create-account.principal-residence.${translationKey}`)
const contactForm = ref()
const isFinalStepValid = ref(false)

const toggleValid = () => { isFinalStepValid.value = !isFinalStepValid.value }

const t = useNuxtApp().$i18n.t
const {
  currentAccount,
  userFullName,
  userFirstName,
  userLastName
} = useBcrosAccount()

const toggleAddSecondary = () => { addSecondaryContact.value = !addSecondaryContact.value }

const propertyToApiType = (type: string | undefined): string => {
  switch (type) {
    case (t('create-account.property-form.primaryDwelling')):
      return 'PRIMARY'
    case (t('create-account.property-form.secondarySuite')):
      return 'SECONDARY'
    case (t('create-account.property-form.accessory')):
      return 'ACCESSORY'
    case (t('create-account.property-form.float')):
      return 'FLOAT_HOME'
    case (t('create-account.property-form.other')):
      return 'OTHER'
  }
  return ''
}

const ownershipToApiType = (type: string | undefined): string => {
  switch (type) {
    case (t('create-account.property-form.rent')):
      return 'RENT'
    case (t('create-account.property-form.own')):
      return 'OWN'
    case (t('create-account.property-form.other')):
      return 'CO_OWN'
  }
  return ''
}

const submit = () => submitCreateAccountForm(
  userFirstName,
  userLastName,
  currentAccount.id,
  addSecondaryContact.value,
  propertyToApiType(formState.propertyDetails.propertyType),
  ownershipToApiType(formState.propertyDetails.ownershipType)
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
  }
})

watch(formState.principal, () => {
  if (formState.principal.isPrincipal &&
    formState.principal.consent &&
    formState.principal.declaration
  ) {
    setStepValid(2, true)
  }
  if (!formState.principal.isPrincipal &&
    formState.principal.reason &&
    formState.principal.reason !== tPrincipalResidence('other')
  ) {
    setStepValid(2, true)
  }
  if (!formState.principal.isPrincipal &&
    formState.principal.reason &&
    formState.principal.otherReason
  ) {
    setStepValid(2, true)
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
  }
}

definePageMeta({
  layout: 'wide'
})

</script>
