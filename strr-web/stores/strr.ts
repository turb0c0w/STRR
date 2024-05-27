import { z } from 'zod'
import { CreateAccountFormStateI, OrgI } from '~/interfaces/account-i'

const numbersRegex = /^[0-9]+$/
// matches chars 123456789 ()
const phoneRegex = /^[0-9*#+() -]+$/
const phoneError = { message: 'Valid characters are "()- 123457890" ' }
const requiredPhone = z.string().regex(phoneRegex, phoneError)
const requiredNumber = z.string().regex(numbersRegex, { message: 'Must be a number' })
const optionalOrEmptyString = z.string().optional().transform(e => e === '' ? undefined : e)

export const contactSchema = z.object({
  preferredName: optionalOrEmptyString,
  phoneNumber: requiredPhone,
  extension: optionalOrEmptyString,
  faxNumber: optionalOrEmptyString,
  emailAddress: z.string(),
  address: z.string(),
  country: z.string(),
  addressLineTwo: optionalOrEmptyString,
  city: z.string(),
  province: z.string(),
  postalCode: z.string(),
  birthDay: requiredNumber.refine(day => day.length === 2, 'Day must be two digits'),
  birthMonth: z.string(),
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

const secondaryContact: ContactInformationI = {
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

export const propertyDetailsSchema = z.object({
  parcelIdentifier: optionalOrEmptyString,
  businessLicense: optionalOrEmptyString,
  propertyType: z.string(),
  ownershipType: z.string(),
  primaryResidence: z.string(),
  whichPlatform: z.string(),
  useMailing: z.string(),
  nickname: z.string(),
  country: z.string(),
  address: z.string(),
  addressLineTwo: z.string(),
  city: z.string(),
  province: z.string(),
  postalCode: z.string(),
  listingDetails: z.array(z.string())
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
  dateOfBirth: {
    date: ''
  },
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
  dateOfBirth: {
    date: ''
  },
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
