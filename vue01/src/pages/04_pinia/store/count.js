import {defineStore} from 'pinia'

export const useCountStore = defineStore('count',{
     actions:{
        increment(value){
           if(this.sum < 10){
               this.sum += value
           }
        }    

     },
     state(){
        return{
           sum:6,
           school:'atguigu',
           adress:'高新科技园' 
        }

     }  

})
