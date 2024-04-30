<template>
  <div class="flex">
    <slot>
      <UButton
        :class="classWithDefaultSpacing"
        :color="color || 'primary'"
        :icon="icon"
        :label="label"
        :loading="loading"
        :text="text"
        :trailing="trailing"
        :variant="variant"
        @click="action()"
      >
        {{ text }}
      </UButton>
    </slot>
  </div>
</template>

<script setup lang="ts">
import { ButtonVariant } from '@nuxt/ui/dist/runtime/types'

const { action, color, className, icon, label, loading, text, trailing, variant } = defineProps<{
  action: Function,
  className?: string,
  color?: string,
  icon: string,
  loading?: boolean,
  label: string,
  text: string,
  trailing?: boolean,
  variant?: ButtonVariant
}>()

const classWithDefaultSpacing = `${className} text-[16px] px-[28px] py-[10px] mobile:grow justify-center`

</script>
