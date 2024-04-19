<template>
    <div class="common-layout">
        <el-container>
            <el-aside width="100px">

                <el-menu class="el-menu-vertical-demo" router>

                    <el-menu-item v-for="(list, i) in newsList" :key="i" index="xq"
                       :route="{params:{id:list.id,content:list.content},name:'xq'}"
                       >
                        <span>{{ list.title }}</span>
                    </el-menu-item>

                </el-menu>

                <!-- <ul>
                    <li v-for="list in newsList" :key="list.id"  >
                        <RouterLink :to="{
                             name:'xq',
                             params:{
                                id:list.id,
                                content:list.content
                             } 
                        }">
                        {{ list.title }}                           
                    </RouterLink>

                    </li>
                </ul> -->



            </el-aside>

            <el-main>
                <RouterView></RouterView>
            </el-main>
        </el-container>
    </div>
</template>


<script setup>
import { reactive } from 'vue'
import { RouterLink, RouterView } from 'vue-router';
const newsList = reactive([
    { id: '001', title: '一种食物', content: '除了iPhone15之外，去年下半年发布的这些国产手机' ,path:'/news/detail'},
    { id: '002', title: '一种水果', content: '华为Mate60系列的强项是拍照，',path:'/news/detail' },
    { id: '003', title: '一种蔬菜', content: '国产新发布的手机激活榜，我们可以从中看出端倪来' ,path:'/news/detail'}
])
</script>


<style scoped></style>
