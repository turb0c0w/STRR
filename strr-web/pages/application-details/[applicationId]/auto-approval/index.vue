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
                  : ''}${tApplicationDetails('registration')} #${applicationId}
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
          {{ tAutoApproval('automatic-logic') }}
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
            {{ tAutoApproval('provisional-logic') }}
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
const tApplicationDetails = (translationKey: string) => t(`application-details.${translationKey}`)
const tAutoApproval = (translationKey: string) => t(`auto-approval.${translationKey}`)
const automaticRows = ref<{ [key: string]: string }[]>([])
const provisionalRows = ref<{ [key: string]: string }[]>([])

const { applicationId } = route.params

const { getRegistration, getAutoApproval } = useRegistrations()

const application = await getRegistration(applicationId.toString())

const data: AutoApprovalDataI[] = await getAutoApproval(applicationId.toString()) || {} as AutoApprovalDataI[]

const buildAutomaticRows = (rowsData: AutoApprovalDataI[]) => {
  if (rowsData[0].record.renting !== null) {
    automaticRows.value.push({
      criteria: tAutoApproval('renting'),
      outcome: rowsData[0].record.renting ? tAutoApproval('yes') : tAutoApproval('no')
    })
  }
  if (rowsData[0].record.service_provider !== null) {
    automaticRows.value.push({
      criteria: tAutoApproval('accomodation-selected'),
      outcome: rowsData[0].record.service_provider ? tAutoApproval('yes') : tAutoApproval('no')
    })
  }
  if (rowsData[0].record.pr_exempt !== null) {
    automaticRows.value.push({
      criteria: tAutoApproval('pr-exempt'),
      outcome: rowsData[0].record.pr_exempt
        ? tAutoApproval('exempt')
        : rowsData[0].record.pr_exempt === false
          ? tAutoApproval('not-exempt')
          : tAutoApproval('lookup-failed')
    })
  }
}

const buildProvisionalRows = (rowsData: AutoApprovalDataI[]) => {
  if (rowsData[0].record.address_match !== null) {
    provisionalRows.value.push({
      criteria: tAutoApproval('do-addresses-match'),
      outcome: rowsData[0].record.address_match ? tAutoApproval('do') : tAutoApproval('do-not')
    })
  }

  const licenseNull =
    rowsData[0].record.business_license_required_provided === null &&
    rowsData[0].record.business_license_required_not_provided === null &&
    rowsData[0].record.business_license_not_required_not_provided === null

  if (!licenseNull) {
    provisionalRows.value.push({
      criteria: tAutoApproval('do-addresses-match'),
      outcome: rowsData[0].record.business_license_required_provided
        ? tAutoApproval('required-provided')
        : rowsData[0].record.business_license_not_required_not_provided
          ? tAutoApproval('not-required-not-provided')
          : tAutoApproval('required-not-provided')
    })
  }
  if (rowsData[0].record.title_check !== null) {
    provisionalRows.value.push({
      criteria: tAutoApproval('title-check'),
      outcome: rowsData[0].record.title_check ? tAutoApproval('passed') : tAutoApproval('did-not-pass')
    })
  }
}

buildAutomaticRows(data)
buildProvisionalRows(data)

const getFlavour = (status: string, invoices: RegistrationI['invoices']):
  { alert: AlertsFlavourE, text: string } | undefined => {
  if (invoices.length === 0) {
    return {
      text: tRegistrationStatus('applied'),
      alert: AlertsFlavourE.APPLIED
    }
  }
  if (invoices[0].payment_status_code === 'COMPLETED') {
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
