<template>
    <div>
        <ul>
            <!-- <li>编号:{{route.query.id}}</li> -->
            <!-- <li>标题:{{route.query.title }}</li>
            <li>内容:{{route.query.content}}</li> -->
        </ul>
    </div>

</template>


<script setup name="Detail">
import{useRoute} from 'vue-router'
const route = useRoute()
console.log(route.query)
</script>