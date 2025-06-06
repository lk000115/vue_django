import { createRouter,createWebHashHistory } from "vue-router";

const routes = [

    {
        path: "/vue2",
        name:"vue2",
        component: ()=>import("../views/vue2.vue")
    },
    
    {
        path: "/vue3",
        name:"vue3",
        component: ()=>import("../views/vue3.vue")
    }

]

const router = createRouter({

   history: createWebHashHistory(),
   routes, 
})

export default router