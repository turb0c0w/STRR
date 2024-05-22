import { reactive } from 'vue'
import { useRuntimeConfig } from '#app'
import type { CanadaPostAddressI, CanadaPostResponseAddressI } from '#imports'

export const useCanadaPostAddress = () => {
  const address = reactive<CanadaPostAddressI>({
    street: '',
    streetAdditional: '',
    city: '',
    region: '',
    postalCode: '',
    country: '',
    deliveryInstructions: ''
  })

  const createAddressComplete = (pca: any, key: string, element_prefix:string): object => {
    const fields = [
      { element: element_prefix + '_street', field: 'Line1', mode: pca.fieldMode.SEARCH },
      { element: 'CA', field: 'CountryName', mode: pca.fieldMode.COUNTRY }
    ]
    console.log(fields)
    const options = { key }
    const addressComplete = new pca.Address(fields, options)
    addressComplete.listen('populate', addressCompletePopulate)
    return addressComplete
  }

  const enableAddressComplete = (element_prefix: string): void => {
    const config = useRuntimeConfig()
    const pca = (window as any).pca
    const key = config.public.addressCompleteKey
    if (!pca || !key) {
      console.log('AddressComplete not initialized due to missing script and/or key')
      return
    }
    if ((window as any).currentAddressComplete) {
      console.log('destroy');
      (window as any).currentAddressComplete.destroy()
    }
    (window as any).currentAddressComplete = createAddressComplete(pca, key, element_prefix)
  }

  const addressCompletePopulate = (addressComplete: CanadaPostResponseAddressI): void => {
    address.street = addressComplete.Line1 || 'N/A'
    address.city = addressComplete.City
    address.region = addressComplete.ProvinceCode
    address.postalCode = addressComplete.PostalCode
    address.country = addressComplete.CountryName
  }

  return {
    address,
    enableAddressComplete
  }
}
