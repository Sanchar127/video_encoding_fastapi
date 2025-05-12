import { createRouter, createWebHistory, RouteRecordRaw, viewDepthKey } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import EncodeProfilesPage from '../views/EncodeProfilesPage.vue';
import AdminDashBoardPage from '../views/AdminDashBoardPage.vue';
import SuperAdminDashBoardPage from '../views/SuperAdminDashBoardPage.vue';
import ViewProfiles from '../views/encodeProfile/ViewProfiles.vue';
import Edit from '../views/encodeProfile/[id]/Edit.vue';
import EditUser from '../views/user/EditUser.vue';
import New from '../views/epDeatails/new.vue';
import Edit from '../views/epDeatails/Edit.vue';
import JobList from '../views/job/JobList.vue';

const routes: RouteRecordRaw[] = [
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/adDashboard', name: 'AdminDashBoard', component: AdminDashBoardPage },
  { path: '/sadDashboard', name: 'SuperAdminDashBoard', component: SuperAdminDashBoardPage },
  {path: '/encodeProfiles', name: 'EncodeProfiles', component:EncodeProfilesPage},
  {path:'/editUser',name:'Viewuser',component:EditUser},
  {path:'/viewEncodeProfiles',name:'Viewprofiles',component:ViewProfiles},
  {path:'/updateEncodeProfiles/:id', name:'Update  EncodeProfiles', component:Edit},
  {path:'/new/EncodeProfileDetails',name:'New Encode Profile Deatils', component:New},
 {path:'/edit/EncodeProfilesDetails',name:'Edit Encode Profile Details', component:Edit},
 {path:'/job/jobList',name:'view Job list and retry failJob',component:JobList}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
