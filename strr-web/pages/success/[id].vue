<template>
  <div data-cy="account-select-page">
    <BcrosTypographyH1 text="Application Submitted" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
    <div class="bg-white py-[22px] px-[30px] flex flex-row">
      <img
        class="self-start mr-[10px] mt-[2px]"
        src="/icons/create-account/check_circle.svg"
        alt="Confirmation check mark"
      >
      <div>
        <p class="mb-[24px]">
          Short term registry application submitted for the following property:
        </p>
        <p class="mb-[24px] font-bold">
          {{ fetchedRegistration ? fetchedRegistration.unitAddress.address : '-' }}
        </p>
        <p>Your application will be reviewed by our team and we will email you with next steps.</p>
      </div>
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

axiosInstance.get(`${apiURL}/registrations`)
  .then((res) => {
    res.data.forEach((registration: any) => {
      if (registration.id.toString() === id.toString()) {
        fetchedRegistration.value = registration
      }
    })
  })

</script>
