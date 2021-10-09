import { Session, User } from '@/api/apiTypes'

export interface ApiClient {
  getSession(sessionId: string): Promise<Session>
  createUser(sessionId: string, username: string): Promise<User>
  submitOrder(sessionId: string, userId: string, mealId: string): Promise<void>
}