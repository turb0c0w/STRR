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
          :day="formState.primaryContact.birthDay"
          :month="formState.primaryContact.birthMonth"
          :year="formState.primaryContact.birthYear"
          :months="getMonths(true)"
          @set-day="(day: number) => setDay(day, true)"
          @set-year="(year: number) => setYear(year, true)"

        />
        <BcrosFormSectionContactInformationContactDetails
          :phone-number="formState.primaryContact.phoneNumber"
          :preferred-name="formState.primaryContact.preferredName"
          :extension="formState.primaryContact.extension"
          :fax-number="formState.primaryContact.faxNumber"
          :email-address="formState.primaryContact.emailAddress"
          @set-email-address="(email: string) => setEmail(email, true)"
          @set-fax-number="(fax: string) => setFax(fax, true)"
          @set-extension="(extension: string) => setExtension(extension, true)"
          @set-preferred-name="(preferred: string) => setPreferred(preferred, true)"
          @set-phone-number="(phone: string) => setPhone(phone, true)"
        />
        <BcrosFormSectionContactInformationMailingAddress
          id="primaryContactAddress"
          :country="formState.primaryContact.country"
          :address="formState.primaryContact.address"
          :addressLineTwo="formState.primaryContact.addressLineTwo"
          :city="formState.primaryContact.city"
          :province="formState.primaryContact.province"
          :postalCode="formState.primaryContact.postalCode"
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
            :day="formState.primaryContact.birthDay"
            :month="formState.primaryContact.birthMonth"
            :year="formState.primaryContact.birthYear"
            :months="getMonths(true)"
            @set-day="(day: number) => setDay(day, false)"
            @set-year="(year: number) => setYear(year, false)"
            :dob-optional="true"
          />
          <BcrosFormSectionContactInformationContactDetails
            :phone-number="formState.secondaryContact.phoneNumber"
            :preferred-name="formState.secondaryContact.preferredName"
            :extension="formState.secondaryContact.extension"
            :fax-number="formState.secondaryContact.faxNumber"
            :email-address="formState.secondaryContact.emailAddress"
            @set-email-address="(email: string) => setEmail(email, false)"
            @set-fax-number="(fax: string) => setFax(fax, false)"
            @set-extension="(extension: string) => setExtension(extension, false)"
            @set-preferred-name="(preferred: string) => setPreferred(preferred, false)"
            @set-phone-number="(phone: string) => setPhone(phone, false)"
          />
          <BcrosFormSectionContactInformationMailingAddress
            id="secondaryContactAddress"
            :country="formState.secondaryContact.country"
            :address="formState.secondaryContact.address"
            :addressLineTwo="formState.secondaryContact.addressLineTwo"
            :city="formState.secondaryContact.city"
            :province="formState.secondaryContact.province"
            :postalCode="formState.secondaryContact.postalCode"
            :enable-address-complete="enableAddressComplete"
          />
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'
import { DropdownItem } from '@nuxt/ui/dist/runtime/types';

const { fullName } = defineProps<{ fullName: string }>()

const emit = defineEmits<{
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

const setDay = (day: number, primary: boolean) => { 
  primary
    ? formState.primaryContact.birthDay = day
    : formState.secondaryContact.birthDay = day
}

const setYear = (year: number, primary: boolean) => { 
  primary
    ? formState.primaryContact.birthYear = year 
    : formState.secondaryContact.birthYear = year
}

const setEmail = (email: string, primary: boolean) => { 
  primary
    ? formState.primaryContact.emailAddress = email
    : formState.secondaryContact.emailAddress = email
}

const setFax = (fax: string, primary: boolean) => { 
  primary
    ? formState.primaryContact.faxNumber = fax
    : formState.secondaryContact.faxNumber = fax
}

const setExtension = (extension: string, primary: boolean) => { 
  primary
    ? formState.primaryContact.extension = extension
    : formState.secondaryContact.extension = extension
}

const setPreferred = (preferred: string, primary: boolean) => { 
  primary
    ? formState.primaryContact.preferredName = preferred
    : formState.secondaryContact.preferredName = preferred
}

const setPhone = (phone: string, primary: boolean) => { 
  primary
    ? formState.primaryContact.phoneNumber = phone
    : formState.secondaryContact.phoneNumber = phone
}

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
  t('general.december'),
]


const getMonths = (primary: boolean): DropdownItem[][] => months.map((month: string) => [{
    label: month,
    click: () => { 
      primary ?
        formState.primaryContact.birthMonth = month :
        formState.secondaryContact.birthMonth = month
    }
  }]
)

</script>
