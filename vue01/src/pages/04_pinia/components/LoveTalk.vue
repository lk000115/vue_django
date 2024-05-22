<template>
    <div class="talk">
     <button @click="getLoveTalk">获取信息</button>
     <ul>
        <li v-for="talk in talkStore.talkList"  :key="talk.id">
              {{ talk.title }}
        </li>
     </ul> 
    </div>
</template>
<script   setup>
import{useTalkStore} from '../store/loveTalk'

const talkStore = useTalkStore()

function getLoveTalk(){

    console.log('获取信息');
}
</script>
<style scoped>
</style> 
