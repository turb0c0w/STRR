import { KeycloakConfig } from 'keycloak-js'

/** Manages auth flows */
export const useBcrosAuth = () => {
  const config = useRuntimeConfig()
  const keycloak = useBcrosKeycloak()
  const account = useBcrosAccount()
  const { redirect, goToSetupAccount, goToCreateAccount } = useBcrosNavigate()

  /** redirect to the correct creation screen based on auth state */
  function createAccount () {
    if (keycloak.kc.authenticated) {
      goToSetupAccount()
    } else {
      goToCreateAccount()
    }
  }

  /** Logout and then redirect to given page (if redirect provided). */
  async function logout (redirect: string) { await keycloak.logout(redirect) }

  /** redirect if account status is suspended */
  function verifyAccountStatus () {
    const accountStatus = account.currentAccount?.accountStatus
    if (accountStatus) {
      if ([AccountStatusE.NSF_SUSPENDED, AccountStatusE.SUSPENDED].includes(accountStatus)) {
        redirect(`${config.public.authWebURL}/account-freeze`)
      } else if (accountStatus === AccountStatusE.PENDING_STAFF_REVIEW) {
        const accountName = encodeURIComponent(btoa(account.currentAccountName || ''))
        redirect(`${config.public.authWebURL}/pendingapproval/${accountName}/true`)
      }
    }
  }

  /** Setup keycloak / user auth pieces */
  async function setupAuth (kcConfig: KeycloakConfig, currentAccountId?: string) {
    if (!keycloak.kc.authenticated) {
      console.info('Initializing auth setup...') // eslint-disable-line no-console
      // initialize keycloak with user token
      console.info('Initializing Keycloak...') // eslint-disable-line no-console
      try {
        await keycloak.initKeyCloak(kcConfig)
        if (keycloak.kc.authenticated) {
          // successfully initialized so setup other pieces
          keycloak.syncSessionStorage()
          keycloak.scheduleRefreshToken()
          // set user info
          console.info('Setting user name...') // eslint-disable-line no-console
          await account.setUserName()
          // set account info
          console.info('Setting user account information...') // eslint-disable-line no-console
          await account.setAccountInfo(currentAccountId)
          // check account status
          console.info('Checking account status...') // eslint-disable-line no-console
          // verify account status
          verifyAccountStatus()
          console.info('Auth setup complete.') // eslint-disable-line no-console
        }
      } catch (error) {
        console.warn('Keycloak initialization failed:', error) // eslint-disable-line no-console
      }
    }
  }

  return {
    createAccount,
    logout,
    setupAuth
  }
}
