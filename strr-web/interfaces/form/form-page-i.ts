import { SectionI } from './section-i'
import { StepI } from './step-i'

export interface FormPageI {
  step: StepI
  title: string,
  subtitle: string,
  formTitle: string,
  sections: SectionI[]
}
