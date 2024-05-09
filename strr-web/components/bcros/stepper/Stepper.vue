<template>
  <div
    data-cy="stepper-component"
    class="rounded-[4px] w-full flex flex-row justify-between bg-white px-[20px] pt-[20px]"
  >
    <div
      v-for="(step, index) in steps"
      :key="step.label"
      :class="`
        ${index == steps.length - 1 ? 'shrink grow-0': 'shrink-0 grow'}
        flex flex-row align-center
      `"
    >
      <div
        :class="`${index == activeStep.valueOf() ? 'border-b-[3px] border-blue-500' : ''} pb-[20px] flex flex-col cursor-pointer`"
        @click="setActiveStep(index)"
      >
        <div class="flex justify-center pt-[7px] ">
          <div :class="`${index == activeStep.valueOf() ? 'bg-blue-500' : ''} grow-0 shrink outline outline-1 outline-blue-500 px-[15px] py-[15px] rounded-full`">
            <img :src="`${index == activeStep.valueOf() ? `${step.activeIconPath}`: step.inactiveIconPath}`">
          </div>
        </div>
        <p :class="`${index == activeStep.valueOf() ? 'font-bold text-black' : 'text-blue-500'} mt-[8px] leading-[20px] text-[14px] max-w-[95px] text-center`">
          {{ t(step.label) }}
        </p>
      </div>
      <div
        v-if="index < steps.length - 1"
        class="self-center grow shrink-0 mb-[35px]"
      >
        <div class="h-[1px] bg-bcGovColor-formFieldLines" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { steps } = defineProps<{ steps: StepI[] }>()
const activeStep = ref(0)

const setActiveStep = (newStep: number) => activeStep.value = newStep

const t = useNuxtApp().$i18n.t

</script>
