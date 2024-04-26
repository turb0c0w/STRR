<template>
  <div>
    <div v-if="userAccounts && authenticated">
      <ul>
        <li v-for="userAccount in userAccounts" :key="userAccount.id">
          {{ userAccount.label }}-
          {{ userAccount.accountType }}-
          {{ userAccount.mailingAddress?.street }}
          {{ userAccount.mailingAddress?.city }}
          {{ userAccount.mailingAddress?.region }}
        </li>
      </ul>
      <div>Create an Account</div>
    </div>
    <div v-if="!userAccounts && authenticated">
      You have no accounts, please Create Account
    </div>
    <div v-if="!authenticated">
      Please login
    </div>
  </div>
</template>

<script setup lang="ts">

import { useBcrosAccount } from '@/stores/account'
import { useBcrosKeycloak } from '@/stores/keycloak'

const account = useBcrosAccount()
const { userAccounts } = storeToRefs(account)
const keycloak = useBcrosKeycloak()
const authenticated = computed(() => keycloak.kc.authenticated)

</script>
