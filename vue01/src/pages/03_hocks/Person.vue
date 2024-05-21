<template>
<div class="person">
    <h2>当前求和项为: {{ sum }} ,放大10倍后为{{ bigSum }}</h2>
    <button @click="add" >点我sum加1</button>
    <hr>
    <img v-for="(dog,index) in dogList" :src="dog" :key="index">
    <br>
    <button @click="getDog">再来一个</button> 
</div>
</template>
<script   setup>
import useSum from './useSum'
import useDog from './useDog'
const {sum,add,bigSum} = useSum()
const{dogList,getDog} = useDog()

</script>

<style scoped>
.person{
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    padding: 20px;
}
img{
    height: 100px;
    margin-right: 10px;
}
</style> 
