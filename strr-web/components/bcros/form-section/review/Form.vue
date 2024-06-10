<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="desktop:mb-[180px] mobile:mb-[32px] rounded-[4px]">
      <div class="bg-white px-[30px] py-[22px] mobile:px-[8px]">
        <p>{{ tReview('review-instructions') }}</p>
        <p>{{ tReview('review-instructions-continued') }}</p>
      </div>
      <div>
        <div class="mt-[48px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            {{ tReview('primary-contact') }}
          </p>
          <BcrosFormSectionReviewSubsection
            :state="formState.primaryContact"
            :primary="true"
          />
        </div>
        <div v-if="secondaryContact" class="mt-[48px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            {{ tReview('secondary-contact') }}
          </p>
          <BcrosFormSectionReviewSubsection
            :state="formState.secondaryContact"
            :primary="false"
          />
        </div>
        <div class="mt-[48px]">
          <p class="font-bold mb-[24px] mobile:mx-[8px]">
            {{ tReview('rental-unit') }}
          </p>
          <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
            <div class="flex flex-row justify-between w-full desktop:mb-[24px] mobile:flex-col">
              <BcrosFormSectionReviewItem
                :title="tReview('nickname')"
                :content="formState.propertyDetails.nickname === '' ? '-': formState.propertyDetails.nickname"
              />
              <BcrosFormSectionReviewItem
                :title="tReview('business-license')"
                :content="formState.propertyDetails.businessLicense ?? '-'"
              />
              <BcrosFormSectionReviewItem
                :title="tReview('ownership-type')"
                :content="formState.propertyDetails.ownershipType ?? '-'"
              />
            </div>
            <div class="flex flex-row justify-between w-full desktop:mb-[24px] mobile:flex-col">
              <BcrosFormSectionReviewItem
                :title="tReview('address')"
                :content="formState.propertyDetails.address ?? '-'"
              />
              <BcrosFormSectionReviewItem
                :title="tReview('property-type')"
                :content="formState.propertyDetails.propertyType ?? '-'"
              />
              <div class="flex-1" />
            </div>
          </div>
          <div class="mt-[48px]">
            <p class="font-bold mb-[24px] mobile:mx-[8px]">
              {{ tReview('principal') }}
            </p>
            <div class="bg-white py-[22px] px-[30px] mb-[24px] mobile:px-[8px]">
              {{
                `${formState.principal.isPrincipal
                  ? tPrincipal('yes')
                  : tPrincipal('no')
                }`
              }}
              <div v-if="!formState.principal.isPrincipal">
                <p>
                  <b>{{ tReview('reason') }}: </b>
                  {{ `${formState.principal.otherReason
                    ? formState.principal.otherReason
                    : formState.principal.reason
                  }` }}
                </p>
              </div>
            </div>
            <div class="bg-white py-[22px] px-[30px] mobile:px-[8px]">
              <p class="font-bold">
                {{ tReview('proof') }}
              </p>
              <div class="mb-[24px]" />
              <p class="font-bold">
                {{ tReview('declaration') }}
              </p>
              <div class="mt-[8px]">
                <div class="mb-[12px] flex flex-row">
                  <img
                    class="mr-[8px] self-start"
                    src="/icons/create-account/gray_check.svg"
                    alt="Confirmation checkmark"
                  >
                  <BcrosFormSectionReviewDeclaration />
                </div>
                <div class="flex flex-row">
                  <img
                    class="mr-[8px] self-start"
                    src="/icons/create-account/gray_check.svg"
                    alt="Confirmation checkmark"
                  >
                  {{ tPrincipal('consent') }}
                </div>
              </div>
            </div>
          </div>
          <div class="mt-[48px]">
            <p class="font-bold mb-[24px] mobile:mx-[8px]">
              {{ tReview('review') }}
            </p>
            <div class="bg-white py-[22px] px-[30px] mobile:px-[8px] mb-[24px]">
              <UCheckbox
                :label="tReview('confirm')"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

const { secondaryContact } = defineProps<{ secondaryContact: boolean }>()

const tReview = (translationKey: string) => t(`create-account.review.${translationKey}`)
const tPrincipal = (translationKey: string) => t(`create-account.principal-residence.${translationKey}`)

</script>
