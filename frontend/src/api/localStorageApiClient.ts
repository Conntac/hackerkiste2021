import { ApiClient } from '@/api/apiClient'
import { Session, User } from '@/api/apiTypes'
import { v4 as uuidv4 } from 'uuid'

export default class LocalStorageApiClient implements ApiClient {
  createUser(sessionId: string, username: string): Promise<User> {
    return Promise.resolve({ id: uuidv4(), name: username });
  }

  getSession(sessionId: string): Promise<Session> {
    return Promise.resolve({
      id: sessionId,
      name: "coolSession",
      organizer: {
        id: uuidv4(),
        name: "Organizer",
      },
      menu: [
        { id: "1", name: "1 Pfund Fritten", description: "3 Gramm mehr als 450 Gramm Fritten!", price: 690 },
        { id: "2", name: "Lagerfeuer", description: "Möglicherweise etwas scharf", price: 1000 },
        { id: "O51O573031", name: "Menü Avocado", price: 1480 },
      ],
    });
  }

  submitOrder(
    sessionId: string,
    userId: string,
    mealId: string
  ): Promise<void> {
    return Promise.resolve(undefined);
  }
}
