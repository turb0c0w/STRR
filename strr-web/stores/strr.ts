import { z } from 'zod'
import { CreateAccountFormStateI, OrgI } from '~/interfaces/account-i'

export const contactSchema = z.object({
  preferredName: z.string().optional(),
  phoneNumber: z.string(),
  extension: z.string().optional(),
  faxNumber: z.string().optional(),
  emailAddress: z.string(),
  address: z.string(),
  country: z.string(),
  addressLineTwo: z.string().optional(),
  city: z.string(),
  province: z.string(),
  postalCode: z.string(),
  birthDay: z.string(),
  birthMonth: z.string(),
  birthYear: z.string()
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
  parcelIdentifier: z.string(),
  businessLicense: z.string(),
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
    country: undefined,
    address: undefined,
    addressLineTwo: undefined,
    city: undefined,
    province: undefined,
    postalCode: undefined,
    listingDetails: ['']
  },
  selectedAccount: {} as OrgI
})
