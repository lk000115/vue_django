<template>
<div class="father" >
    <h3>父组件</h3>
    <h4>{{ username }}</h4>
    <h4>{{ password }}</h4>
    <input :value = "username"  @input="username = $event.target.value"  />

    <!-- <AtguiguInput  :modelValue="username" 
     @update:modelValue = "username = $event"
    /> -->
    <!-- 以上写法简写如下 -->
    <AtguiguInput v-model="username" />

</div>
</template>
<script   setup>
import AtguiguInput from './AtguiguInput.vue'
import{ref} from 'vue'
let username = ref('zhansan')
let password = ref('123456')


</script>




<style scoped>
</style> 
