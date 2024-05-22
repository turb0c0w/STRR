import { z } from 'zod'
import { OrgI } from '~/interfaces/account-i'

export const primaryContactSchema = z.object({
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
  postalCode: z.string()
})

export const formState = reactive({
  dateOfBirth: {
    day: '',
    month: '',
    year: ''
  },
  primaryContact: {
    preferredName: '',
    phoneNumber: '',
    extension: '',
    faxNumber: '',
    emailAddress: '',
    address: '',
    country: '',
    addressLineTwo: '',
    city: '',
    province: '',
    postalCode: ''
  },
  secondaryContact: {
    email: '',
    phone: '',
    phoneExtension: ''
  },
  questions: {
    primaryResidence: '',
    whichPlatform: ''
  },
  unitDetails: {
    parcelIdentifier: '',
    businessLicense: '',
    propertyType: '',
    ownershipType: ''
  },
  unitAddress: {
    nickname: '',
    country: '',
    address: '',
    addressLineTwo: '',
    city: '',
    province: '',
    postalCode: ''
  },
  listingDetails: {
    urlOne: '',
    urlTwo: ''
  },
  selectedAccount: {} as OrgI
})
