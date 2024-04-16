<template>
    <div>
        <h2><el-icon><Search /></el-icon>测试组件</h2>   
        <RouterView></RouterView>

    </div> 
 



</template>




<script  setup>
import { RouterView,RouterLink } from 'vue-router';


</script>





<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 20px;
}







.demo-border .text {
  width: 15%;
  border: 1px solid;
  border-radius: 4px;

}




</style>



