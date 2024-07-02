<template>
    <div class="page-my-account">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/dashbooard/mon-compte" aria-current="true">Mon Compte</router-link></li>
            </ul>
        </nav>
        
        <div class="columns is-multiline">
            <div class="column is-6">
                <h1 class="title">Mon Compte</h1>
                <strong>{{ $store.state.user.username }}</strong>
                <strong>{{ team.team_name }}</strong>

            </div>
            
            <div class="column is-6 is-flex is-justify-content-flex-end">
                <div class="buttons">
                    <router-link to="/dashboard/mon-compte/update-team" class="button is-light">Info</router-link>
                    <button @click="logout()" class="button is-danger">Se Deconnecter</button>
                </div>
            </div>

           <div 
                class="column is-3"
                v-for="team in teams"
                v-bind:key="team.id"
            >
                <div class="box">
                    <h3 class="is-size-4 mb-4">{{ team.team_name }}</h3>
                    <h4 class="is-size-6 mb-4">RCS {{ team.RCS }}</h4>
                    <h4 class="is-size-6 mb-4">SIRET {{ team.SIRET }}</h4>
                    <h4 class="is-size-6 mb-4">TVA {{ team.TVA }}</h4>

                </div>
            </div>
        </div>

        
    </div>
</template>

<script>
import axios from 'axios'
import Dashboard from './Dashboard.vue'
export default {
  components: { Dashboard },
    name: 'MonCompte',
    data() {
        return {
            team: {}
        }
    },
    async mounted() {
         await this.getOrCreateTeam()
    },
    methods: {
        logout() {
            axios
                .post('api/v1/token/logout')
                .then(response => {
                    axios.defaults.headers.common['Authorization'] = ''

                    localStorage.removeItem('username')
                    localStorage.removeItem('userid')
                    localStorage.removeItem('token')

                    this.$store.commit('removeToken')

                    this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }

                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                        console.log(JSON.stringify(error.response))
                    } else {
                        console.log(JSON.stringify(error))
                    }
                })
        },
        getOrCreateTeam() {
            axios
                .get('/api/v1/teams/')
                .then(response => {
                    this.team = response.data[0]
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }      
    }
}
</script>
