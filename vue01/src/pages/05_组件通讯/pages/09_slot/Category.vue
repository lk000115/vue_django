<template>
<div  class="category">
    <h4>{{ title }} </h4>
    <!-- 以下是默认插槽 -->
    <slot></slot>
</div>
</template>

<script   setup>
defineProps(['title'])
</script>

<style scoped>
  .category {
    background-color: skyblue;
    border-radius: 10px;
    box-shadow: 0 0 10px;
    padding: 10px;
    width: 200px;
    height: 300px;
  }
  h4{
    text-align: center;
  }
</style> 
