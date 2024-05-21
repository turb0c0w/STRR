<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection title="Contact Details">
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="preferredName" class="pr-[16px] flex-grow">
          <UInput v-model="preferredName" placeholder="Preferred name" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="phoneNumber" class="pr-[16px] flex-grow">
          <UInput v-model="phoneNumber" placeholder="Phone Number" />
        </UFormGroup>
        <UFormGroup name="extension" class="pr-[16px] flex-grow">
          <UInput v-model="extension" placeholder="Extension (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="faxNumber" class="pr-[16px] flex-grow">
          <UInput v-model="faxNumber" placeholder="Fax Number (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="emailAddress" class="pr-[16px] flex-grow">
          <UInput v-model="emailAddress" placeholder="Email Address" />
        </UFormGroup>
      </div>
      <BcrosAlertsMessage :flavour="AlertsFlavourE.INFO" class="mr-[20px]">
        <p>
          <b>Please note:</b>
          Email will be default method of communication. Notices sent to your email address will be deemed received on
          the
          third day after the email is sent.
        </p>
      </BcrosAlertsMessage>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const {
  primaryContact: {
    preferredName,
    phoneNumber,
    extension,
    faxNumber,
    emailAddress
  }
} = formState

const t = useNuxtApp().$i18n.t

</script>
