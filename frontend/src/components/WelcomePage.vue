<template>
  <v-container>
    <v-card out>
      <v-card-title>
        {{ sessionName }}
      </v-card-title>
      <v-card-subtitle> Organized by {{ ownerName }} </v-card-subtitle>

      <v-card-text>
        <v-form ref="form" v-model="valid" @submit.prevent="onSubmit">
          <v-col>
            <v-text-field
              v-model="name"
              label="Please enter your name"
              required
              :rules="[validateName]"
            />
            <v-row justify="center">
              <v-btn color="primary" :disabled="!valid" type="submit">Next</v-btn>
            </v-row>
          </v-col>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Session } from '@/api/apiTypes'

export default Vue.extend({
  name: "WelcomePage",
  data() {
    return {
      name: "",
      valid: false,
    };
  },
  props: {
    session: Object as () => Session
  },
  computed: {
    sessionName() {
      return this.session.name;
    },
    ownerName() {
      return this.session.organizer.name;
    },
  },
  methods: {
    validateName(name: string) {
      if (name !== "") return true;

      return "Your name can not be empty";
    },
    onSubmit() {
      this.$emit('name',  this.name)
    }
  },
});
</script>

<style scoped></style>
