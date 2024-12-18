import { createRouter, createWebHistory } from 'vue-router'
import SignInView from '../views/SignInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/login', name: 'signin', component: SignInView },
    // { path: '/login', name: 'signin', component: () => import('../views/SignInView.vue'), },
    // {
    //   path: '/',
    //   name: 'signin',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/SignInView.vue'),
    // },
  ],
})

export default router
