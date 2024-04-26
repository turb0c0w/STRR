<template>
  <h1 class="font-bold text-[32px] pb-[25px]" :data-cy="dataCy">
    {{ t(text) }}
  </h1>
</template>

<script setup lang="ts">
  const t = useNuxtApp().$i18n.t
  const { text, dataCy} = defineProps<{ text: string, dataCy: string }>()
</script>