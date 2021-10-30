<template>
  <v-list-item>
    <v-list-item-content>
      <v-list-item-title>{{ meal.name }}</v-list-item-title>
      <v-list-item-subtitle>{{ meal.description }}</v-list-item-subtitle>
    </v-list-item-content>
    <v-list-item-action>
      <v-btn @click="this.$emit('click')" color="primary" class="order-button">
        <v-icon left>mdi-basket-plus</v-icon>
        {{ mealPrice }}
      </v-btn>
    </v-list-item-action>
  </v-list-item>
</template>
<script lang="ts">
import Vue, { PropType } from "vue";
import { Meal } from "@/api/apiTypes";

import { eurosToString } from "@/format";

export default Vue.extend({
  name: "MealItem",
  props: {
    meal: Object as PropType<Meal>,
  },
  computed: {
    mealPrice(): string {
      return eurosToString(this.meal.price / 100);
    },
  },
});
</script>
<style scoped lang="sass">
.order-button
  min-width: 8em !important
</style>
