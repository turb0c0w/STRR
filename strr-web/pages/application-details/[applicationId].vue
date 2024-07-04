<template>
  <div>
    <BcrosBanner>
      <div class="flex items-center">
        <BcrosTypographyH1
          :text="`${application?.unitAddress.nickname ? application?.unitAddress.nickname + ' ' : ''}REGISTRATION #${applicationId}`"
          class-name="pb-[0px]"
        />
        <BcrosChip v-if="flavour" :flavour="flavour" class="ml-[16px]">
          {{ flavour.text }}
        </BcrosChip>
      </div>
    </BcrosBanner>
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'

const route = useRoute()
const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)

const { applicationId } = route.params

const { getRegistration } = useRegistrations()

const application = await getRegistration(applicationId.toString())

const getFlavour = (status: string, invoices: RegistrationI['invoices']):
  { alert: AlertsFlavourE, text: string } | undefined => {
  if (status === 'PENDING' && invoices[0].payment_status_code === 'COMPLETED') {
    return {
      text: tRegistrationStatus('applied'),
      alert: AlertsFlavourE.APPLIED
    }
  }
  if (status === 'PENDING' && invoices[0].payment_status_code !== 'COMPLETED') {
    return {
      text: tRegistrationStatus('payment-due'),
      alert: AlertsFlavourE.WARNING
    }
  }
}

console.log(application)
const flavour = application ? getFlavour(application.status, application.invoices) : null
console.log(flavour)
</script>
