<template>
  <div>
    <BcrosTypographyH1 text="BC Registry Terms and Conditions" />
    <div class="bg-white flex flex-col pb-[20px]">
      <div class="px-[20px] py-[25px]">
        <span v-html="tos?.content"></span>
      </div>
      <div class="flex flex-row justify-center">
        <BcrosButtonsPrimary
          text="Accept Terms"
          :action="() => null"
        />
        <BcrosButtonsPrimary
          text="Decline"
          :action="() => null"
          variant="outline"
          class-name="ml-[4px]"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

const { updateTosAccpetance } = useBcrosAccount()

const tos = await updateTosAccpetance()

</script>
