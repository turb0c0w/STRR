<template>
  <div>
    <p>
      {{ tReview('declaration-part-one') }}
    </p>
    <p class="pl-[12px]">
      a. {{ tReview('declaration-a') }}
    </p>
    <p class="pl-[12px]">
      b. {{ tReview('declaration-a') }}
    </p>
    <p>
      {{ tReview('declaration-part-one') }}
    </p>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

const tReview = (translationKey: string) => t(`create-account.review.${translationKey}`)

</script>
