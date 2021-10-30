<template>
  <v-list class="py-0">
    <template v-for="(meal, index) in meals">
      <v-divider v-bind:key="index" v-if="index !== 0" />
      <MealItem :key="'li' + meal.id" :meal="meal" />
    </template>
  </v-list>
</template>
<script lang="ts">
import MealItem from "@/components/MealItem.vue";
import Vue, { PropType } from "vue";
import { Meal } from "@/api/apiTypes";

export default Vue.extend({
  name: "MealList",
  components: { MealItem },
  props: {
    meals: Array as PropType<Array<Meal>>,
  },
});
</script>
<style scoped lang="sass">
.order-button
  min-width: 8em !important
</style>
