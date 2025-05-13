import { createRouter, createWebHistory, RouteRecordRaw, viewDepthKey } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import EncodeProfilesPage from '../views/EncodeProfilesPage.vue';
import AdminDashBoardPage from '../views/AdminDashBoardPage.vue';
import SuperAdminDashBoardPage from '../views/SuperAdminDashBoardPage.vue';
import EditUser from '../views/user/EditUser.vue';
import New from '../views/epDeatails/newDetails.vue';
import JobList from '../views/job/JobList.vue';
import New from '../views/user/new.vue';
import Manage from '../views/user/manage.vue';
import EditProfiles from '../views/encodeProfile/editProfiles.vue';
import ManageProfile from '../views/encodeProfile/manageProfile.vue';
import NewDetails from '../views/epDeatails/newDetails.vue';
import EditDetails from '../views/epDeatails/EditDetails.vue';
import ManageDetails from '../views/epDeatails/manageDetails.vue';
import LoginPage from '../views/LoginPage.vue';

const routes: RouteRecordRaw[] = [
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/user/new', name: 'create new user', component: New },
  {path: '/encodeProfiles', name: 'EncodeProfiles', component:EncodeProfilesPage},
  {path:'/editUser',name:'Viewuser',component:EditUser},
  {path:'/edit/profile',name:'Viewprofiles',component:EditProfiles},
  {path:'/new/EncodeProfileDetails',name:'New Encode Profile Deatils', component:NewDetails},
 {path:'/edit/EncodeProfilesDetails',name:'Edit Encode Profile Details', component:EditDetails},
 {path:'/jobList',name:'view Job list and retry failJob',component:JobList},
 {path:'/user/manage',name:'Manage User Dashboard',component:Manage},
 {path:'/profile/manage',name:'Manage Encode Profile Dashboard',component:ManageProfile},
 {path:'/ProfileDetails/manage',name:'Manage Profile Details Dashboard',component:ManageDetails}

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
