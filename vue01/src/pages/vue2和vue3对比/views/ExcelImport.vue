<template>
  <div class="excel-import">
    <a-upload
      accept=".xlsx, .xls"
      :before-upload="handleBeforeUpload"
    >
      <a-button>
        <!-- <a-icon type="upload" />  -->
        选择文件
      </a-button>
    </a-upload>
    <div v-if="excelData.length > 0">
      <a-table :columns="columns" :data-source="excelData" />
    </div>
  </div>
  <div>
      {{ excelData }}---{{ columns }}
  </div>
</template>

<script setup>
import { ref } from 'vue';
import * as XLSX from 'xlsx';

// 定义响应式数据
const excelData = ref([]);
const columns = ref([]);

// 处理文件上传前的逻辑
const handleBeforeUpload = (file) => {
  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      // 获取 ArrayBuffer 数据
      const arrayBuffer = e.target.result;
      // 将 ArrayBuffer 转换为二进制字符串
      const binaryString = arrayBufferToBinaryString(arrayBuffer);
      const workbook = XLSX.read(binaryString, { type: 'binary' });
      const sheetName = workbook.SheetNames[0];
      const worksheet = workbook.Sheets[sheetName];
      const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
      // 将第一行数据作为表头
      columns.value = json[0].map((title) => ({
        title,
        dataIndex: title,
        key: title,
      }));
      // 从第二行开始作为表格数据
      excelData.value = json.slice(1).map((row, index) => ({
        key: index,
        ...Object.fromEntries(columns.value.map((col, i) => [col.dataIndex, row[i]])),
      }));
    } catch (error) {
      console.error('解析 Excel 文件出错:', error);
    }
  };
  // 使用 readAsArrayBuffer 替代 readAsBinaryString
  reader.readAsArrayBuffer(file);
  return false;
};

// 辅助函数：将 ArrayBuffer 转换为二进制字符串
function arrayBufferToBinaryString(arrayBuffer) {
  const uint8Array = new Uint8Array(arrayBuffer);
  let binaryString = '';
  for (let i = 0; i < uint8Array.length; i++) {
    binaryString += String.fromCharCode(uint8Array[i]);
  }
  return binaryString;
}
</script>

<style scoped>
.excel-import {
  margin: 20px;
}
</style>
