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
        <div ref="testRef" class="mb-[16px] text-[14px] leading-[22px]">
          {{ t('create-account.contact.disclaimer') }}
        </div>
      </BcrosFormSection>
      <UForm ref="form" :schema="contactSchema" :state="formState.primaryContact">
        <BcrosFormSectionContactInformationContactInfo
          v-model:day="formState.primaryContact.birthDay"
          v-model:month="formState.primaryContact.birthMonth"
          v-model:year="formState.primaryContact.birthYear"
          :month-error="monthError"
          :is-primary="true"
          @validate-months="validateMonths"
        />
        <BcrosFormSectionContactInformationContactDetails
          v-model:phone-number="formState.primaryContact.phoneNumber"
          v-model:preferred-name="formState.primaryContact.preferredName"
          v-model:extension="formState.primaryContact.extension"
          v-model:fax-number="formState.primaryContact.faxNumber"
          v-model:email-address="formState.primaryContact.emailAddress"
          :is-primary="true"
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
          default-country-iso2="CA"
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
        <UForm ref="secondForm" :schema="secondaryContactSchema" :state="formState.secondaryContact">
          <BcrosFormSectionContactInformationContactInfo
            v-model:day="formState.secondaryContact.birthDay"
            v-model:month="formState.secondaryContact.birthMonth"
            v-model:year="formState.secondaryContact.birthYear"
            :is-primary="false"
          />
          <BcrosFormSectionContactInformationContactDetails
            v-model:phone-number="formState.secondaryContact.phoneNumber"
            v-model:preferred-name="formState.secondaryContact.preferredName"
            v-model:extension="formState.secondaryContact.extension"
            v-model:fax-number="formState.secondaryContact.faxNumber"
            v-model:email-address="formState.secondaryContact.emailAddress"
            v-model:first-name="formState.secondaryContact.firstName"
            v-model:last-name="formState.secondaryContact.lastName"
            v-model:middle-name="formState.secondaryContact.middleName"
            :is-primary="false"
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
            default-country-iso2="CA"
            :postal="false"
          />
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'
const t = useNuxtApp().$i18n.t
const monthError = ref('')

const {
  fullName,
  addSecondaryContact,
  toggleAddSecondary,
  isComplete,
  secondFormIsComplete
} = defineProps<{
  fullName: string,
  addSecondaryContact: boolean,
  toggleAddSecondary:() => void,
  isComplete: boolean,
  secondFormIsComplete: boolean
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

const validateMonths = () => {
  const parsed = contactSchema.safeParse(formState.primaryContact).error?.errors
  const error = parsed?.find(error => error.path.includes('birthMonth'))
  monthError.value = error ? error.message : ''
}

const { me, currentAccount } = useBcrosAccount()

if (me?.profile.contacts && me?.profile.contacts.length > 0) {
  formState.primaryContact.phoneNumber = me?.profile.contacts[0].phone
  formState.primaryContact.emailAddress = me?.profile.contacts[0].email
  formState.primaryContact.extension = me?.profile.contacts[0].phoneExtension
}

if (currentAccount && me) {
  const mailingAddress = me?.orgs.find(({ id }) => id === currentAccount.id)?.mailingAddress
  if (mailingAddress) {
    // Check if field already has content before populating so as not to overwrite user changes
    if (!formState.primaryContact.country) { formState.primaryContact.country = mailingAddress[0].country }
    if (!formState.primaryContact.city) { formState.primaryContact.city = mailingAddress[0].city }
    if (!formState.primaryContact.postalCode) { formState.primaryContact.postalCode = mailingAddress[0].postalCode }
    if (!formState.primaryContact.province) { formState.primaryContact.province = mailingAddress[0].region }
    if (!formState.primaryContact.address) { formState.primaryContact.address = mailingAddress[0].street }
    if (!formState.primaryContact.addressLineTwo) {
      formState.primaryContact.addressLineTwo = mailingAddress[0].streetAdditional
    }
  }
}

onMounted(() => {
  if (isComplete) { validateMonths() }
})

const form = ref()

watch(form, () => {
  if (form.value && isComplete) { form.value.validate() }
})

const secondForm = ref()

watch(secondForm, () => {
  if (secondForm.value && secondFormIsComplete) { secondForm.value.validate() }
})

</script>
