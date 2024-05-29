<template>
<div class="father">
    <h3>父组件</h3>
    <h4 v-show="toy">子给的玩具:{{ toy }}</h4>
    <Child @send-toy="saveToy"  />   
</div>
</template>
<script   setup>
import Child from './Child.vue'
import{ref} from 'vue'
let toy = ref('')

function saveToy(value){

    toy.value = value

}

</script>
<style scoped>
</style> 
