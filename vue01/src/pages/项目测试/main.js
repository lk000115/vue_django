import{createApp} from 'vue'
import App from './App.vue'
// 导入公共样式
import '@/assets/css/common.css'
// 导入 iconfont 图库
import '@/assets/font/iconfont.css'
import '@/assets/css/index.css'
import router from './router/index'

const app = createApp(App)

app.use(router)
app.mount('#app')