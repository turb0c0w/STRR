import { OrgI } from '~/interfaces/account-i'

export const formState = reactive({
  dateOfBirth: {
    day: '',
    month: '',
    year: ''
  },
  primaryContact: {
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
