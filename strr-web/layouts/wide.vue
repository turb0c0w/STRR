<template>
  <div data-cy="default-layout">
    <div class="flex justify-between flex-col h-screen">
      <BcrosHeader />
      <div class="flex grow justify-center">
        <div class="py-[56px] mobile:py-[20px]">
          <NuxtPage />
        </div>
      </div>
      <BcrosFooter />
    </div>
  </div>
</template>
