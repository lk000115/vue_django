<template>
<div >
    <h3>测试axios</h3>
    <button @click="text">按钮</button>    

    <router-view/>
</div>
</template>


<script   setup>
import axios  from 'axios'
async function text() {
    // console.log("aaa");
   let res = await axios.get("http://localhost:3000/user")
   console.log(res );
}


</script>


<style scoped>


</style> 
