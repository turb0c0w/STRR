<template>
  <div>
    <div>
      <BcrosBanner hide-buttons>
        <div class="flex items-center m:justify-between">
          <BcrosTypographyH1
            :text="
              `${
                application?.unitAddress.nickname
                  ? application?.unitAddress.nickname + ' '
                  : ''}REGISTRATION #${applicationId}
                `
            "
            class-name="mobile:text-[24px]"
            no-spacing
          />
          <BcrosChip v-if="flavour" :flavour="flavour" class="ml-[16px]">
            {{ flavour.text }}
          </BcrosChip>
        </div>
      </BcrosBanner>
    </div>
    <div class="mt-[104px] m:mt-[74px]">
      <div>
        <p class="font-bold mb-[24px] mobile:mx-[8px]">
          Automatic Approval Logic
        </p>
        <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
          <div class="flex flex-col justify-between w-full mobile:flex-col">
            <UTable :rows="automaticRows" />
          </div>
        </div>
      </div>
      <div class="mt-[40px]">
        <div>
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            Provisional Approval Logic
          </p>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
            <div class="flex flex-col justify-between w-full mobile:flex-col">
              <UTable :rows="provisionalRows" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'
import { AutoApprovalDataI } from '~/interfaces/auto-approval-data-i'

const route = useRoute()
const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)

const { applicationId } = route.params

const { getRegistration, getAutoApproval } = useRegistrations()

const application = await getRegistration(applicationId.toString())

const data: AutoApprovalDataI[] = await getAutoApproval(applicationId.toString()) || {} as AutoApprovalDataI[]

const automaticRows = [
  {
    criteria: 'Renting',
    outcome: data[0].record.renting ? 'Yes' : 'No'
  },
  {
    criteria: 'Accommodation Service Provider Selected',
    outcome: data[0].record.service_provider ? 'Yes' : 'No'
  },
  {
    criteria: 'Principal Residence Exempt',
    outcome: data[0].record.pr_exempt
      ? 'PR Exempt'
      : data[0].record.pr_exempt === false
        ? 'Not PR Exempt'
        : 'Address Look Up Service Failed'
  }
]

const provisionalRows = [
  {
    criteria: 'Does the STR  Address match the BC Services Account Address',
    outcome: data[0].record.address_match ? 'Addresses match' : 'Addresses do not match'
  },
  {
    criteria: 'Business License Required and Provided',
    outcome: data[0].record.business_license_required_provided
      ? 'Required & Provided'
      : data[0].record.business_license_not_required_not_provided
        ? 'Not Required & Not provided'
        : 'Required & Not Provided'
  },
  {
    criteria: 'Title Check',
    outcome: data[0].record.title_check ? 'Passed LTSA Check' : 'Did Not Pass LTSA Check'
  }
]

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

const flavour = application ? getFlavour(application.status, application.invoices) : null

</script>
