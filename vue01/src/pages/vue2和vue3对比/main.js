import { createApp } from "vue";
import App from './App.vue'
import {createPinia} from 'pinia'
import '@/assets/font/iconfont.css'
import router from './router/index'
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')