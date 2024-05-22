<template>
    <div>
        <h2>当前求和为: {{ countStore.sum }}</h2>
        <select v-model.number="n">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="add">加</button>
        <button @clicl="minus">减</button>
     

    </div>
</template>
<script   setup>
import{ref,reactive} from 'vue'
import {useCountStore} from '../store/count'
const countStore = useCountStore()

let n = ref(1)

function add(){
    console.log(countStore);
}

function minus(){


}

</script>
<style scoped>
</style> 
