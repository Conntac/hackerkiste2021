<template>
  <v-container>
      <v-row>
        <v-col cols="9">
          <v-card outlined>
            <v-list class="py-0">
              <template v-for="(meal, index) in session.menu" >
                <v-divider v-bind:key="index" v-if="index !== 0"/>

                <v-list-item v-bind:key="'li' + meal.id">
                  <v-list-item-content>
                    <v-list-item-title>{{ meal.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ meal.description }}</v-list-item-subtitle>
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn @click="sendOrder(meal.id)" color="primary" class="order-button">
                      <v-icon left>mdi-basket-plus</v-icon>
                      {{toCurrency(meal.price)}}
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
              </template>
            </v-list>
          </v-card>
        </v-col>
        <v-col cols="3">

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
  data() {
  return {
    numberFormatter: new Intl.NumberFormat(undefined, {style: "currency", currency: "EUR"})
  };
},
  methods: {
    sendOrder(foodId: string) {
      console.log(foodId);
    },
    toCurrency(value: number) {
      return this.numberFormatter.format((value / 100));
    }
  }
});
</script>

<style scoped lang="sass">
.order-button
  min-width: 8em !important
</style>
