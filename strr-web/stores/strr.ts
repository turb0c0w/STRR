import { z } from 'zod'
import axios from 'axios'
import { CreateAccountFormStateI, OrgI, SecondaryContactInformationI } from '~/interfaces/account-i'

const apiURL = useRuntimeConfig().public.strrApiURL
const axiosInstance = addAxiosInterceptors(axios.create())

export const submitCreateAccountForm = (
  userFirstName: string,
  userLastName: string,
  userFullName: string,
  mailingAddress: {
    city: string;
    country: string;
    postalCode: string;
    region: string;
    street: string;
    streetAdditional: string;
  }[] | undefined,
  addSecondaryContact: boolean
) => {
  const formData: CreateAccountFormAPII = formStateToApi(
    formState,
    userFirstName,
    userLastName,
    userFullName,
    mailingAddress,
    addSecondaryContact
  )

  axiosInstance.post<CreateAccountFormAPII>(`${apiURL}/registrations`,
    { ...formData }
  )
    .then((response) => {
      const data = response?.data
      if (!data) { throw new Error('Invalid AUTH API response') }
      return data
    })
    .catch((error: string) => {
      console.warn('Error creating account.')
      console.error(error)
    })
}

const numbersRegex = /^[0-9]+$/
// matches chars 123456789 ()
const phoneRegex = /^[0-9*#+() -]+$/
const httpRegex = /^https?:/
const phoneError = { message: 'Valid characters are "()- 123457890" ' }
const requiredPhone = z.string().regex(phoneRegex, phoneError)
const requiredNumber = z.string().regex(numbersRegex, { message: 'Must be a number' })
const optionalOrEmptyString = z.string().optional().transform(e => e === '' ? undefined : e)
const requiredURL = z.string().regex(httpRegex, { message: 'Must begin with http' })
const requiredNonEmptyString = z.string().refine(e => e !== '')

export const contactSchema = z.object({
  preferredName: optionalOrEmptyString,
  phoneNumber: requiredPhone,
  extension: optionalOrEmptyString,
  faxNumber: optionalOrEmptyString,
  emailAddress: requiredNonEmptyString,
  address: requiredNonEmptyString,
  country: requiredNonEmptyString,
  addressLineTwo: optionalOrEmptyString,
  city: requiredNonEmptyString,
  province: requiredNonEmptyString,
  postalCode: requiredNonEmptyString,
  birthDay: requiredNumber.refine(day => day.length === 2, 'Day must be two digits'),
  birthMonth: requiredNonEmptyString,
  birthYear: requiredNumber
    .refine(year => Number(year) <= new Date().getFullYear(), 'Year must be in the past')
    .refine(year => year.length === 4, 'Year must be four digits')
})

export const secondaryContactSchema = z.object({
  firstName: requiredNonEmptyString,
  lastName: requiredNonEmptyString,
  middleName: requiredNonEmptyString,
  preferredName: optionalOrEmptyString,
  phoneNumber: requiredPhone,
  extension: optionalOrEmptyString,
  faxNumber: optionalOrEmptyString,
  emailAddress: requiredNonEmptyString,
  address: requiredNonEmptyString,
  country: requiredNonEmptyString,
  addressLineTwo: optionalOrEmptyString,
  city: requiredNonEmptyString,
  province: requiredNonEmptyString,
  postalCode: requiredNonEmptyString,
  birthDay: requiredNumber
    .refine(day => day.length === 2, 'Day must be two digits')
    .refine(day => Number(day) <= 31, 'Must be less than or equal to 31'),
  birthMonth: requiredNonEmptyString,
  birthYear: requiredNumber
    .refine(year => Number(year) <= new Date().getFullYear(), 'Year must be in the past')
    .refine(year => year.length === 4, 'Year must be four digits')
})

const primaryContact: ContactInformationI = {
  preferredName: '',
  phoneNumber: undefined,
  extension: '',
  faxNumber: '',
  emailAddress: undefined,
  address: undefined,
  country: undefined,
  addressLineTwo: undefined,
  city: undefined,
  province: undefined,
  postalCode: undefined,
  birthDay: undefined,
  birthMonth: undefined,
  birthYear: undefined
}

const secondaryContact: SecondaryContactInformationI = {
  preferredName: '',
  phoneNumber: undefined,
  extension: '',
  faxNumber: '',
  emailAddress: undefined,
  address: undefined,
  country: undefined,
  addressLineTwo: undefined,
  city: undefined,
  province: undefined,
  postalCode: undefined,
  birthDay: undefined,
  birthMonth: undefined,
  birthYear: undefined,
  firstName: undefined,
  lastName: undefined,
  middleName: undefined
}

export const propertyDetailsSchema = z.object({
  address: requiredNonEmptyString,
  addressLineTwo: optionalOrEmptyString,
  businessLicense: optionalOrEmptyString,
  city: requiredNonEmptyString,
  country: requiredNonEmptyString,
  listingDetails: z
    .array(
      z
        .object({ url: requiredNonEmptyString })
        .refine(({ url }) => url !== '')
    )
    .refine(arr => arr.length > 0),
  nickname: optionalOrEmptyString,
  ownershipType: requiredNonEmptyString,
  parcelIdentifier: optionalOrEmptyString,
  postalCode: requiredNonEmptyString,
  propertyType: requiredNonEmptyString,
  province: requiredNonEmptyString,
  useMailing: z.boolean()
})

export const formState: CreateAccountFormStateI = reactive({
  primaryContact,
  secondaryContact,
  propertyDetails: {
    parcelIdentifier: undefined,
    businessLicense: undefined,
    propertyType: undefined,
    ownershipType: undefined,
    primaryResidence: undefined,
    whichPlatform: undefined,
    useMailing: false,
    nickname: '',
    country: 'CAN',
    address: undefined,
    addressLineTwo: undefined,
    city: undefined,
    province: 'BC',
    postalCode: undefined,
    listingDetails: [{ url: '' }]
  },
  selectedAccount: {} as OrgI
})

const primaryContactAPI: ContactAPII = {
  name: {
    firstName: '',
    middleName: '',
    lastName: ''
  },
  dateOfBirth: '',
  details: {
    preferredName: '',
    phoneNumber: '',
    extension: '',
    faxNumber: '',
    emailAddress: ''
  },
  mailingAddress: {
    address: '',
    addressLineTwo: '',
    city: '',
    postalCode: '',
    province: '',
    country: ''
  }
}

const secondaryContactAPI: ContactAPII = {
  name: {
    firstName: '',
    middleName: '',
    lastName: ''
  },
  dateOfBirth: '',
  details: {
    preferredName: '',
    phoneNumber: '',
    extension: '',
    faxNumber: '',
    emailAddress: ''
  },
  mailingAddress: {
    address: '',
    addressLineTwo: '',
    city: '',
    postalCode: '',
    province: '',
    country: ''
  }
}

export const formDataForAPI: CreateAccountFormAPII = {
  selectedAccount: {
    name: '',
    mailingAddress: {
      street: '',
      streetAdditional: '',
      city: '',
      postalCode: '',
      region: '',
      country: ''
    }
  },
  registration: {
    primaryContact: primaryContactAPI,
    secondaryContact: secondaryContactAPI,
    unitAddress: {
      address: '',
      addressLineTwo: '',
      city: '',
      postalCode: '',
      province: '',
      country: ''
    },
    unitDetails: {
      parcelIdentifier: '',
      businessLicense: '',
      propertyType: '',
      ownershipType: ''
    },
    listingDetails: []
  }
}
