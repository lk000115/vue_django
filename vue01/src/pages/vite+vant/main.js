import { createApp } from "vue";
import App from './App.vue'

import router from './router/index'
import 'amfe-flexible'
import './static/styles/index.css'
const app = createApp(App)

app.use(router)
app.mount('#app')