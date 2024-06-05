<template>
<div class="father" >
    <h3>父组件</h3>
    <div class="content">
      <Category title="标题1">
          <ul>
            <li v-for="g in games" :key="g.id">{{ g.name }}</li>
          </ul>
      </Category>
      <Category title="标题2"></Category>
    </div>
    
</div>
</template>

<script   setup  lang="js">
import Category from './Category.vue'
import{ref,reactive} from 'vue'
let title = ref('')
let games = reactive([
{id:'asgytdfats01',name:'英雄联盟'},
    {id:'asgytdfats02',name:'王者农药'},
    {id:'asgytdfats03',name:'红色警戒'},
    {id:'asgytdfats04',name:'斗罗大陆'}
])
</script>


<style scoped>
  .father {
    background-color: rgb(165, 164, 164);
    padding: 20px;
    border-radius: 10px;
  }
  .content{
    display: flex;
    justify-content: space-evenly;
  }
</style> 
