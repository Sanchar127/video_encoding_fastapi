import { createRouter, createWebHistory, RouteRecordRaw, viewDepthKey } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import EncodeProfilesPage from '../views/EncodeProfilesPage.vue';
import AdminDashBoardPage from '../views/AdminDashBoardPage.vue';
import SuperAdminDashBoardPage from '../views/SuperAdminDashBoardPage.vue';
import Edit from '../views/user/[id]/edit.vue';
import ViewUser from '../views/user/ViewUser.vue';
import ViewProfiles from '../views/encodeProfile/ViewProfiles.vue';
import Edit from '../views/encodeProfile/[id]/Edit.vue';

const routes: RouteRecordRaw[] = [
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/adDashboard', name: 'AdminDashBoard', component: AdminDashBoardPage },
  { path: '/sadDashboard', name: 'SuperAdminDashBoard', component: SuperAdminDashBoardPage },
  {path: '/encodeProfiles', name: 'EncodeProfiles', component:EncodeProfilesPage},
  {path:'/updateUser/:id',name:'Update',component:Edit},
  {path:'/viewUser',name:'Viewuser',component:ViewUser},
  {path:'/viewEncodeProfiles',name:'Viewprofiles',component:ViewProfiles},
  {path:'/updateEncodeProfiles/:id', name:'Update  EncodeProfiles', component:Edit}
  
 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
