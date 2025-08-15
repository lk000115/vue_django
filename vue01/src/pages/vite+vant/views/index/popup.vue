<template>
<div class="popup">
    <van-cell title="热门分类" is-link @click="showPopup" />
    <!-- 右侧弹出 -->
    <van-popup
        v-model:show="showRight"
        position="right"
        closeable
        close-icon-position="top-right"
        :style="{ width: '70%', height: '100%' }">
      
       <div  class="popupList">
            <h4>分类标题</h4>
            <ul>
                <li v-for="(item, index) in popuplist" :key="index" :class='n==index ? "active" : "" '  @click="n=index" >{{ item }}</li>
            </ul>
       </div>


    </van-popup> 

</div>
</template>


<script   setup>
import { ref } from 'vue';
const showRight = ref(false);
const showPopup = () => {
    showRight.value = true;
};

const popuplist = ref(['首页','都市','历史','悬疑','游戏','分类'])
const n = ref(0)


</script>

<style    scoped>
</style> 

