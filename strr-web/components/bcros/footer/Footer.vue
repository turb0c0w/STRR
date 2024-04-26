<template>
  <footer
    id="bcros-main-footer"
    class="h-[54px] grow flex items-center border-t-2 border-bcGovColor-navDivider bg-bcGovColor-footer text-sm"
    data-cy="footer"
  >
    <div class="m-auto px-4 w-full max-w-[1360px]">
      <nav class="flex flex-grow">
        <ul class="p-0 -ml-2 list-none">
          <li v-for="link in links" :key="link.text" class="inline-block mr-2 pr-2 border-r last:mr-0 last:border-r-0">
            <a
              class="block py-1 px-2 text-white hover:underline"
              :href="link.href"
              :target="link.newTab ? '_blank' : '_self'"
            >

              <!-- {{ t('header.buttons.createAccount') }} -->
              {{ t(`footer.link.${link.text}`) }}
            </a>
          </li>
        </ul>
        <div class="flex flex-auto justify-end">
          <Tooltip
            id="footer-tooltip"
            class="mt-1"
            :text="`BTR UI v${version}`"
            :popper="{
              placement: 'left',
              arrow: true
            }"
          >
            <div class="icon-container" role="img" aria-label="information">
              <UIcon class="text-2xl text-white" name="i-mdi-information-outline" />
            </div>
          </Tooltip>
        </div>
      </nav>
    </div>
  </footer>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t
const version = useRuntimeConfig().public.version

const links = [
  { text: 'home', href: '/', newTab: false },
  { text: 'disclaimer', href: 'https://www2.gov.bc.ca/gov/content/home/disclaimer', newTab: true },
  { text: 'privacy', href: 'https://www2.gov.bc.ca/gov/content/home/privacy', newTab: true },
  { text: 'accessibility', href: 'https://www2.gov.bc.ca/gov/content/home/accessibility', newTab: true },
  { text: 'copyright', href: 'https://www2.gov.bc.ca/gov/content/home/copyright', newTab: true }
]
</script>
