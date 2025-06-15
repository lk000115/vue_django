<template>
  <div>
    <ul>
      <li>内容1</li>
      <li>内容2</li>
    </ul>
    
   <button @click="change">修改</button>   

  </div>

  <div>
    <h4>姓名：{{props.name}}-----</h4>
  </div>
  



</template>






<script  setup>
import { ref,defineProps } from 'vue'

const props = defineProps({
  name: {
    type: [String,Number] , //可以设定接受多种数据类型
    default: '默认姓名'
  }
})

// const props = defineProps(['name'])

const change = ()=>{
  console.log(props);
  // props.name = props.name + "aa"  //父组件传过来的name是只读属性
  
}





</script>

<style scoped>


</style>
