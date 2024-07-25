<template>
    <div>
        <van-nav-bar title="登陆" />
        <van-form>
            <van-cell-group inset>
                <van-field name="username" placeholder="用户名" />
                <van-field type="password" name="userpwd" placeholder="密码" />
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

</script>
<style scoped></style>
