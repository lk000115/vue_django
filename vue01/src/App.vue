<script setup>
import Person from './components/Person.vue';
</script>

<template>

  <div class="common-layout">

    <el-container>
      <el-header>
        <el-row class="row-bg" justify="end">
          <el-col :span="6">
            <el-button type="primary">首页</el-button>
          </el-col>
          <el-col :span="6">
            <el-button type="primary">新闻</el-button>
          </el-col>
          <el-col :span="6">
            <el-button type="primary">列表</el-button>
          </el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <!--  -->
          <el-col >
            <h5 class="mb-2">Default colors</h5>
            <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
              <el-menu-item index="1">
                <el-icon><icon-menu /></el-icon>
                <span>Navigator 1</span>
              </el-menu-item>
              <el-menu-item index="2" >
                <el-icon>
                  <document />
                </el-icon>
                <span>Navigator 2</span>
              </el-menu-item>
              <el-menu-item index="3">
                <el-icon>
                  <setting />
                </el-icon>
                <span>Navigator 3</span>
              </el-menu-item>
            </el-menu>
          </el-col>


          <!--  -->
        </el-aside>
        <el-main>
          Main
        </el-main>
      </el-container>
    </el-container>
  </div>



</template>

<style scoped>
.el-col {}

.el-header {
  padding: 15px 20px;
  /* background-color:#019fa0; */
}

.el-aside {

  /* background-color: #ff5675; */
}

.el-main {
  background-color: #ff8345;
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
