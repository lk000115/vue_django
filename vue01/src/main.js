import { createApp } from 'vue'
// import './style.css'

//导入element
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

//导入路由
import router from './router/index'

//设定启动的APP入口组件
import App from './App.vue'


const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
