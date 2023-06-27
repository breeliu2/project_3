import Vue, { createApp } from '@vue/compat';
import App from './App.vue'
import router from './router'
import 'bootstrap'

// Based on ref from https://bootstrap-vue.org/docs making BootstrapVue available throughout the project for style
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

const app = createApp(App)

app.use(router)

Vue.use(BootstrapVue)

app.mount('#app')
