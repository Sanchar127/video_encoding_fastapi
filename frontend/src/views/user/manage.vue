<template>
  <DefaultLayout>
    <div class="min-h-screen  py-8 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <!-- Header Section -->
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
          <div>
            <h1 class="text-2xl md:text-3xl font-bold text-gray-900">User Management</h1>
            <p class="mt-1 text-sm text-gray-500">Manage all registered users and their permissions</p>
          </div>
          <div class="flex gap-3 w-full sm:w-auto">
            <div class="relative flex-grow sm:flex-grow-0 sm:w-64">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
              </div>
              <input
                type="text"
                class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                placeholder="Search users..."
              />
            </div>
            <button class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              <PlusIcon class="-ml-1 mr-2 h-5 w-5" />
              Add User
            </button>
          </div>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <div class="flex items-center">
                <div class="flex-shrink-0 bg-indigo-500 rounded-md p-3">
                  <UsersIcon class="h-6 w-6 text-white" />
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Total Users</dt>
                    <dd class="flex items-baseline">
                      <div class="text-2xl font-semibold text-gray-900">1223</div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <div class="flex items-center">
                <div class="flex-shrink-0 bg-green-500 rounded-md p-3">
                  <CheckCircleIcon class="h-6 w-6 text-white" />
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Active Users</dt>
                    <dd class="flex items-baseline">
                      <div class="text-2xl font-semibold text-gray-900">1,042</div>
                      <div class="ml-2 flex items-baseline text-sm font-semibold text-green-600">
                        <ArrowTrendingUpIcon class="h-4 w-4" />
                        <span class="sr-only">Increased by</span>
                        12%
                      </div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <div class="flex items-center">
                <div class="flex-shrink-0 bg-yellow-500 rounded-md p-3">
                  <ExclamationTriangleIcon class="h-6 w-6 text-white" />
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Black listed User</dt>
                    <dd class="flex items-baseline">
                      <div class="text-2xl font-semibold text-gray-900">30</div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <div class="flex items-center">
                <div class="flex-shrink-0 bg-blue-500 rounded-md p-3">
                  <BellAlertIcon class="h-6 w-6 text-white" />
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Notifications Enabled</dt>
                    <dd class="flex items-baseline">
                      <div class="text-2xl font-semibold text-gray-900">932</div>
                      <div class="ml-2 flex items-baseline text-sm font-semibold text-blue-600">
                        <span>75%</span>
                      </div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Main Table -->
        <div class="bg-white shadow overflow-hidden sm:rounded-lg">
          <div class="flex flex-col">
            <!-- Table Filters -->
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center px-6 py-4 border-b border-gray-200">
              <div class="flex items-center space-x-4 mb-4 sm:mb-0">
                <div class="relative">
                  <select class="appearance-none block w-full pl-3 pr-10 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-white">
                    <option>All Roles</option>
                    <option>Admin</option>
                    <option>User</option>
                    <option>Manager</option>
                  </select>
                  <div class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
                    <ChevronDownIcon class="h-5 w-5 text-gray-400" />
                  </div>
                </div>
                <div class="relative">
                  <select class="appearance-none block w-full pl-3 pr-10 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-white">
                    <option>All Statuses</option>
                    <option>Active</option>
                    <option>Inactive</option>
                  </select>
                  <div class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
                    <ChevronDownIcon class="h-5 w-5 text-gray-400" />
                  </div>
                </div>
              </div>
              <div class="flex items-center space-x-3">
                <button type="button" class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  <ArrowDownTrayIcon class="-ml-0.5 mr-2 h-4 w-4" />
                  Export
                </button>
                <div class="relative" x-data="{ open: false }">
                  <button @click="open = !open" type="button" class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <FunnelIcon class="-ml-0.5 mr-2 h-4 w-4" />
                    Columns
                    <ChevronDownIcon class="ml-1.5 -mr-1 h-5 w-5 text-gray-400" />
                  </button>
                </div>
              </div>
            </div>

            <!-- Responsive Table Container -->
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                  <tr>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Contact</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Notifications</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Integration</th>
                    <th scope="col" class="relative px-6 py-3">
                      <span class="sr-only">Actions</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50 transition-colors duration-150">
                    <!-- User Column -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="flex-shrink-0 h-10 w-10">
                          <div class="h-10 w-10 rounded-full bg-indigo-100 flex items-center justify-center">
                            <UserIcon class="h-6 w-6 text-indigo-600" />
                          </div>
                        </div>
                        <div class="ml-4">
                          <div class="text-sm font-medium text-gray-900">{{ user.name }}</div>
                          <div class="text-sm text-gray-500">ID: {{ user.id }}</div>
                        </div>
                      </div>
                    </td>
                    
                    <!-- Contact Column -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">
                        <a :href="`mailto:${user.email}`" class="flex items-center text-indigo-600 hover:text-indigo-900">
                          <EnvelopeIcon class="flex-shrink-0 mr-1.5 h-4 w-4" />
                          {{ user.email }}
                        </a>
                      </div>
                      <div v-if="user.mobile" class="text-sm text-gray-500 mt-1 flex items-center">
                        <PhoneIcon class="flex-shrink-0 mr-1.5 h-4 w-4" />
                        {{ user.mobile }}
                      </div>
                    </td>
                    
                    <!-- Role Column -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span :class="{
                        'bg-purple-100 text-purple-800': user.role === 'admin',
                        'bg-green-100 text-green-800': user.role === 'user',
                        'bg-blue-100 text-blue-800': user.role === 'manager'
                      }" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full capitalize">
                        {{ user.role }}
                      </span>
                    </td>
                    
                    <!-- Status Column -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span :class="user.is_activated ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                        {{ user.is_activated ? 'Active' : 'Inactive' }}
                      </span>
                      <div v-if="user.last_login" class="text-xs text-gray-500 mt-1">
                        Last login: {{ formatDate(user.last_login) }}
                      </div>
                    </td>
                    
                    <!-- Notifications Column -->
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <span :class="user.email_notification ? 'text-green-500' : 'text-gray-400'" class="mr-2">
                          <BellIcon class="h-5 w-5" />
                        </span>
                        <span class="text-sm text-gray-500">
                          {{ user.email_notification ? 'Enabled' : 'Disabled' }}
                        </span>
                      </div>
                    </td>
                    
                    <!-- Integration Column -->
                    <td class="px-6 py-4">
                      <div class="text-sm text-gray-900 truncate max-w-[180px]" :title="user.callback_url || 'Not configured'">
                        <span v-if="user.callback_url" class="flex items-center text-indigo-600">
                          <LinkIcon class="flex-shrink-0 mr-1 h-4 w-4" />
                          {{ truncateUrl(user.callback_url) }}
                        </span>
                        <span v-else class="text-gray-400">—</span>
                      </div>
                    </td>
                    
                    <!-- Actions Column -->
                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <div class="flex justify-end space-x-3">
                        <button @click="openEditModal(user)" class="text-indigo-600 hover:text-indigo-900">
                          <PencilSquareIcon class="h-5 w-5" />
                        </button>
                        <button class="text-gray-500 hover:text-gray-700">
                          <EllipsisVerticalIcon class="h-5 w-5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Pagination -->
            <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
              <div class="flex-1 flex justify-between sm:hidden">
                <a href="#" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"> Previous </a>
                <a href="#" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"> Next </a>
              </div>
              <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                <div>
                  <p class="text-sm text-gray-700">
                    Showing
                    <span class="font-medium">1</span>
                    to
                    <span class="font-medium">10</span>
                    of
                    <span class="font-medium">97</span>
                    results
                  </p>
                </div>
                <div>
                  <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                    <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                      <span class="sr-only">Previous</span>
                      <ChevronLeftIcon class="h-5 w-5" />
                    </a>
                    <a href="#" aria-current="page" class="z-10 bg-indigo-50 border-indigo-500 text-indigo-600 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 1 </a>
                    <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 2 </a>
                    <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"> 3 </a>
                    <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                      <span class="sr-only">Next</span>
                      <ChevronRightIcon class="h-5 w-5" />
                    </a>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Edit User Modal -->
      <div v-if="showEditModal" class="fixed z-50 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="closeEditModal"></div>

          <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

          <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full sm:p-6">
            <div class="absolute top-0 right-0 pt-4 pr-4">
              <button type="button" class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" @click="closeEditModal">
                <span class="sr-only">Close</span>
                <XMarkIcon class="h-6 w-6" />
              </button>
            </div>
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-indigo-100 sm:mx-0 sm:h-10 sm:w-10">
                <UserIcon class="h-6 w-6 text-indigo-600" />
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">Edit User</h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">Update user details and permissions below.</p>
                </div>
              </div>
            </div>
            <div class="mt-5">
              <form @submit.prevent="saveUser">
                <div class="space-y-6">
                  <!-- Basic Information Section -->
                  <div>
                    <h4 class="text-md font-medium text-gray-900 mb-3">Basic Information</h4>
                    <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                      <div class="sm:col-span-3">
                        <label for="name" class="block text-sm font-medium text-gray-700">Full name</label>
                        <input 
                          v-model="editingUser.name"
                          type="text" 
                          id="name"
                          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          required
                        >
                      </div>

                      <div class="sm:col-span-3">
                        <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                        <input 
                          v-model="editingUser.email"
                          type="email" 
                          id="email"
                          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                          required
                        >
                      </div>

                      <div class="sm:col-span-3">
                        <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile number</label>
                        <input 
                          v-model="editingUser.mobile"
                          type="tel" 
                          id="mobile"
                          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        >
                      </div>

                      <div class="sm:col-span-3">
                        <label for="role" class="block text-sm font-medium text-gray-700">Role</label>
                        <select 
                          v-model="editingUser.role"
                          id="role"
                          class="mt-1 block w-full bg-white border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        >
                          <option value="admin">Admin</option>
                          <option value="user">User</option>
                          <option value="manager">Manager</option>
                        </select>
                      </div>

                      <div class="sm:col-span-6">
                        <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
                        <textarea 
                          v-model="editingUser.address"
                          id="address"
                          rows="3"
                          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        ></textarea>
                      </div>
                    </div>
                  </div>

                  <!-- Account Status Section -->
                  <div>
                    <h4 class="text-md font-medium text-gray-900 mb-3">Account Status</h4>
                    <div class="space-y-4">
                      <div class="relative flex items-start">
                        <div class="flex items-center h-5">
                          <input 
                            v-model="editingUser.is_activated"
                            id="isActive" 
                            type="checkbox" 
                            class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                          >
                        </div>
                        <div class="ml-3 text-sm">
                          <label for="isActive" class="font-medium text-gray-700">Account is active</label>
                          <p class="text-gray-500">User will be able to login if enabled.</p>
                        </div>
                      </div>
                      <div class="relative flex items-start">
                        <div class="flex items-center h-5">
                          <input 
                            v-model="editingUser.email_notification"
                            id="emailNotifications" 
                            type="checkbox" 
                            class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                          >
                        </div>
                        <div class="ml-3 text-sm">
                          <label for="emailNotifications" class="font-medium text-gray-700">Email notifications</label>
                          <p class="text-gray-500">User will receive email notifications if enabled.</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Integration Settings Section -->
                  <div>
                    <h4 class="text-md font-medium text-gray-900 mb-3">Integration Settings</h4>
                    <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                      <div class="sm:col-span-6">
                        <label for="callback_url" class="block text-sm font-medium text-gray-700">Callback URL</label>
                        <div class="mt-1 flex rounded-md shadow-sm">
                          <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">
                            <LinkIcon class="h-5 w-5 text-gray-400" />
                          </span>
                          <input 
                            v-model="editingUser.callback_url"
                            type="url" 
                            id="callback_url"
                            class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            placeholder="https://example.com/callback"
                          >
                        </div>
                      </div>

                      <div class="sm:col-span-3">
                        <label for="callback_key" class="block text-sm font-medium text-gray-700">API Key</label>
                        <div class="mt-1 flex rounded-md shadow-sm">
                          <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">
                            <KeyIcon class="h-5 w-5 text-gray-400" />
                          </span>
                          <input 
                            v-model="editingUser.callback_key"
                            type="text" 
                            id="callback_key"
                            class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            placeholder="Your API key"
                          >
                        </div>
                      </div>

                      <div class="sm:col-span-3">
                        <label for="callback_secret_key" class="block text-sm font-medium text-gray-700">Secret Key</label>
                        <div class="mt-1 flex rounded-md shadow-sm">
                          <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm">
                            <LockClosedIcon class="h-5 w-5 text-gray-400" />
                          </span>
                          <input 
                            v-model="editingUser.callback_secret_key"
                            type="password" 
                            id="callback_secret_key"
                            class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            placeholder="Your secret key"
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-8 flex justify-end space-x-3">
                  <button 
                    type="button"
                    @click="closeEditModal"
                    class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Cancel
                  </button>
                  <button 
                    type="submit"
                    class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Save Changes
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import {
  // Heroicons
  UserIcon,
  UsersIcon,
  EnvelopeIcon,
  PhoneIcon,
  LinkIcon,
  KeyIcon,
  LockClosedIcon,
  BellIcon,
  XMarkIcon,
  PencilSquareIcon,
  EllipsisVerticalIcon,
  MagnifyingGlassIcon,
  PlusIcon,
  CheckCircleIcon,
  ExclamationTriangleIcon,
  BellAlertIcon,
  ArrowTrendingUpIcon,
  ChevronDownIcon,
  FunnelIcon,
  ArrowDownTrayIcon,
  ChevronLeftIcon,
  ChevronRightIcon
} from '@heroicons/vue/24/outline'

