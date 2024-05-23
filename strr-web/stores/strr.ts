import { z } from 'zod'
import { CreateAccountFormStateI, OrgI } from '~/interfaces/account-i'

export const primaryContactSchema = z.object({
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

export const formState: CreateAccountFormStateI = reactive({
  preferredName: null,
  phoneNumber: null,
  extension: null,
  faxNumber: null,
  emailAddress: null,
  address: null,
  country: null,
  addressLineTwo: null,
  city: null,
  province: null,
  postalCode: null,
  birthDay: null,
  birthMonth: null,
  birthYear: null,
  secondaryContactPreferredName: null,
  secondaryContactPhoneNumber: null,
  secondaryContactExtension: null,
  secondaryContactFaxNumber: null,
  secondaryContactEmailAddress: null,
  secondaryContactAddress: null,
  secondaryContactCountry: null,
  secondaryContactAddressLineTwo: null,
  secondaryContactCity: null,
  secondaryContactProvince: null,
  secondaryContactPostalCode: null,
  secondaryContactBirthDay: null,
  secondaryContactBirthMonth: null,
  secondaryContactBirthYear: null,
  questions: {
    primaryResidence: null,
    whichPlatform: null
  },
  unitDetails: {
    parcelIdentifier: null,
    businessLicense: null,
    propertyType: null,
    ownershipType: null
  },
  unitAddress: {
    useMailing: false,
    nickname: null,
    country: null,
    address: null,
    addressLineTwo: null,
    city: null,
    province: null,
    postalCode: null
  },
  listingDetails: [null],
  selectedAccount: {} as OrgI
})
