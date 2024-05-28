<template>
    <div class="father" >
        <h3>父组件</h3>
        <h4 v-show="toy">子给的玩具:{{ toy }}</h4>
        <Child :car="car" :sendToy="getToy"  :x="a" :fn="fun" />
    </div>
</template>
<script   setup>
import Child from './Child.vue'
import {ref}  from 'vue'
let a = ref('来自父组件的aa')
let car = ref('奔驰')
let toy = ref('')
function getToy(value){
   toy.value = value

}
function fun(){
    console.log("调用父组件的函数");
}


</script>
<style scoped>
</style> 
