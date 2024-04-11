<template>
    <div class="news">
        <ul>
            <li v-for="item in newsList" :key="item.id" >
               <a href="#"> {{ item.title }}</a> 
            </li>
        </ul>  
    </div>
</template>



<script setup name="News">
import{reactive} from 'vue'

const newsList = reactive([
    {id:'001',title:'一种食物',content:'除了iPhone15之外，去年下半年发布的这些国产手机'},
    {id:'002',title:'一种水果',content:'华为Mate60系列的强项是拍照，'},
    {id:'003',title:'一种蔬菜',content:'国产新发布的手机激活榜，我们可以从中看出端倪来'}
])

</script>

<style  scope>



</style>