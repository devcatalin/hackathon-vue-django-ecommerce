import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';

import ProductList from '../views/ProductList.vue';
import ProductDetail from '../views/ProductDetail.vue';

Vue.use(VueRouter)

const routes = [{
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/products',
    name: 'product_list',
    component: ProductList
  },
  {
    path: '/products/:slug',
    name: 'product_detail',
    component: ProductDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
