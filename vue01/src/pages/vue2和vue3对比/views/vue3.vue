<template>
<div >
    <h4>vue3写法</h4>
    姓名: <input type="text" v-model="name">{{ name }}  <br/>
    年龄: <input type="text" v-model="age"> {{ age }}  <br/>
    <button @click="add">+1</button>

</div>
<div>
    <Child :name="name" />
</div>
</template>

<script   >
import { ref,onMounted,computed,watch } from 'vue'
import Child from './Child.vue'
export default {
  setup() {
    const name = ref('Hello Vue!')
    const age = ref(18)
    const add = () => {
      age.value++;
      name.value = 'Hello Vue3!'+age.value;
    }

    const newName = computed(()=>{
      return '姓名：'+name.value
    })
    
    onMounted(()=>{
      console.log('组件挂载完成');
      name.value = '挂载完成后的姓名'
    })
    watch(age,(newValue,oldValue)=>{
      console.log('年龄变化了',newValue,oldValue);
    })

    return { name, age, add }

  },
  components:{
    Child
  }

}


</script>



<style scoped>
</style> 
