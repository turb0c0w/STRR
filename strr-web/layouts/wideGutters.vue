<template>
  <div data-cy="default-layout">
    <div class="flex justify-between flex-col min-h-screen">
      <BcrosHeader />
      <div class="flex grow justify-center">
        <div class="grow desktop:px-[75px] pt-[75px] mobile:pt-[20px]">
          <NuxtPage />
        </div>
      </div>
      <BcrosFooter :extra-space="false" />
    </div>
  </div>
</template>
