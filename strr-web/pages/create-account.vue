<template>
  <div data-cy="create-account-page">
    <BcrosTypographyH1 text="account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
    <BcrosStepper :steps="steps" />
  </div>
</template>

<script setup lang="ts">
import steps from "../page-data/create-account/steps";

</script>
