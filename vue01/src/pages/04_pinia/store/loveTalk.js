import {defineStore} from 'pinia'
import axios from 'axios'
import {nanoid} from 'nanoid'

export const useTalkStore = defineStore('talk',{
     
    actions:{
       async getTalk(){
         // 发请求，下面这行的写法是：连续解构赋值+重命名
      let {data:{content:title}} = await axios.get('https://api.uomg.com/api/rand.qinghua?format=json')
      // 把请求回来的字符串，包装成一个对象
      let obj = {id:nanoid(),title}
      // 放到数组中
      this.talkList.unshift(obj)     //在数组开头添加数据
    //   this.talkList.push(obj)     //在数组末尾添加数据 

       } 
    } ,

     state(){
         return{
            talkList:[
                {id:'ftrfasdf01',title:'今天你有点怪，哪里怪？怪好看的！'},
                {id:'ftrfasdf02',title:'草莓、蓝莓、蔓越莓，今天想我了没？'},
                {id:'ftrfasdf03',title:'心里给你留了一块地，我的死心塌地'}
            ]

         }
         
     }

})