<template>
  <v-container>
    <v-card
        out>
      <v-card-title>
        Session Name
      </v-card-title>
      <v-card-subtitle>
        Organized by Name
      </v-card-subtitle>

      <v-card-text>
        <v-form>
          <v-col>
            <v-text-field v-model="name" label="Please enter your name" required/>
            <v-row justify="center">
              <v-btn
                  color="primary"
              >
                Next
              </v-btn>
            </v-row>
          </v-col>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "WelcomePage",
  data () {
    return {
      "name": ""
    };
  }
};
</script>

<style scoped>

</style>