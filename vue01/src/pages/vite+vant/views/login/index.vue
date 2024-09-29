<template>
    <div>
        <van-nav-bar title="登陆" class="page-nav-bar" />
        <van-form @submit="onSubmit">
            <van-cell-group inset>
                <van-field name="username" placeholder="用户名" left-icon="manager" 
                v-model="user.userName" 
                :rules="userFormRules.userName"
                />
                <van-field type="password" name="userPwd" placeholder="密码" left-icon="lock"
                 v-model="user.userPwd" 
                 :rules="userFormRules.userPwd"
                 />
            </van-cell-group>
            <div style="margin: 16px;">
                <van-button  block type="primary" native-type="submit">
                    提交
                </van-button>
            </div>

        </van-form>
    </div>
</template>
<script setup>
import {reactive,toRefs} from 'vue'
import {login} from '../../api/user.js'
import{showSuccessToast, showFailToast} from 'vant'

function useSubmit(user){
    const onSubmit = async ()=>{
      const res = await login(user);
    //   console.log(res.data);
      
      if (res.data.code === 200){
        //   console.log("用户登陆成功-----",res.data);
        showSuccessToast('用户登陆成功');
      }else{
        //   console.log("用户名或密码错误----",res.data);
        showFailToast('用户登陆失败');
      }

    };

    const userFormRules={
        userName:[{required:true,message:"请输入用户名"}],
        userPwd:[{required:true , message:"请输入密码"},{pattern:/^\d{6}$/,message:"密码格式错误"}]
    };

    return {
        onSubmit,
        userFormRules
    }

}


const user = reactive({
    userName:'',
    userPwd:''
})
 
const {onSubmit,userFormRules} = useSubmit(user)
// 定义表单输入框校验


</script>
<style scoped></style>
