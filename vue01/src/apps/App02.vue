<template>

    <div class="common-layout">
        <Header />
        <el-container>
            <el-aside width="200px">
                Aside
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


</script>


<style scoped></style>
