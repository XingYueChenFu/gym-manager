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



## Vue3

```cmd
C:\Users\XYCF\Documents\Code\gym-manager>npm create vue@latest

> npx
> create-vue


Vue.js - The Progressive JavaScript Framework

√ 请输入项目名称： ... frontend
√ 是否使用 TypeScript 语法？ ... 否 / 是
√ 是否启用 JSX 支持？ ... 否 / 是
√ 是否引入 Vue Router 进行单页面应用开发？ ... 否 / 是
√ 是否引入 Pinia 用于状态管理？ ... 否 / 是
√ 是否引入 Vitest 用于单元测试？ ... 否 / 是
√ 是否要引入一款端到端（End to End）测试工具？ » 不需要
√ 是否引入 ESLint 用于代码质量检测？ » 是
√ 是否引入 Prettier 用于代码格式化？ ... 否 / 是

正在初始化项目 C:\Users\XYCF\Documents\Code\gym-manager\frontend...

项目初始化完成，可执行以下命令：

  cd frontend
  npm install
  npm run format
  npm run dev
```

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
