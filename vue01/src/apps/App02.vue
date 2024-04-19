<template>

    <div class="common-layout">
        <Header a="sdsds"  />
        <el-container>
            <el-aside width="150px">

                <el-menu  class="el-menu-vertical-demo" :router="true">

                    <el-menu-item  v-for="(list,i) in navlist"  :key="i" :index="list.path">
                        <el-icon><setting /></el-icon>
                        <span>{{ list.title }}</span>
                    </el-menu-item>

                </el-menu>


            </el-aside>

            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>



</template>

<script setup>
import Header from '@/components/Header.vue'
import { RouterView, RouterLink } from 'vue-router'

import { reactive } from 'vue'

const navlist = reactive([
    { path: "/home", title: "首页导航" },
    { path: "/news", title: "新闻导航" },

])


</script>




<style scoped></style>
