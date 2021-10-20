export interface Session {
  id: string,
  name: string,
  organizer: User,
  menu?: Meal[],
  users?: User[]
}

export interface Meal {
  id: string,
  name: string,
  description?: string
  price: number
  info?: ProductInfo
}

export interface ProductInfo {
  text: string
}

export interface User {
  id: string,
  name: string,
  orders?: Meal[]
}