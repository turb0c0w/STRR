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
  postalCode: z.string(),
  day: z.string(),
  month: z.string(),
  year: z.string()
})

const primaryContact = {
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
  postalCode: '',
  dateOfBirth: {
    day: '',
    month: '',
    year: ''
  }
}

const secondaryContact = {
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
  postalCode: '',
  dateOfBirth: {
    day: '',
    month: '',
    year: ''
  }
}

export const formState = reactive({
  primaryContact,
  secondaryContact,
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
