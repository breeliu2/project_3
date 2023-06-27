import { createRouter, createWebHistory } from 'vue-router'
import DoctorAI from '../components/DoctorAI.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/doctorai',
      name: 'Doctor.AI',
      component: DoctorAI
    }
  ]
})
export default router
