export interface PaginationI {
  filter_by_status?: string,
  offset?: string,
  limit?: string,
  sort_by?: string,
  sort_desc?: string,
  search?: string
}

export enum RegistrationStatusesE {
  PENDING,
  APPROVED,
  UNDER_REVIEW,
  MORE_INFO_NEEDED,
  PROVISIONAL,
  DENIED
}
