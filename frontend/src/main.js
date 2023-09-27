import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/router.js"
import { backendDomain } from "@/config.js"

const app = createApp(App)

app.config.globalProperties.$backendDomain = backendDomain;

app.use(router).mount('#app')
