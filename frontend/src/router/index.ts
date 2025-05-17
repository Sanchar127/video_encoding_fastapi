import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';

// Import your views
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
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard
router.beforeEach((to, from, next) => {
  const token = Cookies.get('access_token');

  if (to.meta.requiresAuth) {
    if (!token) {
      return next({ path: '/' });
    }

    try {
      const decoded: DecodedToken = jwtDecode(token);
      const isExpired = decoded.exp * 1000 < Date.now();

      if (isExpired) {
        Cookies.remove('access_token');
        return next({ path: '/' });
      }

      // Role-based access (optional)
      if (to.path.includes('/admin') && decoded.role !== 'admin' && decoded.role !== 'super_admin') {
        return next({ path: '/' });
      }

      if (to.path.includes('/superadmin') && decoded.role !== 'super_admin') {
        return next({ path: '/' });
      }

    } catch (err) {
      Cookies.remove('access_token');
      return next({ path: '/' });
    }
  }

 
  if (to.path === '/' && token) {
    try {
      const decoded: DecodedToken = jwtDecode(token);
      if (decoded.role === 'super_admin') {
        return next('/superadmin/dashboard');
      } else if (decoded.role === 'admin') {
        return next('/admin/dashboard');
      }
    } catch {
      Cookies.remove('access_token');
    }
  }

  return next();
});

export default router;
