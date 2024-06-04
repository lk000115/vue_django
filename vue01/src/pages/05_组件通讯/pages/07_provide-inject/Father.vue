<template>
    <!-- 实现祖孙之间传递数据 -->
<div class="father" >
    <h3>父组件</h3>
    <h4>银子: {{ money }}</h4>
    <h4>车子: {{car.brand }}</h4>
    <Child/>
</div>
</template>

<script  setup  lang="js" >
import {ref , reactive,provide} from 'vue'
import Child from './Child.vue'
let money = ref(20)
let car = reactive({
    brand:'奔驰',
    price:100
})
function updateMoney(value){
   money.value -= value  
}

//向后代提供数据,及修改数据的方法
provide('moneyContext',{money,updateMoney})
provide('car',car)




</script>
<style scoped>
</style> 
