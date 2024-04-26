<template>
  <button class="w-[48px] h-[44px]"><img :src="iconPath" :altText="altText"></img></button>
</template>

<script setup lang="ts">
const { iconPath, altText } = defineProps<{ iconPath: string, altText: string }>()
</script>
