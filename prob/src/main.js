import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { createAuth0 } from '@auth0/auth0-vue'

createApp(App).use(store).use(router).use(
  createAuth0({
    domain: 'dev-hjwwa3u2bt3atz2h.eu.auth0.com',
    client_id: 'bDKP6liDKtpVLmmaVISdMgO3hpezPKOn',
    redirect_uri: window.location.origin
  })
).mount('#app')
