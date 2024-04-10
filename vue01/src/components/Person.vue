<script setup  name="Person">
import{ref,computed} from 'vue'
let firstName = ref('张')
let lastName = ref('三')

let fullName = computed({
    // 读取
    get(){
      return firstName.value + '-' + lastName.value
    },
    // 修改
    set(val){
      console.log('有人修改了fullName',val)
      firstName.value = val.split('-')[0]
      lastName.value = val.split('-')[1]
    }
  })
  function changeFullName(){
    fullName.value = 'li-si'
  } 


</script>

<template>

   姓：<input type="text" v-model="firstName">   <br>
   名：<input type="text" v-model="lastName">   <br>
 全名：   <span>{{ fullName }}</span>       <br>

 <button @click="changeFullName">全名改为：li-si</button>
</template>

<style scoped>

</style>
