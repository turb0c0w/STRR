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
          LTSA General Information
        </p>
        <div class="bg-white py-[22px] px-[30px] mobile:px-[8px] flex d:flex-row m:flex-col">
          <div class="flex flex-col justify-between w-full mobile:flex-col mr-[40px]">
            <BcrosFormSectionReviewItem
              title="Tax Authority"
            >
              <p>{{ data.taxAuthorities[0].authorityName }}</p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="Date"
              class="d:mt-[24px]"
            >
              <p>{{ data.tombstone.applicationReceivedDate }}</p>
            </BcrosFormSectionReviewItem>
          </div>
          <div class="flex flex-col justify-between w-full mobile:flex-col mr-[40px]">
            <BcrosFormSectionReviewItem
              title="Description of Land"
            >
              <p>
                {{ data.descriptionsOfLand[0].fullLegalDescription }}
              </p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="PID"
              class="d:mt-[24px]"
            >
              <p>
                {{ data.descriptionsOfLand[0].parcelIdentifier }}
              </p>
            </BcrosFormSectionReviewItem>
            <BcrosFormSectionReviewItem
              title="Parcel Status"
              class="d:mt-[24px]"
            >
              <p>{{ data.descriptionsOfLand[0].parcelStatus }}</p>
            </BcrosFormSectionReviewItem>
          </div>
          <div class="flex flex-col justify-between w-full mobile:flex-col">
            <BcrosFormSectionReviewItem
              title="Ownership Group"
            >
              <p>{{ `Joint Tenancy: ${data.ownershipGroups[0].jointTenancyIndication}` }}</p>
              <p>{{ `Interest Fraction Numerator: ${data.ownershipGroups[0].interestFractionNumerator}` }}</p>
              <p>{{ `Interest Fraction Denominator: ${data.ownershipGroups[0].interestFractionDenominator}` }}</p>
            </BcrosFormSectionReviewItem>
          </div>
        </div>
        <div class="mt-[40px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            LTSA Title Owner(s)
          </p>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
            <div class="d:hidden">
              <BcrosFormSectionReviewItem
                title="Given Name"
              >
                <p>
                  {{ ownerRows[0].givenName }}
                </p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Last Name"
              >
                <p>
                  {{ ownerRows[0].lastName }}
                </p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Address"
              >
                <p>
                  {{ ownerRows[0].address }}
                </p>
              </BcrosFormSectionReviewItem>
              <BcrosFormSectionReviewItem
                title="Occupation"
              >
                <p>
                  {{ ownerRows[0].occupation }}
                </p>
              </BcrosFormSectionReviewItem>
            </div>
            <div class="flex flex-row justify-between w-full mobile:flex-col desktop:mb-[24px] m:hidden">
              <UTable :rows="ownerRows" />
            </div>
          </div>
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

const flavour = application ? getFlavour(application.status, application.invoices) : null

const data = {
  titleStatus: 'REGISTERED',
  titleIdentifier: {
    titleNumber: 'CA111111',
    landTitleDistrict: 'VICTORIA'
  },
  tombstone: {
    applicationReceivedDate: '2007-09-28T13:02:23Z',
    enteredDate: '2007-10-01T21:58:48Z',
    titleRemarks: '',
    marketValueAmount: '194000',
    fromTitles: [
      {
        titleNumber: 'EW111111',
        landTitleDistrict: 'VICTORIA'
      }
    ],
    natureOfTransfers: [
      {
        transferReason: 'FEE SIMPLE'
      }
    ]
  },
  taxAuthorities: [
    {
      authorityName: 'Courtenay Assessment Area'
    }
  ],
  ownershipGroups: [
    {
      jointTenancyIndication: false,
      interestFractionNumerator: '1',
      interestFractionDenominator: '1',
      ownershipRemarks: '',
      titleOwners: [
        {
          lastNameOrCorpName1: 'LASTNAME',
          givenName: 'FIRST MIDDLE',
          incorporationNumber: '',
          occupationDescription: 'PROFESSIONAL DRIVER',
          address: {
            addressLine1: '12 123 HUGH ST',
            addressLine2: '',
            city: 'PRINCE GEORGE',
            province: '',
            provinceName: 'BC',
            country: 'CANADA',
            postalCode: 'V1V 1R1'
          }
        }
      ]
    }
  ],
  descriptionsOfLand: [
    {
      parcelIdentifier: '001-251-538',
      fullLegalDescription: 'LOT 99, DISTRICT LOT 111, COMOX DISTRICT, PLAN 11111',
      parcelStatus: 'A'
    }
  ]
}

const ownerRows = [{
  givenName: data.ownershipGroups[0].titleOwners[0].givenName,
  lastName: data.ownershipGroups[0].titleOwners[0].lastNameOrCorpName1,
  address: `
    ${data.ownershipGroups[0].titleOwners[0].address.addressLine1}
    ${data.ownershipGroups[0].titleOwners[0].address.addressLine2
      ? `${data.ownershipGroups[0].titleOwners[0].address.addressLine2} , `
      : ', '}
    ${data.ownershipGroups[0].titleOwners[0].address.city}
    ${data.ownershipGroups[0].titleOwners[0].address.country}
    ${data.ownershipGroups[0].titleOwners[0].address.postalCode}
  `,
  occupation: data.ownershipGroups[0].titleOwners[0].occupationDescription
}]

</script>
