<template>
    <div class="page-add-client">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/clients">Clients</router-link></li>
                <li class="is-active"><router-link to="/dashboard/clients/add" aria-current="true">Ajouter un client</router-link></li>
            </ul>
        </nav>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Ajouter un Client</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Entreprise</label>

                    <div class="control">
                        <input type="text" name="company_name" class="input" v-model="client.company_name">
                    </div>
                </div>

                <div class="field">
                    <label>Contact</label>

                    <div class="control">
                        <input type="text" name="contact_name" class="input" v-model="client.contact_name">
                    </div>
                </div>

                <div class="field">
                    <label>Email</label>

                    <div class="control">
                        <input type="email" name="email" class="input" v-model="client.email">
                    </div>
                </div>

                <div class="field">
                    <label>Tel.</label>

                    <div class="control">
                        <input type="text" name="tel" class="input" v-model="client.tel_number">
                    </div>
                </div>
            </div>
            <div class="column is-6">
                <div class="field">
                    <label>Adresse</label>

                    <div class="control">
                        <input type="text" name="address" class="input" v-model="client.address">
                    </div>
                </div>

                <div class="field">
                    <label>Code Postal</label>

                    <div class="control">
                        <input type="text" name="code_postal" class="input" v-model="client.code_postal">
                    </div>
                </div>

                <div class="field">
                    <label>Ville</label>

                    <div class="control">
                        <input type="text" name="ville" class="input" v-model="client.ville">
                    </div>
                </div>

                <div class="field">
                    <label>Pays</label>

                    <div class="control">
                        <input type="text" name="pays" class="input" v-model="client.pays">
                    </div>
                </div>
            </div>
            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Enregister</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'AddClient',
    data() {
        return {
            client: {}
        }
    },
    methods: {
        submitForm() {
            axios
                .post('api/v1/clients/', this.client)
                .then(response => {

                    toast({
                        message: 'Client Enregisté',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-center',
                    })
                    this.$router.push('/dashboard/clients')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
