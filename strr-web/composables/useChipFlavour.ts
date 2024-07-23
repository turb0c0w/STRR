export const useChipFlavour = () => {
  const t = useNuxtApp().$i18n.t
  const tRegistryDashboardStatus = (translationKey: string) => t(`registry-dashboard.statusChip.${translationKey}`)

  const getChipFlavour = (status: string): StatusChipFlavoursI['flavour'] => {
    switch (status) {
      case 'DENIED':
        return {
          text: tRegistryDashboardStatus('denied'),
          alert: AlertsFlavourE.ALERT
        }
      case 'APPROVED':
        return {
          alert: AlertsFlavourE.SUCCESS,
          text: tRegistryDashboardStatus('approved')
        }
      case 'REJECTED':
        return {
          alert: AlertsFlavourE.ALERT,
          text: tRegistryDashboardStatus('rejected')
        }
      case 'PENDING':
        return {
          alert: AlertsFlavourE.WARNING,
          text: tRegistryDashboardStatus('provisional')
        }
      case 'UNDER_REVIEW':
        return {
          alert: AlertsFlavourE.APPLIED,
          text: tRegistryDashboardStatus('underReview')
        }
      default:
        return {
          alert: AlertsFlavourE.MESSAGE,
          text: ''
        }
    }
  }

  return { getChipFlavour }
}