<template>
  <div data-cy="create-account-page">
    <div class="flex flex-row mobile:flex-col">
      <div class="grow pr-[24px] mobile:pr-[0px]">
        <BcrosTypographyH1 text="create-account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
        <BcrosStepper :steps="steps" />
      </div>
      <div class="shrink mobile:grow">
        <BcrosFeeWidget />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import steps from '../page-data/create-account/steps'

definePageMeta({
  layout: 'wide'
})

</script>
