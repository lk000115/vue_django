<template>
    <div>
        <ul>
            <li>编号:{{query.id}}</li>
            <li>标题:{{query.title }}</li>
            <li>内容:{{query.content}}</li>
        </ul>
    </div>

</template>


<script setup name="Detail">
import{toRefs} from 'vue'
import{useRoute} from 'vue-router'
const route = useRoute()
// route是响应式对象,如果不用toRefs包裹将丢失响应式特性
let {query} = toRefs(route)    
console.log(route.query)
</script>