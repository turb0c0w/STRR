<template>
  <div class="mb-[100px]">
    <BcrosTypographyH1 text="My CEU STR Registry Dashboard" />
    <BcrosTypographyH2 text="Owners STR Registration Applications" />
    <UTabs
      :items="filterOptions"
      class="mb-[24px] w-[500px]"
      @change="onTabChange"
    />
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
      <UTable :loading="loading" :columns="selectedColumns" :rows="tableRows">
        <!-- Only way to do row clicks in NuxtUI currently -->
        <template #registration-data="{ row }">
          <div class="cursor-pointer w-full" @click="navigateToDetails(row.registrationNumber)">
            {{ row.registration }}
          </div>
        </template>
        <template #location-data="{ row }">
          <div class="cursor-pointer w-full" @click="navigateToDetails(row.registrationNumber)">
            {{ row.location }}
          </div>
        </template>
        <template #address-data="{ row }">
          <div class="cursor-pointer w-full" @click="navigateToDetails(row.registrationNumber)">
            {{ row.address }}
          </div>
        </template>
        <template #owner-data="{ row }">
          <div class="cursor-pointer w-full" @click="navigateToDetails(row.registrationNumber)">
            {{ row.owner }}
          </div>
        </template>
        <template #status-data="{ row }">
          <BcrosChip 
            :flavour="getChipFlavour(row.status)" 
          />
        </template>
        <template #submission-data="{ row }">
          <div class="cursor-pointer w-full" @click="navigateToDetails(row.registrationNumber)">
            {{ row.submission }}
          </div>
        </template>
      </UTable>
      <div
        class="
          flex flex-row justify-between border-[#E9ECEF]
          border-t-[1px] h-[67px] justify-center px-[24px]
        "
      >
        <div v-if="totalResults !== 0" class="flex items-center">
          <span class="flex">
            {{
              `
                ${tRegistryDashboard('showing')}
                ${offset + 1} - ${maxPageResults}
                ${tRegistryDashboard('of')}
                ${totalResults}
                ${tRegistryDashboard('results')}
              `
            }}
          </span>
        </div>
        <UPagination v-if="totalResults > 10 " v-model:model-value="page" :total="totalResults" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { PaginatedRegistrationsI } from '~/interfaces/paginated-registrations-i'
import { PaginationI } from '~/interfaces/pagination-i'
import { StatusChipFlavoursI } from '~/interfaces/status-chip-flavours-i';

const t = useNuxtApp().$i18n.t
const tRegistryDashboard = (translationKey: string) => t(`registry-dashboard.${translationKey}`)
const tRegistryDashboardStatus = (translationKey: string) => t(`registry-dashboard.statusChip.${translationKey}`)

const { getPaginatedRegistrations } = useRegistrations()
const statusFilter = ref<string>('')
const limit = ref<number>(10)
const offset = ref<number>(0)
const page = ref<number>(1)
const tableRows = ref<Record<string, string>[]>([])
const totalResults = ref<number>(0)
const loading = ref<boolean>(true)
const maxPageResults = ref<number>(0)

const onTabChange = (index: number) => {
  switch (index) {
    case 1:
      statusFilter.value = 'UNDER_REVIEW'
      break
    case 2:
      statusFilter.value = 'PENDING'
      break
    default:
      statusFilter.value = ''
  }
}

const getChipFlavour = (status: string): StatusChipFlavoursI['flavour'] => {
  switch(status) {
    case 'APPROVED': 
      return { 
        alert: AlertsFlavourE.SUCCESS,
        text: tRegistryDashboardStatus('approved')
      }
    case 'REJECTED': 
      return { 
        alert: AlertsFlavourE.ALERT,
        text: tRegistryDashboardStatus('rejected')
      }
    case 'PENDING': 
      return { 
        alert: AlertsFlavourE.INFO,
        text: tRegistryDashboardStatus('provisional')
      }
    case 'UNDER_REVIEW': 
      return { 
        alert: AlertsFlavourE.INFO,
        text: tRegistryDashboardStatus('underReview')
      }
    default: 
      return {
        alert: AlertsFlavourE.MESSAGE,
        text: ''
      }
  }
}

const filterOptions = [
  {
    label: tRegistryDashboard('all')
  },
  {
    label: tRegistryDashboard('fullReview')
  },
  {
    label: tRegistryDashboard('provisionalApproval')
  }
]
const navigateToDetails = (id: number) => navigateTo(`/application-details/${id.toString()}`)

const updateTableRows = async () => {
  const paginationObject: PaginationI = {
    limit: limit.value.toString(),
    offset: offset.value.toString()
  }
  if (statusFilter.value) {
    paginationObject.filter_by_status = statusFilter.value
  } else {
    delete paginationObject.filter_by_status
  }
  const registrations = await getPaginatedRegistrations(paginationObject)
  if (registrations) {
    totalResults.value = registrations.count
    tableRows.value = registrationsToTableRows(registrations)
  }
  updateMaxPageResults()
  loading.value = false
}

const registrationsToTableRows = (registrations: PaginatedRegistrationsI): Record<string, string>[] => {
  const rows: Record<string, string>[] = []
  registrations.results.forEach((result: RegistrationI) => {
    rows.push({
      registration: result.id.toString(),
      location: result.unitAddress.city,
      address: result.unitAddress.address,
      owner: `
        ${result.primaryContact.name.firstName}
        ${result.primaryContact.name.middleName ?? ''}
        ${result.primaryContact.name.lastName}
      `,
      status: result.status,
      submission: result.submissionDate
    })
  })
  return rows
}

watch(statusFilter, () => updateTableRows())
watch(limit, () => updateTableRows())

const updateMaxPageResults = () => {
  const offsetPlusTen = offset.value + 10
  if (totalResults.value >= offsetPlusTen) {
    maxPageResults.value = offsetPlusTen
  } else {
    maxPageResults.value = totalResults.value
  }
}

watch(page, () => {
  offset.value = (page.value - 1) * 10
  updateTableRows()
})

onMounted(() => {
  updateTableRows()
})

const selectedColumns = ref<{ key: string; label: string; }[]>([])

const columns = [
  { key: 'registration', label: tRegistryDashboard('registrationNumber') },
  { key: 'location', label: tRegistryDashboard('location') },
  { key: 'address', label: tRegistryDashboard('address') },
  { key: 'owner', label: tRegistryDashboard('owner') },
  { key: 'status', label: tRegistryDashboard('status') },
  { key: 'submission', label: tRegistryDashboard('submissionDate') }
]

onMounted(() => {
  selectedColumns.value = columns
})

definePageMeta({
  layout: 'wide-no-space'
})

</script>
