import { createRouter, createWebHistory } from 'vue-router'
import DashBoardView from '../views/DashBoardView.vue'
import SearchView from '../views/SearchView.vue'
// import MemberView from '../views/MemberAddView.vue'
import MemberAddView from '../views/MemberAddView.vue'
import MemberDetailView from '../views/MemberDetailView.vue'
import RechargeView from '../views/RechageView.vue'
import RecordView from '../views/RecordView.vue'
import ActivityView from '@/views/ActivityView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/main', name: 'dashboard', component: DashBoardView, },
    // { path: '/main', name: 'dashboard', component: () => import('../views/DashBoardView.vue'), },
    { path: '/search', name: 'search', component: SearchView, },
    { path: '/member/add', name: 'addMember', component: MemberAddView, },
    { path: '/member/detail', name: 'memberDetail', component: MemberDetailView, },
    { path: '/member/record', name: 'memberRecord', component: RecordView, },
    { path: '/member/recharge', name: 'memberRecharge', component: RechargeView, },
    { path: '/Activity', name: 'activity', component: ActivityView, },
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
