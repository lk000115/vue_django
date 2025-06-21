import { createRouter,createWebHashHistory } from "vue-router";

// 1. 配置路由规则
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
    },
    {
        path: "/child",
        name:"child",
        component: ()=>import("../views/Child.vue")  
    },
    {
        path: "/excelImport",
        name:"excelImport",
        component: ()=>import("../views/ExcelImport.vue")
    }

]

// 2. 创建路由实例

const router = createRouter({

   history: createWebHashHistory(),
   routes, 
})


// 3.导出路由实例
export default router