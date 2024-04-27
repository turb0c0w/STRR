import { describe, it, expect } from 'vitest'
import { VueWrapper, mount } from '@vue/test-utils'
import { BcrosExistingAccountsList } from '#components'
import { existingAccountList } from '@/tests/unit/utils/mockedData'

describe('Existing Accounts List tests', () => {
  let wrapper: VueWrapper<any>

  beforeEach(() => { wrapper = mount(BcrosExistingAccountsList) })
  afterEach(() => { wrapper.unmount() })

  //TODO: TC - use the mocked data
  // inject empty existingAccountList
  //Check for existance of fields per row, or not per row

})
