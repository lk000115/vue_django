<template>
<div >
    <h4>vue3写法</h4>
    姓名: <input type="text" v-model="name">{{ name }}  <br/>
    年龄: <input type="text" v-model="age"> {{ age }}  <br/>
    <button @click="add">+1</button>

</div>
</template>

<script   >
import { ref } from 'vue'
export default {
  setup() {
    const name = ref('Hello Vue!')
    const age = ref(18)
    const add = () => {
      age.value++;
      name.value = 'Hello Vue3!'+age.value;
    }
    return { name, age, add }
  }

}


</script>



<style scoped>
</style> 
