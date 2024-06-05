import { FormPageI } from '~/interfaces/form/form-page-i'

const steps: FormPageI[] = [
  {
    step: {
      label: 'create-account.step-title.contact',
      inactiveIconPath: '/icons/create-account/add_person.svg',
      activeIconPath: '/icons/create-account/add_person_active.svg',
      complete: false,
      isValid: false,
      alt: 'Add contacts'
    },
    title: 'create-account.contact.title',
    subtitle: 'create-account.contact.subtitle',
    formTitle: 'create-account.contact.primary',
    sections: []
  },
  {
    step: {
      label: 'create-account.step-title.property',
      inactiveIconPath: '/icons/create-account/add_location.svg',
      activeIconPath: '/icons/create-account/add_location_active.svg',
      complete: false,
      isValid: false,
      alt: 'Add properties'
    },
    title: 'create-account.details.title',
    subtitle: 'create-account.details.subtitle',
    formTitle: 'create-account.details.primary',
    sections: []
  },
  {
    step: {
      label: 'create-account.step-title.eligibility',
      inactiveIconPath: '/icons/create-account/upload_file.svg',
      activeIconPath: '/icons/create-account/upload_file_active.svg',
      complete: false,
      isValid: false,
      alt: 'Upload documents'
    },
    title: 'create-account.eligibility.title',
    subtitle: '',
    formTitle: 'create-account.eligibility.primary',
    sections: []
  },
  {
    step: {
      label: 'create-account.step-title.review',
      inactiveIconPath: '/icons/create-account/check.svg',
      activeIconPath: '/icons/create-account/check_active.svg',
      complete: false,
      isValid: false,
      alt: 'Check and verify'
    },
    title: 'create-account.confirm.title',
    subtitle: '',
    formTitle: 'create-account.confirm.primary',
    sections: []
  }
]

export default steps
