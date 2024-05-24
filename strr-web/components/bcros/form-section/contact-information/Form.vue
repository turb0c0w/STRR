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
          :form-state="formState.primaryContact"
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
        <BcrosFormSectionContactInformationMailingAddress :form-state="formState.primaryContact"  id="primaryContactAddress" />
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
            :form-state="formState.secondaryContact"
            :dob-optional="true"
          />
          <BcrosFormSectionContactInformationContactDetails
            :phone-number="formState.secondaryContact.phoneNumber"
            :preferred-name="formState.secondaryContact.preferredName"
            :extension="formState.secondaryContact.extension"
            :fax-number="formState.secondaryContact.faxNumber"
            :email-address="formState.secondaryContact.emailAddress"
            @set-email-address="(email: string) => setEmail(email, true)"
            @set-fax-number="(fax: string) => setFax(fax, true)"
            @set-extension="(extension: string) => setExtension(extension, true)"
            @set-preferred-name="(preferred: string) => setPreferred(preferred, true)"
            @set-phone-number="(phone: string) => setPhone(phone, true)"
          />
          <BcrosFormSectionContactInformationMailingAddress :form-state="formState.secondaryContact" id="secondaryContactAddress"/>
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const { fullName } = defineProps<{ fullName: string }>()

const emit = defineEmits<{
  validatePage: [isValid: boolean]
}>()

const { me } = useBcrosAccount()

if (me?.profile.contacts && me?.profile.contacts.length > 0) {
  formState.primaryContact.phoneNumber = me?.profile.contacts[0].phone
  formState.primaryContact.emailAddress = me?.profile.contacts[0].email
  formState.primaryContact.extension = me?.profile.contacts[0].phoneExtension
}

const primaryIsValid = ref(false)
const secondaryIsValid = ref(false)
const addSecondaryContact = ref(false)

const setEmail = (email: string, primary: boolean) => { 
  primary ? 
    formState.primaryContact.emailAddress = email :
    formState.secondaryContact.emailAddress = email
}

const setFax = (fax: string, primary: boolean) => { 
  primary ? 
    formState.primaryContact.faxNumber = fax :
    formState.secondaryContact.faxNumber = fax
}

const setExtension = (extension: string, primary: boolean) => { 
  primary ? 
    formState.primaryContact.extension = extension :
    formState.secondaryContact.extension = extension
}

const setPreferred = (preferred: string, primary: boolean) => { 
  primary ? 
    formState.primaryContact.preferredName = preferred :
    formState.secondaryContact.preferredName = preferred
}

const setPhone = (phone: string, primary: boolean) => { 
  primary ? 
    formState.primaryContact.phoneNumber = phone :
    formState.secondaryContact.phoneNumber = phone
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

</script>
