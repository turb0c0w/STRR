<template>
  <div>
    <h1>Selected Account Details</h1>
    <p>Name: {{ selectedAccount.name }}</p>
    <p>ID: {{ selectedAccount.id }}</p>
  </div>
</template>

<script setup lang="ts">

import { useFormStore } from '@/stores/strr'

const formStore = useFormStore()
const selectedAccount = computed(() => formStore.getSelectedAccount())

</script>
