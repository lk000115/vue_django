<template>
    <div class="father" >
        <h3>父组件</h3>
        <h4 v-show="toy">子给的玩具:{{ toy }}</h4>
        <Child :car="car" :sendToy="getToy" />
    </div>
</template>
<script   setup>
import Child from './Child'
import {ref}  from 'vue'
let car = ref('奔驰')
let toy = ref('')
function getToy(value){
   toy.value = value

}


</script>
<style scoped>
</style> 
