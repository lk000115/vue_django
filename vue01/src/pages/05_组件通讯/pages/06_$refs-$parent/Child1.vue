<template>
<div class="child1" >
    <h3>子组件1</h3>
    <h4>书籍:{{ book }}</h4>
</div>
</template>
<script   setup>
import{ref} from 'vue'
let book =ref('look')

defineExpose({book})
</script>
<style scoped>
</style> 
