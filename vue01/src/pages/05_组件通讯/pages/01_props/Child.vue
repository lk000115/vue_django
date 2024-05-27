<template>
<div class="child">
    <h3>子组件</h3>
    <h4>父给的车: {{ car }}</h4>
    <button @click="sendToy(toy)">把玩具给父亲</button>
</div>
</template>
<script   setup>
import{ref } from 'vue'
let toy = ref('奥特曼')

defineProps(['car','sendToy'])

</script>
<style scoped>
</style> 
