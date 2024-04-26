<template>
  <div data-cy="default-layout">
    <div class="flex justify-between flex-col h-screen">
      <BcrosHeader />
      <div class="flex grow justify-center">
        <div class="w-[848px] py-[75px]">
          <NuxtPage />
        </div>
      </div>
      <BcrosFooter />
    </div>
  </div>
</template>
