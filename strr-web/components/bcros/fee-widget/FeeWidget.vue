<template>
  <div
    data-cy="fee-widget"
    class="
      desktop:w-[280px]
      mobile:w-[calc(100%-8px)] mobile:fixed mobile:bottom-[4px] mobile:mx-[4px] mobile:left-[0px]
      rounded-[4px] font-bold text-black bg-white z-10
    "
  >
    <div
      :class="`
        ${isMobile && folded ? 'rounded-[4px]' : 'rounded-t-[4px]'}
        px-[15px] py-[10px] pt-[10px] text-white bg-blue-550 rounded-t-[4px] flex flex-row justify-between
        `
      "
    >
      <p>{{ t("fee-widget.summary") }}</p>
      <div class="hidden mobile:flex" @click="toggleFolded">
        <img src="/icons/caret.svg" :class="`cursor-pointer transition-all ${folded ? 'rotate-180': ''}`">
      </div>
    </div>
    <div :class="`transition-all ${folded ? 'h-[0px] overflow-hidden p-[0px]': 'px-[15px] pb-[10px] '}`">
      <p class="py-[10px] border-b-[1px] border-bcGovGray-300">
        {{ t("fee-widget.registration-fee") }}
      </p>
      <div class="py-[10px] flex-row flex justify-between">
        <p>{{ t("fee-widget.total") }}</p>
        <p class="font-normal text-bcGovGray-700">
          {{ t("fee-widget.cad") }} <b class="text-black">-</b>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

import useScreenSize from '../../../composables/useScreenSize'

const t = useNuxtApp().$i18n.t
const folded = ref(false)

const toggleFolded = () => {
  folded.value = !folded.value
}

const { width } = useScreenSize()

const isMobile = width.value <= 1263

if (isMobile) {
  folded.value = true
}

</script>
