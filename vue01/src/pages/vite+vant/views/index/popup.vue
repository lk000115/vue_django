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
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
                <li>分类</li>
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



</script>

<style    scoped>
</style> 

