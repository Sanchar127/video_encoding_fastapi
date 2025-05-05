<template >
   <DefaultLayout>

     <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
       <div class="w-full max-w-2xl p-8 bg-white rounded-lg shadow-md">
         <h2 class="text-3xl font-semibold text-gray-800 mb-6 text-center">Create New  User</h2>
   
        <form @submit.prevent="onSubmit" class="space-y-5">
  
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name</label>
      <div class="relative">
        <svg class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A7 7 0 0112 15a7 7 0 016.879 2.804M12 11a4 4 0 100-8 4 4 0 000 8z"/>
        </svg>
        <Field
          id="name"
          name="name"
          type="text"
          class="w-full pl-10 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <ErrorMessage name="name" class="text-red-500 text-sm mt-1" />
    </div>

    <div>
      <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
      <div class="relative">
        <svg  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none">
  <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
</svg>

        <Field
          id="email"
          name="email"
          type="email"
          class="w-full pl-10 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <ErrorMessage name="email" class="text-red-500 text-sm mt-1" />
    </div>
  </div>

  <!-- Row 2: Password & Mobile -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
      <Field
        id="password"
        name="password"
        type="password"
        class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
   
      <ErrorMessage name="password" class="text-red-500 text-sm mt-1" />
    </div>

    <div>
      <label for="mobile" class="block text-sm font-medium text-gray-700 mb-1">Mobile</label>
      
      <div class="relative">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none">
  <path fill-rule="evenodd" d="M15 3.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 .75.75v4.5a.75.75 0 0 1-1.5 0V5.56l-4.72 4.72a.75.75 0 1 1-1.06-1.06l4.72-4.72h-2.69a.75.75 0 0 1-.75-.75Z" clip-rule="evenodd" />
  <path fill-rule="evenodd" d="M1.5 4.5a3 3 0 0 1 3-3h1.372c.86 0 1.61.586 1.819 1.42l1.105 4.423a1.875 1.875 0 0 1-.694 1.955l-1.293.97c-.135.101-.164.249-.126.352a11.285 11.285 0 0 0 6.697 6.697c.103.038.25.009.352-.126l.97-1.293a1.875 1.875 0 0 1 1.955-.694l4.423 1.105c.834.209 1.42.959 1.42 1.82V19.5a3 3 0 0 1-3 3h-2.25C8.552 22.5 1.5 15.448 1.5 6.75V4.5Z" clip-rule="evenodd" />
</svg>

<Field
    id="mobile"
    name="mobile"
    type="text"
    class="w-full px-10 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
  />

</div>

<!-- Good design of it -->



      <ErrorMessage name="mobile" class="text-red-500 text-sm mt-1" />
    </div>
  </div>

  <!-- Remaining fields -->
  <div v-for="field in fields.slice(4)" :key="field.name">
    <label :for="field.name" class="block text-sm font-medium text-gray-700 mb-1">
      {{ field.label }}
    </label>
 
    <Field
      v-if="field.type !== 'select'"
      :id="field.name"
      :name="field.name"
      :type="field.type"
      class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
    <Field
      v-else
      as="select"
      :name="field.name"
      :id="field.name"
      class="w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
    >
      <option value="" disabled>Select role</option>
      <option value="super_admin">Super Admin</option>
      <option value="admin">Admin</option>
      <option value="user">User</option>
    </Field>
    <ErrorMessage :name="field.name" class="text-red-500 text-sm mt-1" />
  </div>

  <button
    type="submit"
    :disabled="isSubmitting"
    class="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition duration-200 disabled:opacity-50"
  >
    {{ isSubmitting ? 'Submitting...' : 'Submit' }}
  </button>
</form>

       </div>
     </div>
   </DefaultLayout>
</template>

<!-- i want better desin of the form doesnot change other part -->
<script setup lang="ts">
import { Field, ErrorMessage, useForm } from 'vee-validate'


import * as yup from 'yup';
import DefaultLayout from '@/layout/DefaultLayout.vue';


const schema = yup.object({
  name: yup
    .string()
    .required('Name is required')
    .min(2, 'Name must be at least 2 characters'),

  email: yup
    .string()
    .email('Invalid email format')
    .required('Email is required'),

  password: yup
    .string()
    .required('Password is required')
    .min(8, 'Password must be at least 8 characters')
    .matches(/[a-z]/, 'Password must contain at least one lowercase letter')
    .matches(/[A-Z]/, 'Password must contain at least one uppercase letter')
    .matches(/\d/, 'Password must contain at least one number')
    .matches(/[@$!%*#?&]/, 'Password must contain at least one special character'),

  mobile: yup
    .string()
    .required('Mobile number is required')
    .matches(/^[6-9]\d{9}$/, 'Invalid  mobile number'), 

  address: yup
    .string()
    .required('Address is required')
    .min(5, 'Address must be at least 5 characters'),

  callback_key: yup
    .string()
    .required('Callback Key is required'),

  callback_url: yup
    .string()
    .required('Callback URL is required')
    .url('Must be a valid URL'),

  callback_secret_key: yup
    .string()
    .required('Callback Secret Key is required'),

  role: yup
    .string()
    .required('Role is required')
    .oneOf(['admin', 'user', 'super_admin'], 'Invalid role'), 
});



const { handleSubmit, isSubmitting } = useForm({
  validationSchema: schema
})


const fields = [
  { name: 'name', label: 'Name', type: 'text' },
  { name: 'email', label: 'Email', type: 'email' },
  { name: 'password', label: 'Password', type: 'password' },
  { name: 'mobile', label: 'Mobile', type: 'text' },
  { name: 'address', label: 'Address', type: 'text' },
  { name: 'callback_key', label: 'Callback Key', type: 'text' },
  { name: 'callback_url', label: 'Callback URL', type: 'text' },
  { name: 'callback_secret_key', label: 'Callback Secret Key', type: 'text' },
  { name: 'role', label: 'Role', type: 'select' },
]

const onSubmit = handleSubmit(values => {
  console.log('Form Submitted:', values)
  
})

</script>



