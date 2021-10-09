import WelcomePage from "./components/WelcomePage.vue";
import HelloWorld from "./components/HelloWorld.vue";
import VueRouter from "vue-router";

const routes = [
  { path: "/", redirect: { name: "welcome" } },
  {
    name: "welcome",
    path: "/welcome",
    component: WelcomePage,
  },
  {
    name: "hello",
    path: "/hello",
    component: HelloWorld,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
