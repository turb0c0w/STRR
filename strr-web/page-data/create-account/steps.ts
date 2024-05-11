import { FormPageI } from "~/interfaces/form/form-page-i"
import { contactInformationPage } from "./contact-page"

const steps: FormPageI[] = [
  {
    step: {
      label: 'create-account.step-title.contact',
      inactiveIconPath: '/icons/create-account/add_person.svg',
      activeIconPath: '/icons/create-account/add_person_active.svg',
      complete: false,
      error: false
    },
    title: "create-account.contact.title",
    subtitle: "create-account.contact.subtitle",
    formTitle: "create-account.contact.primary",
    sections: contactInformationPage
  },
  {
    step: {
      label: 'create-account.step-title.property',
      inactiveIconPath: '/icons/create-account/add_location.svg',
      activeIconPath: '/icons/create-account/add_location_active.svg',
      complete: false,
      error: false
    },
    title: "create-account.details.title",
    subtitle: "create-account.details.subtitle",
    formTitle: "create-account.details.primary",
    sections: []
  },
  {
    step: {
      label: 'create-account.step-title.eligibility',
      inactiveIconPath: '/icons/create-account/upload_file.svg',
      activeIconPath: '/icons/create-account/upload_file_active.svg',
      complete: false,
      error: false
    },
    title: "create-account.eligibility.title",
    subtitle: "create-account.eligibility.subtitle",
    formTitle: "create-account.eligibility.primary",
    sections: []
  },
  {
    step: {
      label: 'create-account.step-title.review',
      inactiveIconPath: '/icons/create-account/check.svg',
      activeIconPath: '/icons/create-account/check_active.svg',
      complete: false,
      error: false
    },
    title: "create-account.confirm.title",
    subtitle: "create-account.confirm.subtitle",
    formTitle: "create-account.confirm.primary",
    sections: []
  }
]

export default steps
