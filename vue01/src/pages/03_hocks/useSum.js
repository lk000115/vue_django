import {ref,onMounted,computed}  from 'vue'

export default function(){
    
    let sum = ref(0) 
    let bigSum = computed(()=>{
        return sum.value *10

    })      
    function add (){
        sum.value += 1
    }  
   
   
     return {sum,add,bigSum}
}