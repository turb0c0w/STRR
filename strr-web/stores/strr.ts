import { defineStore } from 'pinia'
import { FormStateI, QuestionsI } from '~/interfaces/strr-i'
import { OrgI } from '~/interfaces/account-i'

export const useFormStore = defineStore({
  id: 'form',
  state: (): FormStateI => ({
    primaryContact: {
      email: '',
      phone: '',
      phoneExtension: ''
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
    selectedAccount: {} as OrgI
  }),
  getters: {
    hasSecondaryContact (state): boolean {
      return !!state.secondaryContact?.email
    },
    selectedAccountName (state): string {
      return state.selectedAccount.name || 'No account selected'
    }
  },
  actions: {
    setPrimaryContact (contact: ContactI) {
      this.primaryContact = contact
    },
    setSecondaryContact (contact: ContactI) {
      this.secondaryContact = contact
    },
    setQuestions (questions: QuestionsI) {
      this.questions = questions
    },
    setSelectedAccount (account: OrgI) {
      this.selectedAccount = account
    },
    getSelectedAccount (): OrgI {
      return this.selectedAccount
    }
  }
})
