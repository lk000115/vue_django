<template>
    <div>
        <ul>
            <li>编号:{{id}}</li>
            <li>内容:{{content}}</li>
        </ul>
    </div>
</template>
<script   setup>
import { defineProps } from 'vue';
// import{toRefs} from 'vue'
// import{useRoute} from 'vue-router'
// const route = useRoute()
// console.log(route.query)
// // route是响应式对象,如果不用toRefs包裹将丢失响应式特性
// let {query} = toRefs(route)
defineProps(['id','content'])


</script>




<style scoped>
</style> 
