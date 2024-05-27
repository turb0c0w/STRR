<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div :class="`mb-[${addSecondaryContact ? '32px' : '132px'}] bg-white rounded-[4px]`">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <BcrosFormSection :title="t('create-account.contact.your-name')" :divider="true">
        <div class="mb-[16px] text-[14px] leading-[22px]">
          {{ fullName }}
        </div>
        <div class="mb-[16px] text-[14px] leading-[22px]">
          {{ t('create-account.contact.disclaimer') }}
        </div>
      </BcrosFormSection>
      <UForm :schema="contactSchema" :state="formState.primaryContact">
        <BcrosFormSectionContactInformationContactInfo
          v-model:day="formState.primaryContact.birthDay"
          v-model:month="formState.primaryContact.birthMonth"
          v-model:year="formState.primaryContact.birthYear"
          :months="getMonths(true)"
        />
        <BcrosFormSectionContactInformationContactDetails
          v-model:phone-number="formState.primaryContact.phoneNumber"
          v-model:preferred-name="formState.primaryContact.preferredName"
          v-model:extension="formState.primaryContact.extension"
          v-model:fax-number="formState.primaryContact.faxNumber"
          v-model:email-address="formState.primaryContact.emailAddress"
        />
        <BcrosFormSectionContactInformationMailingAddress
          id="primaryContactAddress"
          v-model:country="formState.primaryContact.country"
          v-model:address="formState.primaryContact.address"
          v-model:address-line-two="formState.primaryContact.addressLineTwo"
          v-model:city="formState.primaryContact.city"
          v-model:province="formState.primaryContact.province"
          v-model:postal-code="formState.primaryContact.postalCode"
          :enable-address-complete="enableAddressComplete"
          default-country-iso3="CAN"
        />
      </UForm>
    </div>
    <div v-if="!addSecondaryContact" class="desktop:mb-[180px] mobile:mb-[32px] mt-[32px] mobile:w-full mobile:p-[8px]">
      <BcrosButtonsPrimary
        :action="toggleAddSecondary"
        :text="t('create-account.contact.add-secondary')"
        variant="outline"
        icon=""
        class-name="mobile:w-full mobile:mx-[0px]"
      />
    </div>
    <div v-else>
      <div class="mb-[180px] bg-white rounded-[4px]">
        <div class="bg-bcGovColor-gray2 rounded-t-[4px] flex flex-row justify-between items-center">
          <p class="px-[40px] py-[15px] font-bold">
            {{ t('create-account.contact.subtitle-two') }}
          </p>
          <div
            class="flex flex-row mr-[20px] w-[117px] h-[36px] items-center justify-center text-[16px] text-blue-500"
            role="button"
            :onclick="toggleAddSecondary"
          >
            <p class="mr-[4px]">
              {{ t('create-account.contact.remove') }}
            </p>
            <UIcon class="h-[20px] w-[20px]" name="i-mdi-remove" alt="remove icon" />
          </div>
        </div>
        <UForm :schema="contactSchema" :state="formState.secondaryContact">
          <BcrosFormSectionContactInformationContactInfo
            v-model:day="formState.secondaryContact.birthDay"
            v-model:month="formState.secondaryContact.birthMonth"
            v-model:year="formState.secondaryContact.birthYear"
            :months="getMonths(true)"
            :dob-optional="true"
          />
          <BcrosFormSectionContactInformationContactDetails
            v-model:phone-number="formState.secondaryContact.phoneNumber"
            v-model:preferred-name="formState.secondaryContact.preferredName"
            v-model:extension="formState.secondaryContact.extension"
            v-model:fax-number="formState.secondaryContact.faxNumber"
            v-model:email-address="formState.secondaryContact.emailAddress"
          />
          <BcrosFormSectionContactInformationMailingAddress
            id="secondaryContactAddress"
            v-model:country="formState.secondaryContact.country"
            v-model:address="formState.secondaryContact.address"
            v-model:address-line-two="formState.secondaryContact.addressLineTwo"
            v-model:city="formState.secondaryContact.city"
            v-model:province="formState.secondaryContact.province"
            v-model:postal-code="formState.secondaryContact.postalCode"
            :enable-address-complete="enableAddressComplete"
            default-country-iso3="CAN"
          />
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'
import { formState } from '@/stores/strr'
const t = useNuxtApp().$i18n.t

const {
  fullName,
  addSecondaryContact,
  toggleAddSecondary
} = defineProps<{
  fullName: string,
  addSecondaryContact: boolean
  toggleAddSecondary: () => void
}>()

const {
  activeAddressField,
  address: canadaPostAddress,
  enableAddressComplete
} = useCanadaPostAddress()

const getActiveAddressState = (): ContactInformationI | CreateAccountFormStateI['propertyDetails'] => {
  if (activeAddressField.value === 'primaryContactAddress') {
    return formState.primaryContact
  } else if (activeAddressField.value === 'secondaryContactAddress') {
    return formState.secondaryContact
  } else {
    return formState.propertyDetails
  }
}

watch(canadaPostAddress, (newAddress) => {
  const activeAddressState = getActiveAddressState()
  if (newAddress) {
    activeAddressState.address = newAddress.street
    activeAddressState.addressLineTwo = newAddress.streetAdditional
    activeAddressState.country = newAddress.country
    activeAddressState.city = newAddress.city
    activeAddressState.province = newAddress.region
    activeAddressState.postalCode = newAddress.postalCode
  }
})

const { me, currentAccount } = useBcrosAccount()

if (me?.profile.contacts && me?.profile.contacts.length > 0) {
  formState.primaryContact.phoneNumber = me?.profile.contacts[0].phone
  formState.primaryContact.emailAddress = me?.profile.contacts[0].email
  formState.primaryContact.extension = me?.profile.contacts[0].phoneExtension
}

if (currentAccount && me) {
  const mailingAddress = me?.orgs.find(({ id }) => id === currentAccount.id)?.mailingAddress
  if (mailingAddress) {
    formState.primaryContact.country = mailingAddress[0].country
    formState.primaryContact.city = mailingAddress[0].city
    formState.primaryContact.postalCode = mailingAddress[0].postalCode
    formState.primaryContact.province = mailingAddress[0].region
    formState.primaryContact.address = mailingAddress[0].street
    formState.primaryContact.addressLineTwo = mailingAddress[0].streetAdditional
  }
}

const months: string[] = [
  t('general.january'),
  t('general.february'),
  t('general.march'),
  t('general.april'),
  t('general.may'),
  t('general.june'),
  t('general.july'),
  t('general.august'),
  t('general.september'),
  t('general.october'),
  t('general.november'),
  t('general.december')
]

const getMonths = (primary: boolean): DropdownItem[][] => months.map((month: string) => [{
  label: month,
  click: () => {
    primary
      ? formState.primaryContact.birthMonth = month
      : formState.secondaryContact.birthMonth = month
  }
}]
)

</script>
