<template>
<div class="father">
    <h3>父组件</h3>
    <Child1 ref="c1" />
</div>
</template>
<script   setup>
import Child1 from './Child1.vue'
import{ref} from 'vue'
let c1 = ref("chesi")
</script>
<style scoped>
</style> 
