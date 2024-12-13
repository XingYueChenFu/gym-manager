import { createRouter, createWebHistory } from 'vue-router'
import DashBoardView from '../views/DashBoardView.vue'
import SearchView from '../views/SearchView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/main', name: 'dashboard', component: DashBoardView, },
    // { path: '/main', name: 'dashboard', component: () => import('../views/DashBoardView.vue'), },
    { path: '/search', name: 'search', component: SearchView, },
    // { path: '/search', name: 'search', component: () => import('../views/SearchView.vue'), },
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
