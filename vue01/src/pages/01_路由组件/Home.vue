<template>
    <div>
        首页---编程式路由跳转     
    </div>
</template>



<script setup>
import{onMounted} from 'vue'
import{useRouter}  from 'vue-router'

const router = useRouter()

onMounted(()=>{
   setTimeout(() => {
      router.push('/news')
   }, 2000);   

})


</script>