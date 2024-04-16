<script setup>
import { RouterView,RouterLink } from 'vue-router';
import{reactive} from'vue'

const items = reactive([
   {path:"/home",title:"首页导航"},
   {path:"/news",title:"新闻导航"},
   {path:"/about",title:"关于导航"},
   
])

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
              功能列表</h5>
            <el-menu default-active="1" class="el-menu-vertical-demo"  :router="true" >
              <el-menu-item v-for="(item,i) in items" :key="i" :index="item.path" >
                <el-icon><Search /></el-icon>
                <span>{{ item.title }}</span>
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
