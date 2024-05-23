<template>
    <div>
        <h2>当前求和为: {{ countStore.sum }}</h2>
        <select v-model.number="n">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button @click="add">加</button>
        <button @click="minus">修改sum的值</button>
     

    </div>
</template>
<script   setup>
import{ref,reactive} from 'vue'
import {useCountStore} from '../store/count'
import axios from 'axios'
const countStore = useCountStore()

let n = ref(1)

async function add(){
    let {data:{content:title}} = await axios.get('https://api.uomg.com/api/rand.qinghua?format=json')
    console.log(title);
}

function minus(){
//    console.log(n.value);
   countStore.increment(n.value)

}

</script>
<style scoped>
</style> 
