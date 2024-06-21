import axios from 'axios'

export const useFees = () => {
  const apiURL = useRuntimeConfig().public.strrApiURL
  const axiosInstance = addAxiosInterceptors(axios.create())
  const config = useRuntimeConfig()

  const getFeeAmount = (): Promise<string> => axiosInstance.get<{ total: number }>('https://pay-api-dev.apps.silver.devops.gov.bc.ca/api/v1/fees/STRR/RENTAL_FEE')
    .then((res) => {
      return res.data.total.toString()
    })
    .finally(() => {
      return '-'
    })

  const createInvoiceRecord = (invoiceId: string, applicationId: string) => {
    axiosInstance.post(`${apiURL}/registrations/${applicationId}/invoice/${invoiceId}/paid`)
  }

  const handlePaymentRedirect = async (invoiceId: number, applicationId: number) => {
    const paymentUrl = config.public.payPortalURL
    const returnUrl = encodeURIComponent(`${window.location.href.replace('create-account', `success/${applicationId}/invoice/${invoiceId}`)}`)
    const payUrl = `${paymentUrl}/${invoiceId}/${returnUrl}`
    await navigateTo(payUrl, { external: true })
  }

  return {
    createInvoiceRecord,
    getFeeAmount,
    handlePaymentRedirect
  }
}
