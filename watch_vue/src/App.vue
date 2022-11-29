
<template xmlns="http://www.w3.org/1999/html">
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Watch</strong></router-link>

          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = ! showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
       </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <router-link to="/mens" class="navbar-item">Men's watches</router-link>
            <router-link to="/womens" class="navbar-item">Women's watches.</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/log-in" class="button is-light">Log in</router-link>

                <router-link to="/cart" class="button is-success ">
                  <span class="icon"><el-icon><ShoppingCartFull /></el-icon></span>
                  <span>Cart</span>
                </router-link>

              </div>
            </div>
          </div>
      </div>
    </nav>
    <section class="section">
       <router-view/>
    </section>
        <footer class="footer">
          <p class="has-text-centered">Copyright (c) 2022</p>
        </footer>
  </div>

</template>


<style lang="scss">
@import "../node_modules/bulma";
</style>

<script setup>
import {ShoppingCartFull} from '@element-plus/icons-vue'

</script>

<script>
export default  {
  data() {
    return {
      showMobileMenu:false,
    }
  }
}
</script>
