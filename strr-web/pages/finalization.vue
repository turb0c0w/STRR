<template>
  <div data-cy="finalization-page" class="relative h-full">
    <div>
      <BcrosTypographyH1 data-cy="finalization-title" :text="tFinalization('title')" class="mobile:pb-[20px]" />
      <p class="mb-[20px]">
        {{ tFinalization('subtitle') }}
      </p>
      <div class="mb-['132px'] bg-white rounded-[4px] padding-[40px]">
        <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
          <p class="px-[40px] py-[15px] font-bold">
            {{ t('create-account.contact.subtitle') }}
          </p>
        </div>
        <BcrosFormSection :title="t('create-account.contact.your-name')" :divider="true">
          <div class="mb-[16px] text-[14px] leading-[22px]">
            {{ userFullName }}
          </div>
          <div ref="testRef" class="mb-[16px] text-[14px] leading-[22px]">
            {{ t('create-account.contact.disclaimer') }}
          </div>
        </BcrosFormSection>
        <div class="w-full h-[1px] bg-bcGovColor-hairlinesOnWhite mx-[40px]" />
        <UForm
          ref="form"
          :schema="finalizationSchema"
          :state="formState"
        >
          <BcrosFormSection
            :title="tFinalization('account-name')"
            class-name="mb-[-30px]"
          >
            <UFormGroup
              name="name"
              class="desktop:pr-[16px] mr-[13px] mb-[40px] flex-grow mobile:mb-[16px]"
              :error="`${accountNameConflict ? 'Account name already exists': ''}`"
            >
              <UInput
                v-model="formState.name"
                :placeholder="tFinalization('account-name')"
                aria-label="account name"
              />
            </UFormGroup>
          </BcrosFormSection>
          <BcrosFormSection
            :title="tFinalization('contact-details')"
          >
            <div class="flex flex-row">
              <UFormGroup name="phone" class="desktop:pr-[16px] mr-[13px] mb-[40px] flex-grow mobile:mb-[16px]">
                <UInput
                  v-model="formState.phone"
                  :placeholder="tFinalization('phone')"
                  aria-label="phone"
                />
              </UFormGroup>
              <UFormGroup name="extension" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
                <UInput
                  v-model="formState.phoneExtension"
                  :placeholder="tFinalization('extension')"
                  aria-label="extension"
                />
              </UFormGroup>
            </div>
            <UFormGroup name="email" class="desktop:pr-[16px] flex-grow mobile:mb-[16px] mb-[40px]">
              <UInput
                v-model="formState.email"
                :placeholder="tFinalization('email')"
                aria-label="email"
              />
            </UFormGroup>
          </BcrosFormSection>
        </UForm>
      </div>
    </div>
    <div class="w-full mt-[32px] flex justify-center">
      <BcrosButtonsPrimary
        :text="tFinalization('create')"
        variant="outline"
        :action="() => validateAndSubmit()"
        icon="i-mdi-chevron-right"
        :trailing="true"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { SbcCreationResponseE } from '~/enums/sbc-creation-response-e'

const t = useNuxtApp().$i18n.t
const tFinalization = (translationKey: string) => t(`finalization.${translationKey}`)
const { userFullName } = useBcrosAccount()
const { createSbcRegistration } = useRegistrations()
const accountNameConflict = ref<boolean>(false)

const form = ref()

const formState = reactive({
  phone: '',
  phoneExtension: '',
  email: '',
  name: ''
})

const validateAndSubmit = () => {
  if (form.value.validate()) {
    const result: SbcCreationResponseE = await createSbcRegistration(formState)
    if (result === SbcCreationResponseE.CONFLICT) {
      accountNameConflict.value = true
    } else {
      accountNameConflict.value = false
    }
  }
}

</script>
