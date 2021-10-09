<template>
<v-app>
  <v-app-bar
      app
      color="primary"
      dark
    >
      <v-app-bar-title>GroupFood</v-app-bar-title>

      <v-spacer/>

      <span>{{ username }}</span>
  </v-app-bar>
  <v-content>
    <router-view></router-view>
  </v-content>
</v-app>
</template>

<script>
export default {
  name: "App",
  data () {
    return {
      'username': "Username"
    }
  }
};
</script>
