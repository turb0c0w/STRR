<template>
  <div
    class="
      flex justify-between bg-white absolute w-full top-0 left-0 h-[104px] shadow-md
      py-[30px] px-[70px]
    "
  >
    <slot />
    <div>
      <BcrosButtonsPrimary
        text="Approve"
        :action="() => null"
        variant="outline"
        class-name="ml-[16px]"
      />
      <BcrosButtonsPrimary
        text="Reject"
        :action="() => null"
        variant="outline"
        class-name="ml-[16px]"
      />
      <BcrosButtonsPrimary
        text="Issue Certificate"
        :action="() => null"
        variant="outline"
        class-name="ml-[16px]"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

</script>
