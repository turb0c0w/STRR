import { RegistrationI } from './registration-i'

export interface PaginatedRegistrationsI {
  count: number,
  results: RegistrationI[]
}
