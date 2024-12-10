# gym-manager

## frontend

### Vue + vite + bootstrap

见
[Bootstrap & Vite](https://v5.bootcss.com/docs/getting-started/vite/)


可以不使用vue，只用vite

vite + bootstrap

#### 安装vite等

```cmd
mkdir frontend && frontend
npm init -y

npm i --save-dev vite
npm i --save bootstrap @popperjs/core
npm i --save-dev sass
```

#### 补充相关文件

自己建文件夹`\src`与`vite.config.js`

```cmd
frontend/
├── src/
├── package-lock.json
├── package.json
└── vite.config.js
```

对于`vite.config.js`

```js
// vite.config.js
const path = require('path')

export default {
  root: path.resolve(__dirname, 'src'),
  resolve: {
    alias: {
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
    }
  },
  server: {
    port: 8080,
    hot: true
  }
}
```

#### 添加启动方式

对于`package.json`

在`"scripts"`中添加`"start": "vite"`

```json
{
  // ...
  "scripts": {
    "start": "vite",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  // ...
}
```

#### 导入模板

将你下载的模板压缩包的src文件夹中的内容复制到frontend的src文件夹中

#### 启动

```cmd
npm start
```
