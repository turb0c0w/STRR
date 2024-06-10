<template>
  <div data-cy="form-section" class="mt-[40px] mobile:mt-[20px] ml-[40px] mr-[20px] mobile:mx-[8px]">
    <div class="flex flex-row mobile:flex-col">
      <div v-if="title" class="w-[200px]">
        <p class="desktop:font-bold mobile:mb-[8px]">
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
    <div v-if="divider" class="h-[1px] w-full bg-bcGovGray-300 mobile:hidden" />
  </div>
</template>

<script setup lang="ts">

const { title, optional, divider } = defineProps<{
  title?: string,
  optional?: boolean
  divider?: boolean
}>()

const t = useNuxtApp().$i18n.t

</script>
