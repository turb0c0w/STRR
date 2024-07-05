<template>
  <h1
    :class="`${noSpacing ? '': 'pb-[25px]'} ${className} font-bold text-[32px]`"
    :data-cy="dataCy"
  >
    {{ t(text) }}
  </h1>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t
const {
  text,
  className,
  dataCy,
  noSpacing = false
} = defineProps<{
  text: string,
  className?: string,
  dataCy?: string,
  noSpacing?: boolean
}>()

</script>
