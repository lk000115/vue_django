<template>
<div class="child1">
    <h3>子组件1</h3>
    <h4>玩具: {{ toy }}</h4>
    <button @click="emitter.emit('send-toy',toy)">子组件1按钮</button>
</div>
</template>
<script   setup>
import {ref} from 'vue'
import emitter from '../utils/emitter.js'
let toy = ref('子组件1的数据')
</script>


<style scoped>
</style> 
