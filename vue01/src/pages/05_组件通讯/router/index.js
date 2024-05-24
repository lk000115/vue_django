import { createRouter, createWebHistory } from 'vue-router'
import Props from '../pages/01_props/Father.vue'


export default createRouter({
    history: createWebHistory(),
    routes:[
        {
			path: '/props',
			component: Props
		},
		{
			path: '/event',
			component: Event
		},  
   
    ]



})
