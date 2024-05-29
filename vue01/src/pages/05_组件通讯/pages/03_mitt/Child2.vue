<template>
<div class="child2">
    <h3>子组件2</h3>
    <h4>电脑: {{computer  }}</h4>
    <h4>子组件1给的: {{ toy }}</h4>
</div>
</template>
<script   setup>
import {ref,onUnmounted} from 'vue'
import emitter from '../utils/emitter'

let computer = ref('dell')
let toy = ref('')

emitter.on('send-toy',(value)=>{
    toy.value = value 
})

onUnmounted(()=>{
    emitter.off('send-toy')
})

</script>
<style scoped>
</style> 
