<template>
  <div class="flex flex-col flex-1">
    <p class="font-bold">
      {{ title }}
    </p>
    <p v-if="content">
      {{ content }}
    </p>
    <slot />
  </div>
</template>

<script setup lang="ts">
const { title, content } = defineProps<{
  title: string
  content?: string
}>()

</script>
