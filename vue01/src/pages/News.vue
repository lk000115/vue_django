<template>
    <div class="common-layout">
        <el-container>
            <el-aside width="200px">
                <ul>
                    <li v-for="item in newsList" :key="item.id">
                        <button @click="showNewsDetail">查看详情</button>
                        <!-- 第一种写法 -->
                        <!-- <RouterLink :to="`/news/detail?id=${item.id}&title=${item.title}&content=${item.content}` "  style="text-decoration:none; ">{{ item.title }}</RouterLink> -->
                        <!-- 第二种写法 -->
                        <RouterLink  
                           style="text-decoration:none;"
                           :to="{
                              name:'xq',
                              query:{
                                id:item.id,
                                title:item.title,
                                content:item.content
                              }
                           }"  
                        >

                        {{ item.title }}
                        </RouterLink>

                    </li>
                </ul>
            </el-aside>
            <el-main>
                <RouterView></RouterView>
            </el-main>
        </el-container>
    </div>

</template>



<script setup name="News">
import { RouterView, RouterLink } from 'vue-router'
import { reactive } from 'vue'

const newsList = reactive([
    { id: '001', title: '一种食物', content: '除了iPhone15之外，去年下半年发布的这些国产手机' },
    { id: '002', title: '一种水果', content: '华为Mate60系列的强项是拍照，' },
    { id: '003', title: '一种蔬菜', content: '国产新发布的手机激活榜，我们可以从中看出端倪来' }
])

function showNewsDetail(){
    
}

</script>

<style scope>
ul li {
   list-style-type: none;
   margin-bottom:5px;
}
</style>