const apiUrl = 'http://localhost:8084'
const users = ref<any[]>([])
const toast = useToast()

const showEditModal = ref(false)
const editingUser = ref<any>({
  id: '',
  name: '',
  email: '',
  mobile: '',
  address: '',
  role: 'user',
  is_activated: false,
  email_notification: false,
  callback_url: '',
  callback_key: '',
  callback_secret_key: ''
})

// Helper functions
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString()
}

const truncateUrl = (url: string) => {
  if (!url) return ''
  return url.length > 30 ? url.substring(0, 30) + '...' : url
}

const fetchUsers = async () => {
  try {
    const res = await axios.get(`${apiUrl}/users`)
    users.value = res.data
  } catch (error: any) {
    toast.error('Failed to fetch user data: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

const openEditModal = (user: any) => {
  editingUser.value = JSON.parse(JSON.stringify(user)) // Deep copy
  showEditModal.value = true
}

const closeEditModal = () => {
  showEditModal.value = false
}

const saveUser = async () => {
  try {
    await axios.put(`${apiUrl}/users/update`, {
      ...editingUser.value,
      email_notification_status: editingUser.value.email_notification,
    }, {
      params: { user_id: editingUser.value.unique_id }
    })

    toast.success('User updated successfully')
    fetchUsers() // Refresh the user list
    closeEditModal()
  } catch (error: any) {
    toast.error('Failed to update user: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>