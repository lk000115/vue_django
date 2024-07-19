import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { VantResolver } from '@vant/auto-import-resolver';


// https://vitejs.dev/config/
export default defineConfig({
  server:{
    open:true,
    port:8081
  },
  plugins: [
    vue(),
    AutoImport({
      resolvers: [VantResolver()],
    }),
    Components({
      resolvers: [VantResolver()],
    }),
  
  ],
  resolve:{
    alias:{
      '@': path.resolve(__dirname,'./src'),
    }
  }


})
