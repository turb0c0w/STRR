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
        />
      </UForm>
    </div>
    <div v-if="!addSecondaryContact" class="mb-[180px] mt-[32px]">
      <BcrosButtonsPrimary
        :action="toggleAddSecondary"
        :text="t('create-account.contact.add-secondary')"
        variant="outline"
        icon=""
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
            v-model:day="formState.primaryContact.birthDay"
            v-model:month="formState.primaryContact.birthMonth"
            v-model:year="formState.primaryContact.birthYear"
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
          />
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'
import { formState } from '@/stores/strr'

const { fullName } = defineProps<{ fullName: string }>()

defineEmits<{
  validatePage: [isValid: boolean]
}>()

const {
  address: canadaPostAddress,
  enableAddressComplete
} = useCanadaPostAddress()

watch(canadaPostAddress, (newAddress) => {
  if (newAddress) {
    formState.primaryContact.address = newAddress.street
    formState.primaryContact.addressLineTwo = newAddress.streetAdditional
    formState.primaryContact.country = newAddress.country
    formState.primaryContact.city = newAddress.city
    formState.primaryContact.province = newAddress.region
    formState.primaryContact.postalCode = newAddress.postalCode
  }
})

const { me } = useBcrosAccount()

if (me?.profile.contacts && me?.profile.contacts.length > 0) {
  formState.primaryContact.phoneNumber = me?.profile.contacts[0].phone
  formState.primaryContact.emailAddress = me?.profile.contacts[0].email
  formState.primaryContact.extension = me?.profile.contacts[0].phoneExtension
}

const primaryIsValid = ref(false)
const secondaryIsValid = ref(false)
const addSecondaryContact = ref(false)

const toggleAddSecondary = () => {
  addSecondaryContact.value = !addSecondaryContact.value
}

const t = useNuxtApp().$i18n.t

watch(formState.primaryContact, () => {
  primaryIsValid.value = contactSchema.safeParse(formState.primaryContact).success
})

watch(formState.secondaryContact, () => {
  secondaryIsValid.value = contactSchema.safeParse(formState.primaryContact).success
})

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
