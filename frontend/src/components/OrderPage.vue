<template>
  <v-container>
    <v-row>
      <v-col cols="8">
        <h5 class="text-h5 mb-2">Meals</h5>
        <v-card outlined>
          <MealList id="meal-list" :meals="session.menu" />
        </v-card>
      </v-col>
      <v-col cols="4">
        <h5 class="text-h5 mb-2">Orders</h5>
        <v-card outlined class="px-3">
          <OrderList id="order-list" :users="session.users" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { Session } from "@/api/apiTypes";
import MealList from "@/components/MealList.vue";
import OrderList from "@/components/OrderList.vue";

export default Vue.extend({
  name: "OrderPage",
  components: { OrderList, MealList },
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

<style scoped lang="sass">
.order-button
  min-width: 8em !important

#order-list, #order-list ul
  margin: 0
  list-style: none
</style>
