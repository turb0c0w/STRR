<template>
  <div>
    <BcrosTypographyH1 text="My CEU STR Registry Dashboard" />
    <BcrosTypographyH2 text="Owners STR Registration Applications" />
    <div />
    <div class="bg-white">
      <div class="flex flex-row justify-between px-[16px] py-[14px]">
        <div>
          <UInput
            icon="i-heroicons-magnifying-glass-20-solid"
            size="sm"
            color="white"
            :trailing="false"
            :placeholder="tRegistryDashboard('search')"
            class="w-[333px]"
          />
        </div>
        <div>
          <USelectMenu
            v-model="selectedColumns"
            :options="columns"
            multiple
          >
            <template #label>
              <span>{{ tRegistryDashboard('columnsToShow') }}</span>
            </template>
          </USelectMenu>
        </div>
      </div>
      <UTable :columns="columns" :rows="tableRows" />
      <div class="flex flex-row justify-between">
        <span>Showing...</span>
        <UPagination :model-value="1" :total="10" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { PaginatedRegistrationsI } from '~/interfaces/paginated-registrations-i'
import { PaginationI } from '~/interfaces/pagination-i'

const t = useNuxtApp().$i18n.t
const tRegistryDashboard = (translationKey: string) => t(`registry-dashboard.${translationKey}`)
const { getPaginatedRegistrations } = useRegistrations()
const statusFilter = ref<string>('')
const limit = ref<string>('10')
const offset = ref<string>('0')
const tableRows = ref<Record<string, string>[]>([])

const updateTableRows = async () => {
  const paginationObject: PaginationI = {
    limit: limit.value,
    offset: offset.value
  }
  if (statusFilter.value) {
    paginationObject.filter_by_status = statusFilter.value
  } else {
    delete paginationObject.filter_by_status
  }
  const registrations = await getPaginatedRegistrations(paginationObject)
  if (registrations) {
    tableRows.value = registrationsToTableRows(registrations)
  }
}

const registrationsToTableRows = (registrations: PaginatedRegistrationsI): Record<string, string>[] => {
  const rows: Record<string, string>[] = []
  registrations.results.forEach((result: RegistrationI) => {
    rows.push({
      id: result.id.toString(),
      status: result.status,
      nickname: result.unitAddress.nickname,
      address: result.unitAddress.address,
      registration: result.id.toString(),
      owner: result.primaryContact.name.firstName,
      submission: result.submissionDate
    })
  })
  return rows
}

watch(statusFilter, () => updateTableRows())
watch(limit, () => updateTableRows())
watch(offset, () => updateTableRows())

onMounted(() => {
  updateTableRows()
})

const selectedColumns = ref<{ key: string; label: string; }[]>([])

const columns = [
  { key: 'id', label: tRegistryDashboard('applicationNumber') },
  { key: 'status', label: tRegistryDashboard('status') },
  { key: 'nickname', label: tRegistryDashboard('nickname') },
  { key: 'address', label: tRegistryDashboard('address') },
  { key: 'registration', label: tRegistryDashboard('registrationNumber') },
  { key: 'owner', label: tRegistryDashboard('owner') },
  { key: 'submission', label: tRegistryDashboard('submissionDate') }
]

onMounted(() => {
  selectedColumns.value = columns
})

definePageMeta({
  layout: 'wide-no-space'
})

</script>
