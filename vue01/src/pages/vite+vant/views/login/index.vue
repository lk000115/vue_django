<template>
    <div>
        <van-nav-bar title="登陆" class="page-nav-bar" />
        <van-form @submit="onSubmit">
            <van-cell-group inset>
                <van-field name="username" placeholder="用户名" left-icon="manager" :v-model="user.username" />
                <van-field type="password" name="userPwd" placeholder="密码" left-icon="lock" :v-model="user.userPwd" />
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
const user = reactive({
    username:'',
    userPwd:''
})
 
</script>
<style scoped></style>
