import { OrgI } from '~/interfaces/account-i'

export interface QuestionsI {
  primaryResidence: string;
  whichPlatform: string;
}

export interface FormStateI {
  primaryContact: ContactI;
  secondaryContact?: ContactI;
  questions: QuestionsI;
  selectedAccount: OrgI;
}
