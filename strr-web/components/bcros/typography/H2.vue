<template>
  <h2 class="font-bold text-[24px] py-[25px]" :data-cy="dataCy">
    {{ t(text) }}
  </h2>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t
const { text, dataCy } = defineProps<{ text: string, dataCy: string }>()
</script>
