<template>
  <div
    :class="
      `
        flex d:justify-between bg-white absolute w-full top-0 left-0 h-[104px] shadow-md
        py-[30px] px-[70px]
        m:flex-col m:h-[116px] m:pt-[16px] m:pb-[6px] m:px-[8px]
        ${hideButtons ? 'm:h-[70px]': ''}
      `
    "
  >
    <slot />
    <div v-if="!hideButtons">
      <div class="mobile:hidden">
        <BcrosButtonsPrimary
          :text="tBanner('approve')"
          :action="() => null"
          variant="outline"
          class-name="ml-[16px]"
        />
        <BcrosButtonsPrimary
          :text="tBanner('reject')"
          :action="() => null"
          variant="outline"
          class-name="ml-[16px]"
        />
        <BcrosButtonsPrimary
          :text="tBanner('issue')"
          :action="() => null"
          variant="outline"
          class-name="ml-[16px]"
        />
      </div>
      <div class="desktop:hidden flex">
        <a class="mr-[16px] py-[10px]">{{ tBanner('approve') }}</a>
        <a class="mr-[16px] py-[10px]">{{ tBanner('reject') }}</a>
        <a class="mr-[16px] py-[10px]">{{ tBanner('issue') }}</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

const { hideButtons = false } = defineProps<{ hideButtons?: boolean }>()
const t = useNuxtApp().$i18n.t
const tBanner = (text: string) => t(`banner.${text}`)

</script>
