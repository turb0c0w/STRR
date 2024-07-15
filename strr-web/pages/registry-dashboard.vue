<template>
  <div>
    <BcrosTypographyH1 text="My CEU STR Registry Dashboard" />
    <BcrosTypographyH2 text="Owners STR Registration Applications" />
    <div />
    <div class="bg-white">
      <div class="flex flex-row justify-between">
        <div>
          <UInput />
        </div>
        <div>
          <USelect />
        </div>
      </div>
      <UTable />
    </div>
  </div>
</template>

<script setup lang="ts">

// const t = useNuxtApp().$i18n.t

definePageMeta({
  layout: 'wide-no-space'
})

</script>
