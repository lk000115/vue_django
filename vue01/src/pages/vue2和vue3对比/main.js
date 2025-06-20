import { createApp } from "vue";
import App from './App.vue'
import {createPinia} from 'pinia'
import '@/assets/font/iconfont.css'
import router from './router/index'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import Antd from 'ant-design-vue';
const app = createApp(App)


for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(Antd)
app.use(ElementPlus)
app.use(createPinia())
app.use(router)
app.mount('#app')