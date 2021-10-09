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
    <WelcomeDialog />
  </v-content>
</v-app>
</template>

<script>
import WelcomeDialog from "./components/WelcomePage";
export default {
  name: "App",
  components: { WelcomeDialog },
  data () {
    return {
      'username': "Username"
    }
  }
};
</script>
