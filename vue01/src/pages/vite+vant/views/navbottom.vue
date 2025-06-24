<template>
   <div class="footer">
        <div class="footer-seat">
            <div class="footer-list">
                <ul>
                    <li v-for="(item, index) in footerList" :key="index">
                        <router-link :to="item.path" >
                            <i class="iconfont" :class="item.icon"></i>
                            <p>{{ item.title }}</p>
                        </router-link>
                    </li>
 
                </ul>
            </div>
        </div>
      
   </div>


</template>



<script  setup>
import {ref}  from 'vue'

let footerList = ref([
    { icon: 'icon-home', title: '书城',path: '/index' },
    { icon: 'icon-position-line', title: '社区',path: '/community' },
    { icon: 'icon-car', title: '福利' ,path: '/welfare' },
    { icon: 'icon-user', title: '我的',path: '/my' }
  ])



</script>


<style scoped>


</style>
