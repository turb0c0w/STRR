import { DropdownItem } from "@nuxt/ui/dist/runtime/types/dropdown";

export interface DropdownItemWithValueI extends DropdownItem {
  value: string | number
}