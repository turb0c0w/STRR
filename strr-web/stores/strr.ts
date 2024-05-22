import { z } from 'zod'
import { CreateAccountFormStateI, OrgI } from '~/interfaces/account-i'

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

const primaryContact: ContactInformationI = {
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

const secondaryContact: ContactInformationI = {
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

export const formState: CreateAccountFormStateI = reactive({
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
    urlOne: 'aaa',
    urlTwo: ''
  },
  selectedAccount: {} as OrgI
})
