<template>
  <div data-cy="account-select-page">
    <BcrosTypographyH1
      :text="tRegistrationStatus('title')"
      data-cy="accountPageTitle"
      class="mobile:pb-[20px] mobile:mx-[8px] pb-[32px] mobile:pb-[24px]"
    />
    <div>
      <div class="px-[8px] flex flex-row justify-between">
        <BcrosTypographyH2 :text="tRegistrationStatus('my-app')" class-name="mobile:pt-[0px]" />
        <BcrosButtonsPrimary
          :text="tRegistrationStatus('create')"
          :action="() => navigateTo('/create-account')"
          icon="i-mdi-plus"
          class-name="mobile:hidden"
        />
      </div>
      <div class="flex flex-row mobile:flex-col flex-wrap justify-between">
        <div
          v-for="registration in registrations"
          :key="registration.id"
          class="
            desktop:w-[calc(33%-20px)] mb-[42px] mobile:mb-[24px] justify-between flex-col
            bg-white px-[30px] mobile:px-[8px] py-[22px]
            border-[2px] border-bcGovColor-hairlinesOnWhite
          "
        >
          <BcrosChip :flavour="getFlavour(registration.status)" class="mobile:hidden">
            {{ tRegistrationStatus(registration.status) }}
          </BcrosChip>
          <div class="flex w-full justify-between">
            <div class="mb-[24px]">
              <p class="font-bold">
                {{
                  registration.unitAddress.nickname
                    ? registration.unitAddress.nickname
                    : registration.unitAddress.address
                }}
              </p>
              <p>
                {{
                  registration.unitAddress.nickname
                    ? registration.unitAddress.address
                    : registration.unitAddress.addressLineTwo
                }}
              </p>
              <p>
                {{ registration.unitAddress.nickname ? registration.unitAddress.addressLineTwo : "" }}
              </p>
              <p>
                {{
                  `
                  ${registration.unitAddress.city}
                  ${registration.unitAddress.province}
                  ${registration.unitAddress.postalCode},
                  ${registration.unitAddress.country}
                  `
                }}
              </p>
            </div>
            <BcrosChip :flavour="getFlavour(registration.status)" class="desktop: hidden">
              {{ tRegistrationStatus(registration.status) }}
            </BcrosChip>
          </div>
          <div class="flex flex-row text-bcGovColor-activeBlue justify-start">
            <p class="mr-[22px] cursor-pointer">
              {{ tRegistrationStatus('view') }}
            </p>
            <p class="mr-[22px] cursor-pointer">
              {{ tRegistrationStatus('download') }}
            </p>
            <p class="cursor-pointer">
              {{ tRegistrationStatus('renewal') }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
definePageMeta({
  layout: 'wide'
})

const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)

const apiURL = useRuntimeConfig().public.strrApiURL
const axiosInstance = addAxiosInterceptors(axios.create())
const registrations = ref<RegistrationI[]>()

axiosInstance.get(`${apiURL}/registrations`)
  .then((res) => {
    registrations.value = res.data
    for (let i = 0; i < 5; i++) {
      registrations.value?.push(res.data[0])
    }
  })

const getFlavour = (status: string) => {
  switch (status) {
    case 'DENIED':
      return AlertsFlavourE.ALERT
    case 'APPROVED':
      return AlertsFlavourE.SUCCESS
    case 'PENDING':
      return AlertsFlavourE.WARNING
    default:
      return AlertsFlavourE.INFO
  }
}

</script>
