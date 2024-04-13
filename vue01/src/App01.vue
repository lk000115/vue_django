<template>
    <div>
        <h2><el-icon><Search /></el-icon>测试组件</h2>     

    </div> 
    <table  class="demo-border">
         <tbody>
            <tr>
                <td class="text">aaaaaaaaaaa</td>
                <td class="line">bb</td>
            </tr>
         </tbody>

    </table>

    <el-row>
    <el-col :span="24"><div class="grid-content ep-bg-purple-dark" />sdsdd</el-col>
    </el-row>



</template>



<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 20px;
}







.demo-border .text {
  width: 15%;
  border: 1px solid;
  border-radius: 4px;

}




</style>


<script  setup>



</script>

