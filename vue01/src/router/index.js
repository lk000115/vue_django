//引入createRouter
import {createRouter,createWebHashHistory} from 'vue-router'
import Home from '@/pages/01_路由组件/Home.vue'
import News from '@/pages/01_路由组件/News.vue'
import About from '@/pages/01_路由组件/About.vue'
import Detail from '@/pages/01_路由组件/Detail.vue'
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
        component: News,
        children:[
          { 
            name:"xq",
            path:'detail',
            component: Detail
          }  
        ]
      },
      {
        name:'guanyu',
        path:'/about',
        component: About
      }

   ]

})

export  default router

