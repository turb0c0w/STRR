export interface AutoApprovalDataI {
  renting: boolean | null,
  service_provider: boolean | null,
  pr_exempt: boolean | null,
  address_match: boolean | null,
  business_license_required: boolean | null,
  business_license_required_not_provided: boolean | null,
  business_license_required_provided: boolean | null,
  business_license_not_required_not_provided: boolean | null,
  title_check: boolean | null
}
