import { z } from 'zod'
import { CreateAccountFormStateI, OrgI } from '~/interfaces/account-i'

export const contactSchema = z.object({
  preferredName: z.string().optional(),
  phoneNumber: z.number({ invalid_type_error: "Phone number must be a number" }),
  extension: z.string().optional(),
  faxNumber: z.string().optional(),
  emailAddress: z.string(),
  address: z.string(),
  country: z.string(),
  addressLineTwo: z.string().optional(),
  city: z.string(),
  province: z.string(),
  postalCode: z.string(),
  birthDay: z.number({ invalid_type_error: "Day must be a number" }),
  birthMonth: z.string(),
  birthYear: z.number({ invalid_type_error: "Year must be a number" }).lt(new Date().getFullYear())
})

const primaryContact: ContactInformationI = {
  preferredName: '',
  phoneNumber: null,
  extension: '',
  faxNumber: '',
  emailAddress: null,
  address: null,
  country: null,
  addressLineTwo: null,
  city: null,
  province: null,
  postalCode: null,
  birthDay: null,
  birthMonth: null,
  birthYear: null
}

const secondaryContact: ContactInformationI = {
  preferredName: '',
  phoneNumber: null,
  extension: '',
  faxNumber: '',
  emailAddress: null,
  address: null,
  country: null,
  addressLineTwo: null,
  city: null,
  province: null,
  postalCode: null,
  birthDay: null,
  birthMonth: null,
  birthYear: null
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
    parcelIdentifier: null,
    businessLicense: null,
    propertyType: null,
    ownershipType: null,
    primaryResidence: null,
    whichPlatform: null,
    useMailing: false,
    nickname: '',
    country: null,
    address: null,
    addressLineTwo: null,
    city: null,
    province: null,
    postalCode: null,
    listingDetails: [null],
  },
  selectedAccount: {} as OrgI
})
