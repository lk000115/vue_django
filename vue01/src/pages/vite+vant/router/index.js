import { createRouter,createWebHashHistory } from "vue-router";

const routes = [
    {
        path: "/",
        redirect:"/index",
   
    },

    {
        path: "/index",    // 首页
        name:"index",
        component: ()=>import("../views/index/index.vue")
    },
    {
        path: "/community", // 社区
        name:"community",
        component: ()=>import("../views/community/index.vue")
    },
    {
        path: "/welfare",  // 福利
        name:"welfare",
        component: ()=>import("../views/welfare/index.vue")
    },
    {
        path: "/my",  // 我的
        name:"my",
        component: ()=>import("../views/my/index.vue")
    },
    {
        path: "/login",
        name:"login",
        component: ()=>import("../views/login/index.vue")
    },

  

]

const router = createRouter({

   history: createWebHashHistory(),
   routes, 
   linkActiveClass: "selected", // 设置激活的链接的类名

}) 

export default router