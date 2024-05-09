<template>
  <div class="absolute w-screen left-[-55px] bottom-[-75px] bg-white h-[120px] flex items-center pl-[70px]">
    <BcrosButtonsPrimary
      :text="t('general.back')"
      :action="setPreviousStep"
      icon="i-mdi-chevron-left"
      :trailing="false"
      variant="outline"
      class-name="mr-[20px]"
    />
    <BcrosButtonsPrimary
      :text="t('general.next')"
      :action="setNextStep"
      icon="i-mdi-chevron-right"
      :trailing="true"
    />
  </div>
</template>

<script setup lang="ts">

const {
  setNextStep,
  setPreviousStep
} = defineProps<{
  setNextStep:() => void,
  setPreviousStep:() => void
}>()

const t = useNuxtApp().$i18n.t

</script>
