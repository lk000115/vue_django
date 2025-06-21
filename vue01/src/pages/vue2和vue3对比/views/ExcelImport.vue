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
    const workbook = XLSX.read(e.target.result, { type: 'binary' });
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];
    const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
    columns.value = json[0];
    excelData.value = json.slice(1);
  };
  reader.readAsBinaryString(file);
  return false;
};
</script>

<style scoped>
.excel-import {
  margin: 20px;
}
</style>
