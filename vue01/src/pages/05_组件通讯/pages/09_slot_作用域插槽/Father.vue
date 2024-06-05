<template>
<div class="father">
    <h3>父组件-作用域插槽</h3>
    <div class="content">
      <Game>
          <template v-slot="params">
              <ul>
                <li v-for="g in params.game" :key="g.id">
                     {{ g.name }}
                </li>
              </ul>  
          </template>
      </Game>
      <Game>
         <template #default="{game}" >
            <h4 v-for="item in game" :key="item.id">{{ item.name }} </h4> 
         </template>  
      </Game>
    </div>
</div>
</template>

<script   setup lang="js">
import Game from './Game.vue'
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
