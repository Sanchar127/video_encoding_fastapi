
import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const toastOptions: PluginOptions = {
    position: 'top-center',  
    timeout: 2000, 
  };
  
const app = createApp(App);

app.use(router);
app.use(Toast,toastOptions); 
app.mount('#app');
