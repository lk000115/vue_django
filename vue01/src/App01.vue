<template>
<<<<<<< HEAD

  <div class="common-layout">
    <el-container>
      <el-header>
        <el-row class="banner-box">
          <el-col :span="2">
            <div class="grid-content ep-bg-light">sdsdd </div>
          </el-col>
          <el-col :span="20">
            <div class="grid-content ep-bg-light">
              后台管理系统 </div>
          </el-col>
          <el-col :span="2">
            <div class="grid-content ep-bg-light">ababab </div>
          </el-col>
        </el-row>


      </el-header>
      <el-main>Main</el-main>
    </el-container>
  </div>


=======
    <div>
        <h2><el-icon><Search /></el-icon>测试组件</h2>   
        <RouterView></RouterView>

    </div> 
>>>>>>> 7dff83a72271635563548a80d19708d46db3e847
 



</template>




<script  setup>
import { RouterView,RouterLink } from 'vue-router';


</script>





<style scoped>
.banner-box{
   display: flex;
   align-items: center; 
  

}


.grid-content {
  border-radius: 4px;
  min-height: 20px;
}

.ep-bg-light {
  background-color: aqua;
}



</style>


<<<<<<< HEAD
<script setup>



</script>
=======

>>>>>>> 7dff83a72271635563548a80d19708d46db3e847
