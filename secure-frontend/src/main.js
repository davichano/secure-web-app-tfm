import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia';
import axios from 'axios';
import Vue from 'vue';
import {sanitize} from '@/helpers/sanitize';

const app = createApp(App);
const pinia = createPinia();

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';

Vue.filter('sanitize', (value) => sanitize(value));

app.use(router);
app.use(pinia);
app.mount('#app');
