<template>
  <!-- <NuxtLayout name="wide"> -->
    <div data-cy="create-account-page">
      <div class="flex flex-row">
        <div class="grow pr-[24px]">
          <BcrosTypographyH1 text="account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
          <BcrosStepper :steps="steps" />
        </div>
        <div class="shrink">
          <BcrosFeeWidget />
        </div>
      </div>
    </div>
  <!-- </NuxtLayout> -->
</template>

<script setup lang="ts">
import steps from "../page-data/create-account/steps";

const layout = "wide";

</script>
