import axios from 'axios'
import { SbcCreationResponseE } from '~/enums/sbc-creation-response-e'
import { AutoApprovalDataI } from '~/interfaces/auto-approval-data-i'
import { LtsaDataI } from '~/interfaces/ltsa-data-i'
import { RegistrationHistoryEventI } from '~/interfaces/registration-history-event-i'

export const useRegistrations = () => {
  const apiURL = useRuntimeConfig().public.strrApiURL
  const axiosInstance = addAxiosInterceptors(axios.create())

  const getRegistrations = () => axiosInstance.get<RegistrationI[]>(`${apiURL}/registrations`)
    .then((res) => {
      if (res.data.length === 0) {
        navigateTo('/create-account')
      }
      return res.data
        .sort(
          (registrationA, registrationB) =>
            registrationA.unitAddress.city.localeCompare(registrationB.unitAddress.city)
        )
        .sort(
          (registrationA, registrationB) =>
            getStatusPriority(registrationA.status) - getStatusPriority(registrationB.status)
        )
    })

  const getRegistration = (id: string): Promise<RegistrationI | void> =>
    axiosInstance.get(`${apiURL}/registrations`)
      .then(res => res.data.find((registration: any) => registration.id.toString() === id))

  const getLtsa = (id: string): Promise<LtsaDataI[] | void> =>
    axiosInstance.get(`${apiURL}/registrations/${id}/ltsa`)
      .then(res => res.data)

  const getAutoApproval = (id: string): Promise<AutoApprovalDataI[] | void> =>
    axiosInstance.get(`${apiURL}/registrations/${id}/auto_approval`)
      .then(res => res.data)

  const getDocumentsForRegistration = (id: string): Promise<DocumentI[]> =>
    axiosInstance.get(`${apiURL}/registrations/${id}/documents`)
      .then(res => res.data)

  const getRegistrationHistory = (id: string): Promise<RegistrationHistoryEventI[]> =>
    axiosInstance.get(`${apiURL}/registrations/${id}/history`)
      .then(res => res.data)

  const getStatusPriority = (status: string) => {
    switch (status) {
      case 'DENIED':
        return 4
      case 'APPROVED':
        return 3
      case 'PENDING':
        return 2
      default:
        return 1
    }
  }

  const createSbcRegistration = (registration:
    {
      email: string,
      phone: string,
      phoneExtension: string,
      name: string
    }
  ): Promise<SbcCreationResponseE> =>
    axiosInstance
      .post<{
        sbc_account_id: string, id: string
      }>(`${apiURL}/account/sbc`,
        registration
      )
      .then((res) => {
        if (res.data) {
          const { setAccountInfo } = useBcrosAccount()
          setAccountInfo(res.data.sbc_account_id)
          navigateTo('/create-account')
          return SbcCreationResponseE.SUCCESS
        }
        return SbcCreationResponseE.ERROR
      })
      .catch((err) => {
        if (err.status === '403') { return SbcCreationResponseE.CONFLICT }
        return SbcCreationResponseE.ERROR
      })

  return {
    createSbcRegistration,
    getDocumentsForRegistration,
    getRegistrations,
    getRegistration,
    getRegistrationHistory,
    getLtsa,
    getAutoApproval
  }
}
