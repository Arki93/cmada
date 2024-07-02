<template>
    <div class="page-update-team">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/mon-compte">Mon Compte</router-link></li>
                <li><router-link to="/dashboard/mon-compte/update-team">Modifier Parametre</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Team Control</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Nom</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.team_name">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>
                    <div class="control">
                        <input type="email" class="input" v-model="team.email">
                    </div>
                </div>

                <div class="field">
                    <label>Adresse</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.address">
                    </div>
                </div>

                <div class="field">
                    <label>Ville</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.ville">
                    </div>
                </div>

                <div class="field">
                    <label>Code Postal</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.code_postal">
                    </div>
                </div>

                <div class="field">
                    <label>Pays</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.pays">
                    </div>
                </div>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>RCS</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.RCS">
                    </div>
                </div>

                <div class="field">
                    <label>Siret</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.SIRET">
                    </div>
                </div>

                <div class="field">
                    <label>T.V.A</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.TVA">
                    </div>
                </div>

                <div class="field">
                    <label>Banque</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.bank">
                    </div>
                </div>

                <div class="field">
                    <label>IBAN</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.IBAN">
                    </div>
                </div>

                <div class="field">
                    <label>BIC</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.BIC">
                    </div>
                </div>
            </div>
            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Enregistrer</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Dashboard from './Dashboard.vue'
import { toast } from 'bulma-toast'

export default {
  components: { Dashboard },
    name: 'UpdateTeam',
    data() {
        return{
            team: {}
        }
    },
    async mounted() {
        await this.getOrCreateTeam()
    },
    methods: {
        getOrCreateTeam() {
            axios
                .get('/api/v1/teams/')
                .then(response => {
                    this.team = response.data[0]
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        submitForm() {
            axios
                .patch(`api/v1/teams/${this.team.id}/`, this.team)
                .then(response => {
                    toast({
                        message: 'Changement Enregister',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-center',
                    })

                    this.$router.push('/dashboard/mon-compte')  
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
