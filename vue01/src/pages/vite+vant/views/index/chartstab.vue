<template>
<div class="chartstab" >
   <van-tabs v-model:active="active">
        <van-tab title="标签 1">内容 1</van-tab>
        <van-tab title="标签 2">内容 2</van-tab>
        <van-tab title="标签 3">内容 3</van-tab>
        <van-tab title="标签 4">内容 4</van-tab>
  </van-tabs>
  <div class="box">
     <div class="box-item">111</div>
     <div class="box-item">222</div>
     <div class="box-item">333</div>
     <div class="box-item">444</div>
     <div class="box-item">555</div>
     <div class="box-item">666</div>
     <div class="box-item">777</div>
     <div class="box-item">888</div>
  </div>

</div>
</template>


<script   setup>
import { ref } from 'vue';
const active = ref(0);


</script>

<style    scoped>
.box{
   overflow-x: auto;
   white-space: nowrap;
}
.box-item{
  background-color: red;
  padding:5px 20px;
  display: inline-block;
  margin:5px

}
.box::-webkit-scrollbar {
    display: none; /* 隐藏滚动条 */
}

</style> 

