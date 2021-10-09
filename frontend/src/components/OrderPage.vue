<template>
  <v-container>
    <v-row v-for="food in foods" v-bind:key="food.id">
        <v-col>{{food.name}}</v-col>
        <v-col>{{food.desc}}</v-col>
        <v-col><v-btn @click="sendOrder(food.id)" color="primary">Order</v-btn></v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "OrderPage",
  data() {
    return {
      foods: [
      { id: '1-food', name: 'Pizza', desc: 'Pineapple Pizza' },
      { id: '2-food', name: 'Chicken Tikka', desc: 'Spicy' },
      { id: '3-food', name: 'Black Salmon', desc: 'Lachs' }
    ]
    };
  },
  methods: {
      sendOrder (foodId: string) {
        console.log(foodId);
      }
    }
});
</script>

<style scoped></style>
