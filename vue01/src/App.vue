<script setup>
import{RouterView, routerLink} from 'vue-router'

const handleOpen = (key,keyPath) => {
  console.log(key, keyPath)
   
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<template>

  <div class="common-layout">

    <el-container>
      <el-header>
        <el-row class="row-bg" justify="end">
          <el-col :span="6">
              <router-link to="/home" active-class="ac" class="rt">首页</router-link>  
          </el-col>
          <el-col :span="6">
              <router-link :to="{name:'xinwen'}"  active-class="ac" class="rt">新闻</router-link>
          </el-col>
          <el-col :span="6">
              <router-link :to="{path: '/about'}"  active-class="ac" class="rt">关于</router-link>
          </el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <!--  -->
          <el-col >
            <h5 class="mb-2" >
              <el-icon><Menu /></el-icon>
              功能列表</h5>
            <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
              <el-menu-item index="1">
                <el-icon><Search /></el-icon>
                <span>Navigator 0</span>
              </el-menu-item>
              <el-menu-item index="4" >
                <el-icon><Search /></el-icon>
                <span>Navigator 2</span>
              </el-menu-item>
              <el-menu-item index="3">
                <el-icon> <setting /></el-icon>
                <span>Navigator 3</span>
              </el-menu-item>
            </el-menu>
          </el-col>


          <!--  -->
        </el-aside>
        <el-main>
             <RouterView></RouterView>
        </el-main>
      </el-container>
    </el-container>
  </div>



</template>

<style scoped>
.el-col .ac {
    color: red;
    

}
.el-col .rt{
  text-decoration:none;
}

.el-header {
  padding: 15px 20px;
  /* background-color:#019fa0; */
}

.el-aside {

  /* background-color: #ff5675; */
}

.el-main {
  border-radius: 5px;
  border-color: #E6E6FA;
  border-style:groove;
  /* background-color: #ff8345; */
}

.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}


</style>
