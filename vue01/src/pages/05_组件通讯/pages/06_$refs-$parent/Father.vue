<template>
<div class="father">
    <h3>父组件</h3>
    <h4>{{ house }}</h4>
    <button @click="changeBook">修改子组件的数据值</button>
    <Child1 ref="c1" />

</div>
</template>
<script   setup>
import Child1 from './Child1.vue'
import{ref} from 'vue'
let c1 = ref("")
let house = ref('房屋')
function changeBook(){
    c1.value.book = '修改后的值'

}
defineExpose({house})


</script>
<style scoped>


</style> 
