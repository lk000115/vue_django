//引入createRouter
import {createRouter,createWebHashHistory} from 'vue-router'
import Home from '@/pages/Home.vue'
import News from '@/pages/News.vue'
import About from '@/pages/About.vue'
//创建路由器

const router = createRouter({
  history:createWebHashHistory(), 
   routes:[
       {
         path:'/home',
         component: Home
       },
       {
        path:'/news',
        component: News
      },
      {
        path:'/about',
        component: About
      }

   ]

})

export  default router

