<template>
  <div data-cy="account-select-page">
    <BcrosTypographyH1
      text="My STR Registry Dashboard"
      data-cy="accountPageTitle"
      class="mobile:pb-[20px] mobile:mx-[8px] pb-[32px]"
    />
    <div>
      <div class="flex flex-row justify-between">
        <BcrosTypographyH2 text="My Registration Application" />
        <BcrosButtonsPrimary text="Create New Registration" :action="() => navigateTo('/create-account')" icon="i-mdi-plus" />
      </div>
      <div class="flex flex-row flex-wrap justify-between">
        <div
          v-for="registration in registrations"
          :key="registration.id"
          class="w-[calc(33%-20px)] mb-[42px] justify-between flex-col bg-white px-[30px] py-[22px] border-[2px] border-bcGovColor-hairlinesOnWhite"
        >
          <div
            :class="
              `
                bg-${getColor(registration.status).background}
                text-${getColor(registration.status).text}
                mb-[24px] font-bold px-[12px] py-[4px] flex-shrink flex w-fit rounded
              `
            "
          >
            {{ registration.status }}
          </div>
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
          <div class="flex flex-row text-bcGovColor-activeBlue justify-start">
            <p class="mr-[22px] cursor-pointer">
              View
            </p>
            <p class="mr-[22px] cursor-pointer">
              Download Certificate
            </p>
            <p class="cursor-pointer">
              Renewal
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

const getColor = (status: string) => {
  switch (status) {
    case 'DENIED':
      return { text: 'red-500', background: 'red-100' }
    case 'APPROVED':
      return { text: 'green-500', background: 'green-100' }
    case 'PENDING':
      return { text: 'orange-500', background: 'orange-100' }
    default:
      return { text: 'orange-500', background: 'yellow-50' }
  }
}

</script>
