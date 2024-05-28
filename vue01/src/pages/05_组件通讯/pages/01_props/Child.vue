<template>
<div class="child">
    <h3>子组件</h3>
    <h4>父给的东西: {{ car }}----{{ x }}</h4>
    <button @click="sendToy(toy)">把玩具给父亲</button>
    <button @click="fn">调用父组件的函数</button>
</div>
</template>
<script   setup>
import{ref } from 'vue'
let toy = ref('奥特曼')

defineProps(['car','sendToy','x','fn'])

</script>
<style scoped>
</style> 
