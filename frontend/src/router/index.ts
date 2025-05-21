import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';

import { useToast } from 'vue-toastification';

// Views
import LoginPage from '@/views/LoginPage.vue';
import EncodeProfilesPage from '@/views/EncodeProfilesPage.vue';
import EditUser from '@/views/user/EditUser.vue';
import NewUser from '@/views/user/new.vue';
import ManageUser from '@/views/user/manage.vue';
import EditProfiles from '@/views/encodeProfile/editProfiles.vue';
import ManageProfile from '@/views/encodeProfile/manageProfile.vue';
import NewDetails from '@/views/epDeatails/newDetails.vue';
import EditDetails from '@/views/epDeatails/EditDetails.vue';
import ManageDetails from '@/views/epDeatails/manageDetails.vue';
import JobList from '@/views/job/JobList.vue';
import AdminDashboard from '@/views/AdminDashBoardPage.vue';
import SuperAdminDashboard from '@/views/SuperAdDash.vue';
import SystemConfig from '@/views/SystemConfig.vue';
import BlackListUser from '@/views/user/BlackListUser.vue';

const toast = useToast();

interface DecodedToken {
  sub: string;
  role: string;
  exp: number;
}

const routes: RouteRecordRaw[] = [
  { path: '/', name: 'Login', component: LoginPage },
  { path: '/user/new', name: 'Create New User', component: NewUser, meta: { requiresAuth: true } },
  { path: '/user/manage', name: 'Manage User', component: ManageUser, meta: { requiresAuth: true } },
  { path: '/encodeProfiles', name: 'Encode Profiles', component: EncodeProfilesPage, meta: { requiresAuth: true } },
  { path: '/editUser', name: 'Edit User', component: EditUser, meta: { requiresAuth: true } },
  { path: '/edit/profile', name: 'Edit Profile', component: EditProfiles, meta: { requiresAuth: true } },
  { path: '/profile/manage', name: 'Manage Profile', component: ManageProfile, meta: { requiresAuth: true } },
  { path: '/new/EncodeProfileDetails', name: 'New Encode Profile Details', component: NewDetails, meta: { requiresAuth: true } },
  { path: '/edit/EncodeProfilesDetails', name: 'Edit Encode Profile Details', component: EditDetails, meta: { requiresAuth: true } },
  { path: '/ProfileDetails/manage', name: 'Manage Profile Details', component: ManageDetails, meta: { requiresAuth: true } },
  { path: '/jobList', name: 'Job List', component: JobList, meta: { requiresAuth: true } },
  { path: '/admin/dashboard', name: 'Admin Dashboard', component: AdminDashboard, meta: { requiresAuth: true } },
  { path: '/superadmin/dashboard', name: 'Super Admin Dashboard', component: SuperAdminDashboard, meta: { requiresAuth: true } },
  { path: '/systemconfig', name: 'System Config', component: SystemConfig, meta: { requiresAuth: true } },
  { path: '/blacklistUser', name: 'Black list User', component: BlackListUser, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

function isTokenExpired(exp: number): boolean {
  return exp * 1000 < Date.now();
}

router.beforeEach((to, from, next) => {
  const token = Cookies.get('access_token');

  if (to.path === '/') {
    if (token) {
      try {
        const decoded = jwtDecode<DecodedToken>(token);
        const isExpired = decoded.exp * 1000 < Date.now();
        if (isExpired) {
          Cookies.remove('access_token');
          return next(); 
        }
   
        if (decoded.role === 'super_admin') return next('/superadmin/dashboard');
        if (decoded.role === 'admin') return next('/admin/dashboard');
        return next('/jobList');
      } catch {
        Cookies.remove('access_token');
        return next();
      }
    } else {
      return next(); // no token, proceed to login
    }
  }


  if (to.meta.requiresAuth) {
    if (!token) {
      toast.error('Please log in to access this page.');
      return next({ path: '/' });
    }

    try {
      const decoded = jwtDecode<DecodedToken>(token);
      const isExpired = decoded.exp * 1000 < Date.now();
      if (isExpired) {
        Cookies.remove('access_token');
        toast.error('Session expired. Please log in again.');
        return next({ path: '/' });
      }

      const role = decoded.role;

     
      if (to.path.startsWith('/superadmin') && role !== 'super_admin') {
        toast.error('Access denied: Super Admins only can access this page .');
        return next('/'); 
      }

      if (to.path.startsWith('/admin') && role !== 'admin') {
        toast.error('Access denied: Admins only can access this page .');
        return next('/');
      }

     
      return next();
    } catch {
      Cookies.remove('access_token');
      toast.error('Invalid session. Please log in again.');
      return next({ path: '/' });
    }
  }


  return next();
});


export default router;
