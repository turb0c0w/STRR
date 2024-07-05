<template>
  <div>
    <div>
      <BcrosBanner>
        <div class="flex items-center m:mb-[8px] m:justify-between">
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
    <div class="mt-[104px]">
      <div>
        <p class="font-bold mb-[24px] mobile:mx-[8px]">
          Registration Status
        </p>
        <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
          <div class="flex flex-row justify-between w-full mobile:flex-col">
            <BcrosFormSectionReviewItem
              title="Status"
            >
              <p>{{ application?.status }}</p>
            </BcrosFormSectionReviewItem>
          </div>
        </div>
      </div>
      <div class="mt-[40px]">
        <p class="font-bold mb-[24px] mobile:mx-[8px]">
          Rental Unit Information
        </p>
        <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
          <div class="flex flex-row justify-between w-full mobile:flex-col desktop:mb-[24px]">
            <BcrosFormSectionReviewItem
              title="Nickname"
            >
              <p>{{ application?.unitAddress.nickname }}</p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="Business License"
            >
              <p>{{ application?.unitDetails.businessLicense }}</p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="Ownership Type"
            >
              <p>{{ application?.unitDetails.ownershipType }}</p>
            </BcrosFormSectionReviewItem>
          </div>
          <div class="flex flex-row justify-between w-full mobile:flex-col">
            <BcrosFormSectionReviewItem
              title="Address"
            >
              <p>{{ application?.unitAddress.address }}</p>
              <p v-if="application?.unitAddress.addressLineTwo">
                {{ application?.unitAddress.addressLineTwo }}
              </p>
              <p>
                {{
                  `
                    ${application?.unitAddress.city ?? '-'}
                    ${application?.unitAddress.province ?? '-'}
                    ${application?.unitAddress.postalCode ?? '-'}
                  `
                }}
              </p>
              <p>
                {{
                  `
                  ${application?.unitAddress.country
                    ? regionNamesInEnglish.of(application?.unitAddress.country)
                  : '-'}
                `
                }}
              </p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="Type of Property"
            >
              <p>{{ application?.unitDetails.propertyType }}</p>
            </BcrosFormSectionReviewItem>
            <div class="flex-1" />
          </div>
        </div>
        <div class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            Primary Contact Information
          </p>
          <div class="d:hidden">
            <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
              <BcrosFormSectionReviewItem
                title="Name"
              >
                <p>{{ (application ? getContactRows(application?.primaryContact): [])[0].name }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Address"
              >
                <p>{{ (application ? getContactRows(application?.primaryContact): [])[0].address }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Email Address"
              >
                <p>{{ (application ? getContactRows(application?.primaryContact): [])[0].emailAddress }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Phone Number"
              >
                <p>{{ (application ? getContactRows(application?.primaryContact): [])[0].phoneNumber }}</p>
              </BcrosFormSectionReviewItem>
            </div>
          </div>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px] m:hidden">
            <UTable :rows="application ? getContactRows(application?.primaryContact): []" />
          </div>
        </div>
        <div v-if="application && application?.secondaryContact" class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            Secondary Contact Information
          </p>
          <div class="d:hidden">
            <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
              <BcrosFormSectionReviewItem
                title="Name"
              >
                <p>{{ (application ? getContactRows(application?.secondaryContact): [])[0].name }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Address"
              >
                <p>{{ (application ? getContactRows(application?.secondaryContact): [])[0].address }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Email Address"
              >
                <p>{{ (application ? getContactRows(application?.secondaryContact): [])[0].emailAddress }}</p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Phone Number"
              >
                <p>{{ (application ? getContactRows(application?.secondaryContact): [])[0].phoneNumber }}</p>
              </BcrosFormSectionReviewItem>
            </div>
          </div>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px] m:hidden">
            <UTable :rows="getContactRows(application?.secondaryContact)" />
          </div>
        </div>
        <div class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            Documents
          </p>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
            <div class="flex flex-row justify-between w-full mobile:flex-col">
              <BcrosFormSectionReviewItem
                title="Proof of Principal Residence"
              >
                <div v-for="(supportingDocument) in documents" :key="supportingDocument.file_name">
                  <div class="flex flex-row items-center">
                    <img
                      class="mr-[4px] h-[18px] w-[18px]"
                      src="/icons/create-account/attach_dark.svg"
                      alt="Attach icon"
                    >
                    <p>{{ supportingDocument.file_name }}</p>
                  </div>
                </div>
              </BcrosFormSectionReviewItem>
            </div>
          </div>
        </div>
        <div class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            LTSA Information
          </p>
          <a class="mobile:mx-[8px]" @click="() => navigateTo(`/application-details/${applicationId}/ltsa`)">View LTSA Details</a>
        </div>
        <div class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            Auto-Approval Logic
          </p>
          <a class="mobile:mx-[8px]" @click="() => navigateTo(`/application-details/${applicationId}/auto-approval`)">
            View Auto-Approval Details
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'

const route = useRoute()
const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)
const regionNamesInEnglish = new Intl.DisplayNames(['en'], { type: 'region' })

const { applicationId } = route.params

const { getRegistration, getDocumentsForRegistration } = useRegistrations()

const application = await getRegistration(applicationId.toString())
const documents = await getDocumentsForRegistration(applicationId.toString())

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

const getContactRows = (contactBlock: ContactI) => [{
  name: `
    ${contactBlock.name.firstName}
    ${contactBlock.name.middleName
      ? ` ${contactBlock.name.middleName} `
      : ' '
    }
     ${contactBlock.name.lastName}
  `,
  address: `
    ${contactBlock.mailingAddress.address} 
    ${contactBlock.mailingAddress.addressLineTwo} 
    ${contactBlock.mailingAddress.city} 
    ${contactBlock.mailingAddress.province} 
    ${contactBlock.mailingAddress.postalCode}
  `,
  emailAddress: contactBlock.details.emailAddress,
  phoneNumber:
    `
      ${contactBlock.details.phoneNumber}
      ${contactBlock.details.extension
        ? contactBlock.details.extension
        : ''
      }
    `
}]
</script>
