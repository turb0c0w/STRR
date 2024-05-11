<template>
  <div data-cy="form-section" class="mt-[40px]">
    <div class="flex flex-row mobile:flex-col">
      <div class="w-[200px]">
        <p class="font-bold">
          {{ t(title) }}
        </p>
      </div>
      <div>
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

const { title } = defineProps<{
  title: string
}>()

const t = useNuxtApp().$i18n.t

</script>
