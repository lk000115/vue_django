/** 
02_路由组件的导航
入口为App02.vue,组件文件夹:02_路由组件   
*/
import { createRouter,createWebHashHistory } from "vue-router";
import Home from '@/pages/02_路由组件/Home.vue'
import News from '@/pages/02_路由组件/News.vue'
import Detail from '@/pages/02_路由组件/Detail.vue'


const router = createRouter({
     history:createWebHashHistory(),
     routes:[
       {
         name:'myhome',
         path:'/home',
         component:Home
       },
       {
          name:'xinwen',
          path:'/news',
          component:News,
          children:[
          {
            name:"xq",
            path:'detail/:id/:content?',
            component: Detail,
            props:true
            }]
        }, 
       {
          path:'/',
          redirect:'/home'
       } 

     ]

})



export default  router