<template>
<div >
    <h4>vue2写法</h4>
    姓名: <input type="text" v-model="name">{{ name }}  <br>
    年龄: <input type="text" v-model="age"> {{ age }}  <br>
    <button @click="add">+1</button>

</div>
</template>



<script   >
 export default {
    data() {
        return {
            name: 'Hello Vue!',
            age:18
        }
    },
    methods: {
       add() {
         this.age++
       }        
    }
    

}


</script>



<style scoped>
</style> 
