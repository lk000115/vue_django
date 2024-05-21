import { createApp } from 'vue'
// import './style.css'
//在main.js中可以全局引入组件
// import Header from './components/Header.vue'

//导入element
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

//导入路由
import router from './router/index02.js'
//导入图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

//导入启动的APP入口组件
import App from './pages/03_hocks/app.vue'

const app = createApp(App)

//使用图标

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

//全局注册组件Header
// app.component('Header',Header)

//功能注册
app.use(router)
app.use(ElementPlus)
app.mount('#app')
