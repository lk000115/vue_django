<template>
<div class="grandchild">
    <h3>孙组件</h3>
    <h4>{{ money }}---{{ car.brand }}</h4> 
    <button @click="updateMoney(2)">修改上级组件的数据</button>
</div>
</template>

<script   setup lang="js">
import{inject} from 'vue'
let {money,updateMoney} = inject('moneyContext')
let car = inject('car')
</script>

<style scoped>
.grandchild {
    margin-top: 20px;
    background-color: rgb(194, 211, 115);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px black;

}
</style> 
