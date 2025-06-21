<template>
    
  <div class="common-layout">
    <h3> vue2和vue3写法的对比</h3>
    <el-container>
      <el-header>   
          <el-row>
            <el-col :span="4">
                 <router-link to="/vue2" >vue2</router-link>
            </el-col>
            <el-col :span="4">
                <router-link :to="{path:'/vue3'}">vue3</router-link>
            </el-col>
            <el-col :span="4">
             <router-link :to="{name:'child'}">child</router-link>
            </el-col>
            <el-col :span="12">
              <router-link :to="{name:'excelImport'}">excel导入</router-link> 
            </el-col>
          </el-row>
      </el-header>
      <el-main>
              <div>

                  <router-view></router-view> 
              </div>        

               <!-- <div class="mb-4">

                   <el-button type="primary" size="large">primary</el-button>
               </div> -->

      </el-main>
    </el-container>
  </div>

</template>



<script setup>

</script>


<style scoped>

</style> 
