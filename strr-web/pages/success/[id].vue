<template>
  <div data-cy="account-select-page">
    <BcrosTypographyH1
      text="Application Submitted"
      data-cy="accountPageTitle"
      class="mobile:pb-[20px] mobile:mx-[8px] pb-[32px]"
    />
    <div class="bg-white py-[22px] px-[30px] flex flex-row mobile:px-[8px] mobile:[py-16px] mobile:flex-col">
      <img
        class="self-start mr-[10px] mt-[2px] mobile:[mb-8px]"
        src="/icons/create-account/check_circle.svg"
        alt="Confirmation check mark"
      >
      <div>
        <p class="mb-[24px] mobile:[mb-8px]">
          Short term registry application submitted for the following property:
        </p>
        <p class="mb-[24px] font-bold">
          {{ fetchedRegistration ? fetchedRegistration.unitAddress.address : '-' }}
        </p>
        <p class="mobile:mb-[24px]">
          Your application will be reviewed by our team and we will email you with next steps.
        </p>
      </div>
    </div>
    <div class="mobile:mx-[8px]">
      <BcrosTypographyH2 text="Helpful Links" class="mt-[32px] text-[18px] mb-[24px]" />
      <p class="mb-[24px]">
        <a @click="navigateTo('/application-status')">View your application status</a> in your dashboard
      </p>
      <p class="mb-[24px]">
        <a @click="navigateTo('/profile-page')">Visit your BC Registries Online Services profile page</a> to update your profile information
      </p>
      <p class="mb-[24px]">
        Have another rental property?
      </p>
      <BcrosButtonsPrimary text="Start a new application" :action="redirectToCreate" class-name="font-bold" />
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'

const route = useRoute()
const fetchedRegistration = ref()

const id = route.params.id

const apiURL = useRuntimeConfig().public.strrApiURL
const axiosInstance = addAxiosInterceptors(axios.create())

const redirectToCreate = () => {
  navigateTo('/create-account')
}

axiosInstance.get(`${apiURL}/registrations`)
  .then((res) => {
    res.data.forEach((registration: any) => {
      if (registration.id.toString() === id.toString()) {
        fetchedRegistration.value = registration
      }
    })
  })

</script>
