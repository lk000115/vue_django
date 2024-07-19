<!-- 底部导航页面 -->
<template>
<div class="footer" >
    <div class="footer-seat">
        <div class="footer-list">
            <ul>
                <li v-for="(v,i) in footerlist" :key="i">
                    <router-link :to="v.path" >
                        <i class="iconfont" :class="v.icon" ></i>
                        <p>{{ v.title }}</p>
                    </router-link>
                </li>
            </ul> 
        </div>

    </div>
    
</div>
</template>
<script   setup>
import{ref} from 'vue'
let footerlist = ref([
  {title:'详情',icon:'icon-detail',path:'/detail'},
  {title:'列表',icon:'icon-appstore',path:'/list'},
  {title:'首页',icon:'icon-home1',path:'/index'}
])

</script>
<style scoped>
</style> 
