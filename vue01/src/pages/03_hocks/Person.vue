<template>
<div class="person">
    <h2>当前求和项为: {{ sum }} ,放大10倍后为{{ bigSum }}</h2>
    <button @click="add" >点我sum加1</button>
     
</div>
</template>
<script   setup>
import useSum from './useSum'
const {sum,add,bigSum} = useSum()
</script>

<style scoped>

</style> 
