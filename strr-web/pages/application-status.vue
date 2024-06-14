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
      <div class="flex flex-row mobile:flex-col flex-wrap">
        <div
          v-for="registration in registrations"
          :key="registration.id"
          :class="`
            ${
            registrations && registrations?.length > 1
              ? 'desktop:w-[calc(33%-20px)]'
              : 'desktop:w-full flex-grow flex-1'
          }
            flex flex-row mobile:flex-col
          `"
        >
          <BcrosStatusCard
            :flavour="getFlavour(registration.status)"
            :status="registration.status"
            :single="!(registrations && registrations?.length > 1)"
          >
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
          </BcrosStatusCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'wide'
})

const t = useNuxtApp().$i18n.t
const tRegistrationStatus = (translationKey: string) => t(`registration-status.${translationKey}`)

const { getRegistrations } = useRegistrations()
const registrations = ref<RegistrationI[]>()
registrations.value = await getRegistrations()

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
