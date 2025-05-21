<template>
  <DefaultLayout>
    <div class="max-w-md mx-auto mt-10 bg-white shadow-md rounded-2xl p-6">
      <h2 class="text-2xl font-bold mb-4 text-center text-gray-800">Blacklist User</h2>

      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label for="user" class="block text-sm font-medium text-gray-700">Select User</label>
          <select
            id="user"
            v-model="selectedUserId"
            class="mt-1 block w-full rounded-xl border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 px-4 py-2"
          >
            <option disabled value="">-- Select a user --</option>
            <option v-for="user in users" :key="user.id" :value="user.unique_id">
               {{ user.name }} - {{ user.email }}
            </option>
          </select>
        </div>
        <input
  type="Number"
  v-model="duration"
  class="mt-1 block w-full rounded-xl border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 px-4 py-2"
  placeholder="Duration in minutes"
/>

        <button
          type="submit"
          class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-xl transition"
        >
          Blacklist
        </button>

     
      </form>
    </div>
  </DefaultLayout>
</template>

<script>
import axios from "axios";
import DefaultLayout from '../../layout/DefaultLayout.vue';
import { useToast } from 'vue-toastification';
import Cookies from 'js-cookie';


const toast = useToast();

const apiUrl = 'http://localhost:8084';

export default {
  components: { DefaultLayout },

  data() {
    return {
      users: [],
      selectedUserId: "",
      errorMessage: "",
      successMessage: "",
      duration: "",
    };
  },

  mounted() {
    this.fetchUsers();
  },

  methods: {
    async fetchUsers() {
      try {
        const res = await axios.get(`${apiUrl}/users`);
        this.users = res.data;
      } catch (error) {
        console.error(error);
        this.errorMessage = "Failed to fetch users.";
      }
    },

    async submitForm() {
      this.errorMessage = "";
      this.successMessage = "";

      if (!this.selectedUserId) {
        this.errorMessage = "Please select a user to blacklist.";
        return;
      }
  
      try {
          const accessToken = Cookies.get('access_token'); 
          console.log('this access token')
          console.log(accessToken)
        await axios.post(`${apiUrl}/users/blacklist-token`, null, {
  params: {
    user_id: this.selectedUserId,
    duration_minutes: this.duration,
  },
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  }
});


        this.successMessage = "User successfully blacklisted.";
        this.selectedUserId = "";
        toast.success('User successfully blacklisted.');
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || "Error blacklisting user.";
        console.log(this.errorMessage); 
        toast.error(errorMessage);
      }
    },
  },
};

</script>


