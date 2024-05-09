<template>
  <div 
    data-cy="fee-widget" 
    class="w-[280px] rounded-[4px] font-bold text-black bg-white"
  >
   <div class="px-[15px] py-[10px] pt-[10px] text-white bg-blue-550 rounded-t-[4px]">
    <p>{{ t("fee-widget.summary") }}</p>
   </div>
   <div class="px-[15px] pb-[10px]">
    <p class="py-[10px] border-b-[1px] border-bcGovGray-300">{{ t("fee-widget.registration-fee") }}</p>
    <div class="py-[10px] flex-row flex justify-between">
      <p>{{ t("fee-widget.total") }}</p>
      <p class="font-normal text-bcGovGray-700">{{ t("fee-widget.cad") }} <b class="text-black">-</b></p>
    </div>
   </div>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

</script>