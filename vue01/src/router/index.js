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
         name:'myhome',
         path:'/home',
         component: Home
       },
       {
        name:'xinwen',
        path:'/news',
        component: News
      },
      {
        name:'guanyu',
        path:'/about',
        component: About
      }

   ]

})

export  default router

