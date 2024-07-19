import {createRouter,createWebHashHistory} from 'vue-router'


const router = createRouter({
    history:createWebHashHistory(), 
     routes:[
         {
           name:'home',
           path:'/home',
           component: Home
         },

        {
          path:'/',
          redirect: Home
        },
  
     ],
     linkActiveClass:'selected'
  
  })
  
  export  default router