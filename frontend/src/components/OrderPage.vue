<template>
  <v-container>
    <v-row v-for="meal in session.menu" v-bind:key="meal.id">
        <v-col>{{ meal.name }}</v-col>
        <v-col>{{ meal.description }}</v-col>
        <v-col>
          <v-btn @click="sendOrder(meal.id)" color="primary">Order</v-btn>
        </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Session } from "@/api/apiTypes";

export default Vue.extend({
  name: "OrderPage",
  props: {
    session: Object as () => Session,
  },
  methods: {
    sendOrder(foodId: string) {
      console.log(foodId);
    },
  },
});
</script>

<style scoped></style>
