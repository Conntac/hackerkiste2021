<template>
  <div>
    <div class="d-flex justify-space-between">
      <b class="username">{{ user.name }}</b>
      <span class="total-price">{{ eurosToString(totalPrice / 100) }}</span>
    </div>
    <div class="pl-3 orders">
      <div
        v-for="meal in user.orders"
        class="d-flex justify-space-between"
        :key="meal.id"
      >
        <span>
          {{ meal.name }}
        </span>
        <span>
          {{ eurosToString(meal.price / 100) }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from "vue";
import { Meal, User } from "@/api/apiTypes";
import { eurosToString } from "@/format";

export default Vue.extend({
  name: "UserOrderDisplay",
  props: {
    user: Object as PropType<User>,
  },
  methods: {
    eurosToString,
  },
  computed: {
    totalPrice() {
      return this.user?.orders?.reduce(
        (sum: number, meal: Meal) => sum + meal.price,
        0
      );
    },
  },
});
</script>

<style scoped>
.orders > * {
  display: block;
}
</style>
