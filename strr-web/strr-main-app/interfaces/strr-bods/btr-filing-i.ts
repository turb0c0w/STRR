import { BtrBodsEntityI } from '~/interfaces/strr-bods/btr-bods-entity-i'
import { BtrBodsPersonI } from '~/interfaces/strr-bods/btr-bods-person-i'
import { BtrBodsOwnershipOrControlI } from '~/interfaces/strr-bods/btr-bods-ownership-or-control-i'

export interface BtrFilingI {
    businessIdentifier: string
    effectiveDate: string
    entityStatement: BtrBodsEntityI
    personStatements: BtrBodsPersonI[]
    ownershipOrControlStatements: BtrBodsOwnershipOrControlI[]
}
