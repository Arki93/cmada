<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>CMada</strong></router-link>
        <a 
          class="navbar-burger" 
          role="button" 
          aria-label="menu" 
          :aria-expanded="isBurgerActive.toString()" 
          @click="toggleBurgerMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" :class="{ 'is-active': isBurgerActive }">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item"><strong>Dashboard</strong></router-link>
            <router-link to="/dashboard/products" class="navbar-item"><strong>Produits</strong></router-link>
            <router-link to="/dashboard/factures" class="navbar-item"><strong>Factures</strong></router-link>
            <router-link to="/dashboard/clients" class="navbar-item"><strong>Clients</strong></router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/mon-compte" class="button is-light">Mon Compte</router-link>
              </div>
            </div>
          </template>

          <template v-else>
            <router-link to="/" class="navbar-item"><strong>Acceuil</strong></router-link>

            <div class="navbar-item">
              <div class="buttons">
                <!-- <router-link to='/sign-up' class="button is-success"><strong>S'inscrire</strong></router-link> -->
                <router-link to='/login' class="button is-light"><strong>Se Connecter</strong></router-link>
              </div>
            </div>
          </template>
        </div>
      </div>
    </nav>


    <section class="section">
      <router-view/>
    </section>

    <footer class="bd-footer footer has-text-centered">
      <p>Built and Maintained by ARStrategy.</p>
    </footer>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'App',
    data() {
      return {
        isBurgerActive: false
      }
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    methods: {
      toggleBurgerMenu() {
        this.isBurgerActive = !this.isBurgerActive
      }
  }
}

</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
