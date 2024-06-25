import axios from 'axios'
import { SbcCreationResponseE } from '~/enums/sbc-creation-response-e'

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

  const getRegistration = (id: string): Promise<string> =>
    axiosInstance.get(`${apiURL}/registrations`)
      .then((res) => {
        let selectedRegistration = '-'
        res.data.forEach((registration: any) => {
          if (registration.id.toString() === id.toString()) {
            selectedRegistration = registration
          }
        })
        return selectedRegistration
      })

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
            .then(() => {
              navigateTo(`/create-account-pre/${res.data.sbc_account_id}`)
            })
          return res.data
        } else {
          return SbcCreationResponseE.ERROR
        }
      })
      .then((data) => {
        if (data !== SbcCreationResponseE.ERROR) {
          navigateTo(`/create-account-pre/${data.sbc_account_id}`)
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
    getRegistrations,
    getRegistration
  }
}
