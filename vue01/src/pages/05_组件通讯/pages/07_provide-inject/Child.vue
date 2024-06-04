<template>
<div class="child">
    child
    <GrandChild/>
</div>
</template>
<script   setup lang="js">
import GrandChild from './GrandChild.vue'
</script>

<style scoped>
.child {
    margin-top: 20px;
    background-color: skyblue;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px black;
  }
</style> 
