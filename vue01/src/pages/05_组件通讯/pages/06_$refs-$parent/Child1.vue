<template>
<div class="child1" >
    <h3>子组件1</h3>
    <h4>书籍:{{ book }}</h4>
    <button @click="minhouse($parent)">操作父组件的数据</button>
</div>
</template>
<script   setup>
import{ref} from 'vue'
let book =ref('book----')
let book2 = ref('book2')
// 向外部提供数据
defineExpose({book,book2})
function minhouse(parent){
     parent.house = '房屋变小';
}

</script>
<style scoped>
	.child1{
		margin-top: 20px;
		background-color: skyblue;
		padding: 20px;
		border-radius: 10px;
    box-shadow: 0 0 10px black;
	}
</style> 
