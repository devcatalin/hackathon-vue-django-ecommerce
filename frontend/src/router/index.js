import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';

import ProductList from '../views/ProductList.vue';
import ProductDetail from '../views/ProductDetail.vue';
import ProductCreate from '../views/ProductCreate.vue';

import ShoppingCart from '../views/ShoppingCart.vue'

import SellerProducts from '../views/SellerProducts.vue'
import MyAccount from '../views/MyAccount.vue'
import AdminControl from '../views/AdminControl.vue'


Vue.use(VueRouter)

const routes = [{
    path: '/',
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
    path: '/products/detail/:slug',
    name: 'product_detail',
    component: ProductDetail
  },
  {
    path: '/products/create',
    name: 'product_create',
    component: ProductCreate
  },
  {
    path: '/shopping-cart',
    name: 'shopping_cart',
    component: ShoppingCart
  },
  {
    path: '/seller-products',
    name: 'seller_products',
    component: SellerProducts
  },
  {
    path: '/my-account',
    name: 'my_account',
    component: MyAccount
  },
  {
    path: '/admin-control',
    name: 'admin_control',
    component: AdminControl
  },
  {
    path: '*',
    redirect: '/',
    name: 'home'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// router.beforeEach((to, from, next) => {
//   let web = ["home", "login", "register"];
//   if(web.includes(to.name)){
//       next();
//   }else{
//     let token = localStorage.getItem('token');
//     if (token) {
//       next();
//     } else {
//       router.push({
//         name: 'login'
//       });
//     }
//   }
// });

export default router
