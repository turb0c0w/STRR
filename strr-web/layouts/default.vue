<template>
  <div data-cy="default-layout">
    <div class="flex justify-between flex-col h-screen">
      <Header />
      <slot />
      <Footer />
    </div>
  </div>
</template>
