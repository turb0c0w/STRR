import { z } from 'zod'
import axios from 'axios'
import {
  CreateAccountFormStateI,
  OrgI,
  PrimaryContactInformationI,
  SecondaryContactInformationI
} from '~/interfaces/account-i'

const apiURL = useRuntimeConfig().public.strrApiURL
const axiosInstance = addAxiosInterceptors(axios.create())
const fileAxiosInstance = addAxiosInterceptors(axios.create(), 'multipart/form-data')
const { handlePaymentRedirect } = useFees()

export const submitCreateAccountForm = (
  userFirstName: string,
  userLastName: string,
  selectedAccountId: string,
  addSecondaryContact: boolean,
  propertyType: string,
  ownershipType: string
) => {
  const formData: CreateAccountFormAPII = formStateToApi(
    formState,
    userFirstName,
    userLastName,
    selectedAccountId,
    addSecondaryContact,
    propertyType,
    ownershipType
  )
  axiosInstance.post(`${apiURL}/registrations`,
    { ...formData }
  )
    .then((response) => {
      const data = response?.data
      if (!data) { throw new Error('Invalid AUTH API response') }
      return data
    })
    .then((data) => {
      formState.supportingDocuments.forEach((file: File) => {
        fileAxiosInstance.post<File>(`${apiURL}/registrations/${data.id}/documents`, { file })
      })
      return data
    })
    .then((data) => {
      const { invoices } = data
      handlePaymentRedirect(invoices[0].invoice_id, data.id)
    })
    .catch((error: string) => {
      console.warn('Error creating account.')
      console.error(error)
    })
}

const numbersRegex = /^[0-9]+$/
// matches chars 123456789 ()
const phoneRegex = /^[0-9*#+() -]+$/
const httpRegex = /^(https?:\/\/)([\w-]+(\.[\w-]+)+\.?(:\d+)?(\/.*)?)$/i
const emailRegex = /^\S+@\S+\.\S+$/
const pidRegex = /^\d{3}(-)\d{3}(-)\d{3}$/
const sinRegex = /^\d{3}( )\d{3}( )\d{3}$/
const phoneError = { message: 'Valid characters are "()- 123457890" ' }
const emailError = { message: 'Email must contain @ symbol and domain' }
const requiredPhone = z.string().regex(phoneRegex, phoneError)
const requiredEmail = z.string().regex(emailRegex, emailError)
const requiredNumber = z.string().regex(numbersRegex, { message: 'Must be a number' })
const optionalNumber = z.string().regex(numbersRegex, { message: 'Must be a number' }).optional()
const optionalPID = z
  .string()
  .regex(pidRegex, { message: 'If provided this value must be in the format 111-111-111' }).optional()
const requiredSin = z
  .string()
  .regex(sinRegex, { message: 'Social Insurance Number must be provided in the format 111 111 111' })
const optionalExtension = optionalNumber
const optionalOrEmptyString = z.string().optional().transform(e => e === '' ? undefined : e)
const requiredNonEmptyString = z.string().refine(e => e !== '', 'Field cannot be empty')

export const finalizationSchema = z.object({
  phone: requiredPhone,
  phoneExtension: optionalExtension,
  email: requiredEmail,
  name: requiredNonEmptyString
})

export const primaryContactSchema = z.object({
  preferredName: optionalOrEmptyString,
  socialInsuranceNumber: requiredSin,
  businessNumber: optionalOrEmptyString,
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
    .refine(day => Number(day) <= 31, 'Date must be less than or equal to 31')
    .refine(day => Number(day) > 0, 'Date must be less greater to 0'),
  birthMonth: requiredNonEmptyString,
  birthYear: requiredNumber
    .refine(year => Number(year) <= new Date().getFullYear(), 'Year must be in the past')
    .refine(year => year.length === 4, 'Year must be four digits')
    .refine(day => Number(day) > 0, 'Year must be greater than 0')
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
  birthDay: optionalNumber
    .refine(day => day?.length === 2, 'Day must be two digits')
    .refine(day => Number(day) <= 31, 'Must be less than or equal to 31')
    .optional(),
  birthMonth: optionalOrEmptyString,
  birthYear: optionalNumber
    .refine(year => Number(year) <= new Date().getFullYear(), 'Year must be in the past')
    .refine(year => year?.length === 4, 'Year must be four digits')
    .optional()
})

const primaryContact: PrimaryContactInformationI = {
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
  socialInsuranceNumber: '',
  businessNumber: undefined
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

// If any listing details exist must follow httpRegex otherwise can be blank
const listingDetailsSchema =
  z
    .array(
      z
        .object({
          url:
            z
              .string()
              .refine(value => httpRegex
                .test(value ?? ''), 'Invalid URL format')
              .or(
                z
                  .string()
                  .refine(value => value === '')
              )
        })
    )

export const propertyDetailsSchema = z.object({
  address: requiredNonEmptyString,
  addressLineTwo: optionalOrEmptyString,
  businessLicense: optionalOrEmptyString,
  city: requiredNonEmptyString,
  country: requiredNonEmptyString,
  listingDetails: listingDetailsSchema,
  nickname: optionalOrEmptyString,
  ownershipType: requiredNonEmptyString,
  parcelIdentifier: optionalPID,
  postalCode: requiredNonEmptyString,
  propertyType: requiredNonEmptyString,
  province: requiredNonEmptyString
    .refine(province => province === 'BC', { message: 'Province must be set to BC' }),
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
  selectedAccount: {} as OrgI,
  principal: {
    isPrincipal: undefined,
    reason: undefined,
    declaration: false,
    agreeToSubmit: false
  },
  supportingDocuments: []
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
    sbc_account_id: ''
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
    principalResidence: {
      isPrincipalResidence: false,
      agreedToRentalAct: false,
      nonPrincipalOption: '',
      specifiedServiceProvider: '',
      agreedToSubmit: false
    }
  }
}
