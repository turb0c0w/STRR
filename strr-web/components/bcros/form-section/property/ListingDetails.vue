<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.internetListingDetails')">
      <div v-for="(listing, index) in listingDetails">
        <div :key="listing" class="flex flex-row justify-between w-full mb-[40px]">
          <UFormGroup name="urlOne" class="pr-[16px] flex-grow">
            <UInput v-model="listingDetails[index]" placeholder="Platform URL" />
          </UFormGroup>
        </div>
      </div>
      <BcrosButtonsPrimary
        :action="addPlatform"
        :text="t('create-account.contact.add-secondary')"
        variant="outline"
        icon=""
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

const t = useNuxtApp().$i18n.t

</script>
