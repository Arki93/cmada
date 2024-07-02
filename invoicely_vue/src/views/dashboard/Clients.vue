<template>
    <div class="page-clients">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/dashboard/clients" aria-current="true">Clients</router-link></li>
            </ul>
        </nav>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clients</h1>

                <router-link :to="{ name: 'AddClient' }" class="button is-light mt-4">Ajouter un client</router-link>
            </div>

            <div 
                class="column is-3"
                v-for="client in clients"
                v-bind:key="client.id"
            >
                <div class="box">
                    <div class="column">
                        <h3 class="is-size-4 mb-4">{{ client.company_name }}</h3>
                        <p>Tel.: {{ client.tel_number }}</p>
                        <p>Email: {{ client.email }}</p>
                    </div>

                    <router-link :to="{ name: 'Client', params: { id: client.id }}">Details</router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'Clients',
    data() {
        return {
            clients: [] 
        }
    },
    mounted() {
        this.getClients()
    },
    methods: {
        getClients() {
            axios
                .get('/api/v1/clients/')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.clients.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    } 
}
</script>