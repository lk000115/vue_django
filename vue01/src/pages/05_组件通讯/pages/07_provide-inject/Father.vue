<template>
<div class="father" >
    <h3>父组件</h3>
    <h4>银子: {{ money }}</h4>
    <h4>车子: {{car.brand }}</h4>

</div>
</template>

<script  setup  lang="js" >
import {ref , reactive,provide} from 'vue'

let money = ref(20)
let car = reactive({
    brand:'奔驰',
    price:100
})

</script>
<style scoped>
</style> 
