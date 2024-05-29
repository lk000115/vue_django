<template>
<div class="child">
    <h3>子组件</h3>
    <h4>玩具:{{ toy }}</h4>
    <button @click="emit('send-toy',toy)">测试传参</button>
</div>
</template>
<script   setup>
import{ref} from 'vue'
let toy = ref("子组件数据")
const emit = defineEmits(['send-toy'])
</script>
<style scoped>
</style> 
