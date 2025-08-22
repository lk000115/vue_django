<template>
<div class="chartstab" >
   <van-tabs v-model:active="active">
        <van-tab title="标签 1">内容 1</van-tab>
        <van-tab title="标签 2">内容 2</van-tab>
        <van-tab title="标签 3">内容 3</van-tab>
        <van-tab title="标签 4">内容 4</van-tab>
  </van-tabs>


</div>
</template>


<script   setup>
import { ref } from 'vue';
const active = ref(0);


</script>

<style    scoped>


</style> 

