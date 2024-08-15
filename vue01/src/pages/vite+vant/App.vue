<template>
<div >
    <h3>测试axios</h3>
    <button @click="text">发送请求</button>    

    <router-view/>
</div>
</template>


<script   setup>
import axios  from 'axios'

axios.interceptors.request.use((config)=>{
    config.baseURL = 'http://localhost:8000'  
    return config
})

axios.interceptors.response.use(
    res => {
       console.log('响应拦截器成功的回调');
       return res  
    },
    err =>{
       console.log('响应拦截器失败的回调');
    //    return Promise.reject(err)
       return new Promise(()=>{})  //返回一个promise空对象没相当于中断
    }
)

async function text() {
    // console.log("aaa");
//    let res = await axios.get('/user')
   let res = await axios({
     url:'/api/register/',
     method:'POST',
     data:{
        "userName": "s008",
        "userPwd": '123',
        "confirm_password":'123',
     }
   })
   console.log(res);
}


</script>


<style scoped>


</style> 
