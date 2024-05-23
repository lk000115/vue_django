import {createApp} from 'vue'
import App from './App.vue'
import {createPinia} from 'pinia'
import router from '../05_组件通讯/router/index'

const app = createApp(App)

const pinia = createPinia()

app.use(pinia)

app.use(router)

app.mount('#app')
