import {createRouter,createWebHashHistory} from 'vue-router'


const router = createRouter({
    history:createWebHashHistory(), 
     routes:[
         {
           name:'index',
           path:'/index',
           component:()=>import('../views/index/index.vue') 
         },
         {
            name:'home',
            path:'/home',
            component:()=>import('../views/home/home.vue') 
          },
          {
            name:'list',
            path:'/list',
            component:()=>import('../views/list/list.vue') 
          }, 
        {
          path:'/',
          redirect: '/index' 
        },
  
     ],
     linkActiveClass:'selected'
  
  })
  
  export  default router