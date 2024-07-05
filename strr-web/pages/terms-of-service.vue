<template>
  <div>
    <BcrosTypographyH1 text="BC Registry Terms and Conditions" />
    <div class="bg-white flex flex-col pb-[20px]">
      <div class="px-[20px] py-[25px]">
        <!-- eslint-disable-next-line -->
        <span v-html="tos?.content" />
      </div>
      <div class="flex flex-row justify-center">
        <BcrosButtonsPrimary
          text="Accept Terms"
          :action="() => acceptTos(true, tos?.versionId)"
        />
        <BcrosButtonsPrimary
          text="Decline"
          :action="() => acceptTos(false)"
          variant="outline"
          class-name="ml-[4px]"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

const { updateTosAcceptance, acceptTos } = useBcrosAccount()

const tos = await updateTosAcceptance()

</script>
