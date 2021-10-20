import Vue from "vue";
import { Session } from '@/api/apiTypes'

class Store {
  public username: string | null = null;
  public currentSession: Session | null = null;
}

const storeInstance = Vue.observable(new Store());

export default storeInstance;
