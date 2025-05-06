import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import EncodeProfilesPage from '../views/EncodeProfilesPage.vue';
import AdminDashBoardPage from '../views/AdminDashBoardPage.vue';
import SuperAdminDashBoardPage from '../views/SuperAdminDashBoardPage.vue';

const routes: RouteRecordRaw[] = [
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/adDashboard', name: 'AdminDashBoard', component: AdminDashBoardPage },
  { path: '/sadDashboard', name: 'SuperAdminDashBoard', component: SuperAdminDashBoardPage },
  {path: '/encodeProfiles', name: 'EncodeProfiles', component:EncodeProfilesPage},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
