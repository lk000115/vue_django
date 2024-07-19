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
            name:'detail',
            path:'/detail',
            component:()=>import('../views/detail/detail.vue') 
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
     linkActiveClass:'active',
  
  })
  
  export  default router