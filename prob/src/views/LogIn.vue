<template class="page">
  <div>
    <button @click="login">Log in</button>
  </div>
</template>
<script>
// Composition API
import { useAuth0 } from '@auth0/auth0-vue'

export default {
  setup () {
    const auth0 = useAuth0()

    return {
      login () {
        auth0.loginWithRedirect()
      }
    }
  }
}
</script>
