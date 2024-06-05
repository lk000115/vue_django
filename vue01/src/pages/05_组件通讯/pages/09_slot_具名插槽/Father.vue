<template>
<div class="father">
    <h3>父组件-具名插槽</h3>
    <div class="content">
      <Category >
         <template v-slot:s1>
             sssss  
         </template> 
         <template #s2>
             dddd  
         </template> 
      </Category>
      <!-- <Category #s2>dd</Category> -->
    </div>
    


</div>
</template>

<script   setup lang="js">
import Category from './Category.vue'
</script>
<style scoped>
  .father {
    background-color: rgb(165, 164, 164);
    padding: 20px;
    border-radius: 10px;
  }
  .content {
    display: flex;
    justify-content: space-evenly;
  }
</style> 
