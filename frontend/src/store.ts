import Vue from "vue";

class Store {
  public username: string | null = null;
}

const storeInstance = Vue.observable(new Store());

export default storeInstance;
