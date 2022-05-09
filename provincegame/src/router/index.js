import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../HomePage.vue')
  },
  // {
  //   path: '/anhui',
  //   name: 'anhui',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../test/AnHui.vue')
  // }
  {
    path: '/pricepage',
    name: 'pricepage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../PricePage')
  },
  {
    path: '/testpage',
    name: 'testpage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../HuNan')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router