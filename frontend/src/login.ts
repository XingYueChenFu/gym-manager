// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './LoginIndex.vue'
import router from './router/loginRouter.ts'


const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
