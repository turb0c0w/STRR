import axios from 'axios'

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

  const createSbcRegistration = (registration: any) => axiosInstance.post<string>(`${apiURL}/account/sbc`,
    registration
  )
    .then((res) => {
      if (res.data.length === 0) {
        navigateTo('/create-account')
      }
    })

  return {
    createSbcRegistration,
    getRegistrations
  }
}
