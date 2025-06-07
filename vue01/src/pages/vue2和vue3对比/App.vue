<template>
<div class="panel">
    <h3>vue2和vue3写法的对比</h3>
</div>
<p>
    <router-link to="/vue2" >vue2</router-link>
    <router-link :to="{path:'/vue3'}">vue3</router-link>
    <router-link :to="{name:'vue2'}">vue2</router-link>
</p>
<div  class="content">
    
</div>
<router-view></router-view>   
</template>



<script setup>

</script>


<style scoped>
.panel{
    width: 800px;
    height: 300px;
    margin: 0 auto;
    margin-top:130px;
    font-size: 40px;
    background-color: #fff;

}
.content{
    widows: 10%;
    height: 400px;
    background-color: greenyellow;
    border: 1cap; 
}
</style> 
