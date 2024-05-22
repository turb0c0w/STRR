<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.internetListingDetails')" class="pb-[40px]">
      <div v-for="(listing, index) in listingDetails">
        <div :key="listing" class="flex flex-row justify-between w-full mb-[40px] items-center">
          <UFormGroup name="urlOne" class="pr-[16px] flex-grow">
            <UInput
              v-model="listingDetails[index]"
              :placeholder="`Platform URL ${index > 0 ? index + 1: ''}`"
            />
          </UFormGroup>
          <div
            class="flex flex-row mr-[20px] w-[117px] h-[36px] items-center justify-center text-[16px] text-blue-500"
            :role="index > 0 ? 'button': ''"
            :onclick="index > 0 ? () => removeDetailAtIndex(index): null"
          >
            <div v-if="index > 0" class="flex flex-row justify-center items-center">
              <p class="mr-[4px]">
                {{ t('create-account.contact.remove') }}
              </p>
              <UIcon class="h-[20px] w-[20px]" name="i-mdi-remove" alt="remove icon" />
            </div>
          </div>
        </div>
      </div>
      <BcrosButtonsPrimary
        :action="addPlatform"
        :text="t('create-account.contact.add-secondary')"
        variant="outline"
        icon=""
        class="mb-[40px]"
      />
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const { formState } = defineProps<{ formState: any }>();

const {
  listingDetails
} = formState

const addPlatform = () => {
  listingDetails.push('')
}

const removeDetailAtIndex = (index: number) => {
  console.log("removeDetailAtIndex")
  listingDetails.splice(index, 1)
}

const t = useNuxtApp().$i18n.t

</script>
