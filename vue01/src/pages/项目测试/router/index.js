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
          path:'/',
          redirect: '/index' 
        },
  
     ],
     linkActiveClass:'selected'
  
  })
  
  export  default router