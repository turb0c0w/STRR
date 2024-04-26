<template>
  <UButton 
    :label="letter"
    color="primary"
    class="pointer-events-none bg-blue-350 h-[32px] w-[32px] flex font-bold justify-center"
    :inactive="true"
  />
</template>

<script setup lang="ts">
const { letter } = defineProps<{ letter: string }>();
</script>