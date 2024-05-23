<template>
  <div data-cy="form-section" class="mt-[40px] ml-[40px] mr-[20px]">
    <div class="flex flex-row mobile:flex-col">
      <div class="w-[200px]">
        <p class="font-bold">
          {{ t(title) }}
        </p>
        <p v-if="optional">
          {{ t('general.optional') }}
        </p>
      </div>
      <div class="w-full">
        <slot />
      </div>
    </div>
    <div v-if="divider" class="h-[1px] w-full bg-bcGovGray-300" />
  </div>
</template>

<script setup lang="ts">

const { title, optional, divider } = defineProps<{
  title: string,
  optional?: boolean
  divider?: boolean
}>()

const t = useNuxtApp().$i18n.t

</script>
