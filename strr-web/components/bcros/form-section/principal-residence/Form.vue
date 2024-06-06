<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="desktop:mb-[180px] mobile:mb-[32px] rounded-[4px]">
      <div class="mb-[32px] mx-[8px]">
        <p class="text-[18px] mb-[8px] font-bold">
          {{ tPrincipalResidence('property') }}
        </p>
        <p class="text-[16px] text-bcGovColor-midGray">
          {{ formState.propertyDetails.address }}
        </p>
      </div>
      <div class="bg-white py-[22px] px-[30px] mobile:px-[8px] text-bcGovColor-midGray text-[16px]">
        <p class="text-[16px] mb-[16px]">
          {{ tPrincipalResidence('provincial-rules') }}
        </p>
        <URadioGroup v-model="formState.principal.isPrincipal" :legend="tPrincipalResidence('radio-legend')" :options="primaryResidenceRadioOptions" />
        <UFormGroup v-if="!formState.principal.isPrincipal && formState.principal.isPrincipal !== undefined" class="text-[16px] mt-[20px]">
          <USelect
            v-model="formState.principal.reason"
            :placeholder="tPrincipalResidence('reason')"
            :options="exemptionReasons"
            option-attribute="key"
            class="w-full text-[16px]"
            aria-label="Exemption reason"
          />
          <p class="ml-[18px] text-bcGovColor-midGray text-[12px]">
            {{ tPrincipalResidence('reason-hint') }}
          </p>
        </UFormGroup>
        <UFormGroup v-if="formState.principal.reason === tPrincipalResidence('other')" class="text-[16px] ml-[48px] mt-[20px]">
          <USelect
            v-model="formState.principal.otherReason"
            :placeholder="tPrincipalResidence('service')"
            :options="otherExemptionReasons"
            option-attribute="key"
            class="w-full text-[16px]"
            aria-label="Other exemption reason"
          />
          <p class="ml-[18px] text-bcGovColor-midGray text-[12px]">
            {{ tPrincipalResidence('reason-hint') }}
          </p>
        </UFormGroup>
      </div>
      <div v-if="formState.principal.isPrincipal">
        <div class="mt-[40px] mobile:mx-[8px]">
          <p>{{ tPrincipalResidence('required-docs') }}</p>
          <div class="p-[16px] flex flex-row text-blue-500 text-[16px]">
            <img class="mr-[4px]" src="/icons/create-account/info.svg">
            <p>{{ tPrincipalResidence('doc-requirements') }}</p>
          </div>
        </div>
        <div class="mb-[40px] bg-white rounded-[4px]">
          <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
            <p class="px-[40px] py-[15px] font-bold">
              {{ tPrincipalResidence('doc-details') }}
            </p>
          </div>
          <BcrosFormSection
            :title="tPrincipalResidence('file-upload')"
          >
            <p class="mb-[16px]">
              {{ tPrincipalResidence('upload-multiple') }}
            </p>
            <div class="flex flex-row items-center">
              <img class="mr-[4px]" src="/icons/create-account/attach.svg" alt="Paperclip icon">
              <UInput
                accept=".pdf,.jpg,.png"
                type="file"
                class="w-full"
                :placeholder="tPrincipalResidence('supporting')"
                @change="uploadFile"
              />
            </div>
            <p class="text-[12px] ml-[58px] mt-[4px] mb-[40px] text-bcGovColor-midGray">
              {{ tPrincipalResidence('file-reqs') }}
            </p>
          </BcrosFormSection>
        </div>
        <div class="desktop:mb-[180px] mobile:mb-[32px] bg-white rounded-[4px]">
          <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
            <p class="px-[40px] py-[15px] font-bold">
              {{ tPrincipalResidence('declaration') }}
            </p>
          </div>
          <BcrosFormSection class="pb-[40px]">
            <UCheckbox v-model="declaration" class="mb-[18px]" name="declaration" :label="tPrincipalResidence('declare')" />
            <UCheckbox v-model="consent" name="consent" :label="tPrincipalResidence('consent')" />
          </BcrosFormSection>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';

const t = useNuxtApp().$i18n.t
const tPrincipalResidence = (translationKey: string) => t(`create-account.principal-residence.${translationKey}`)

const declaration = ref(false)
const consent = ref(false)

const apiURL = useRuntimeConfig().public.strrApiURL
const axiosInstance = addAxiosInterceptors(axios.create())

const uploadFile = (file: any) => {
  console.log(file)
}

// const upload = () => {
//   axiosInstance.post<string>(`${apiURL}/registrations`)
//     .then((response) => {
//       const data = response?.data
//       if (!data) { throw new Error('Invalid AUTH API response') }
//       return data
//     })
//     .catch((error: string) => {
//       console.warn('Error creating account.')
//       console.error(error)
//     })
// }


const primaryResidenceRadioOptions = [{
  value: true,
  label: tPrincipalResidence('yes')
}, {
  value: false,
  label: tPrincipalResidence('no')
}]

const exemptionReasons: string[] = [
  tPrincipalResidence('exempt-community'),
  tPrincipalResidence('eligible'),
  tPrincipalResidence('other')
]

const otherExemptionReasons: string[] = [
  tPrincipalResidence('timeshare'),
  tPrincipalResidence('fractional'),
  tPrincipalResidence('exchange'),
  tPrincipalResidence('lodge'),
  tPrincipalResidence('institution'),
  tPrincipalResidence('strata-guest')
]

</script>
