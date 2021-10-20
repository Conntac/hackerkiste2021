<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-title>GroupFood</v-app-bar-title>

      <v-spacer />

      <span v-if="username !== ''">{{ username }}</span>
    </v-app-bar>
    <v-content v-if="currentSession">
      <WelcomePage v-if="currentPage === 0" :session="currentSession" @name="handleWelcomePage"/>
      <OrderPage v-if="currentPage === 1" :session="currentSession" />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import WelcomePage from "@/components/WelcomePage.vue";
import LocalStorageApiClient from "@/api/localStorageApiClient";
import { ApiClient } from "@/api/apiClient";
import Vue from "vue";
import OrderPage from '@/components/OrderPage.vue'
import { Session } from '@/api/apiTypes'

export default Vue.extend({
  name: "App",
  components: { OrderPage, WelcomePage },
  data() {
    return {
      currentSession: null as Session | null,
      username: "",
      apiClient: new LocalStorageApiClient() as ApiClient,
      currentPage: 0,
    };
  },
  async created () {
    this.currentSession = await this.apiClient.getSession(this.$route.params['sessionId'])
  },
  methods: {
    handleWelcomePage(name: string) {
      this.username = name
      this.currentPage = 1
    }
  }
});
</script>
