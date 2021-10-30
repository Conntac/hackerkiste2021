<template>
  <div>
    <UserOrderDisplay
      v-for="user in usersHavingOrders"
      :key="user.id"
      :user="user"
    />
  </div>
</template>
<script lang="ts">
import Vue, { PropType } from "vue";
import { User } from "@/api/apiTypes";
import UserOrderDisplay from "@/components/UserOrderDisplay.vue";

export default Vue.extend({
  name: "OrderList",
  components: {
    UserOrderDisplay,
  },
  props: {
    users: Array as PropType<Array<User>>,
  },
  computed: {
    usersHavingOrders(): User[] {
      return (
        this.users?.filter(
          (user: User) => user.orders !== undefined && user.orders.length > 0
        ) ?? []
      );
    },
  },
});
</script>
<style scoped lang="sass">
#order-list, #order-list ul
  margin: 0
  list-style: none
</style>
