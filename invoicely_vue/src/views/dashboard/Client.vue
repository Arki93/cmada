<template>
    <div class="page-client">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/clients">Clients</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'Client', params: { id:client.id } }" aria-current="true">{{ client.company_name }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="Title">{{ client.company_name }}</h1>

                <router-link :to="{ name: 'UpdateClient', params: { id: client.id }}" class="button is-light mt-4">Modifier</router-link>
            </div>

            <div class="column is-6">
                <p><strong>{{ client.contact_name }}</strong></p>
                <p v-if="client.email">{{ client.email }}</p>
                <p v-if="client.tel_number">{{ client.tel_number }}</p>
                <p v-if="client.address">{{ client.address }}</p>
                <p v-if="client.ville || client.code_postal" >{{ client.code_postal }} {{ client.ville }}</p>
                <p v-if="client.pays">{{ client.pays }}</p>
            </div>

            <div class="column is-6">
                <p><strong>Nombre de Commande: </strong>{{ getNbCommand() }}</p>
                <p><strong>C.A Client: </strong>{{ getTotalHt() }}€</p>
                <p><strong>Factures Non Payées: </strong>{{ getUnpaidNb() }}</p>
                <p><strong>Devis en Cours: </strong>{{ getNbDevis() }}</p>
            </div>

            <div class="column is-12" v-if="getNbDevis() != 0">
                <div class="box">
                    <h2 class="subtitle">Devis</h2>

                    <table class="table is-fullwidth">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Total H.T</th>
                        </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="invoice in devisInvoices"
                                v-bind:key="invoice.id"
                            >
                                <td><router-link :to="{ name: 'Facture', params: { id: invoice.id }}">{{ invoice.invoice_number }}</router-link></td>
                                <td>{{ invoice.total_ht }}€</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Factures</h2>

                    <table class="table is-fullwidth">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Total H.T</th>
                            <th>Echeance</th>
                            <th>Statut</th>
                        </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="invoice in factureInvoices"
                                v-bind:key="invoice.id"
                            >
                                <td><router-link :to="{ name: 'Facture', params: { id: invoice.id }}">{{ invoice.invoice_number }}</router-link></td>
                                <td>{{ invoice.total_ht }}€</td>
                                <td>{{ invoice.due_date }}</td>
                                <td 
                                v-if="invoice.is_paid"
                            >
                                <button class="button is-success">{{ getStatusLabel(invoice) }}</button>
                            </td>
                            <td 
                                v-else
                            >
                                <button class="button is-danger">{{ getStatusLabel(invoice) }}</button>
                            </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'Client',
    data() {
        return {
            client: {},
            invoices: []
        }
    },
    mounted() {
        this.getClient(),
        this.getInvoices()
    },
    methods: {
        async getClient() {
            const clientId = this.$route.params.id

            await axios
                .get(`/api/v1/clients/${clientId}`)
                .then(response => {
                    this.client = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        async getInvoices() {
            await axios
                .get('api/v1/factures')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        if (response.data[i].client === this.client.id){
                            this.invoices.push(response.data[i])
                        }
                        
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        formatDate(date) {
            return format(new Date(date), 'dd.MM.yy')
        },
        getStatusLabel(invoice) {
            if (invoice.is_paid) {
                return 'Payée'
            } else {
                return 'Non Payée'
            }
        },
        getTotalHt() {
            let total = 0
            
            for (let i = 0; i < this.invoices.length; i++) {
                if (this.invoices[i].invoice_type != 'Devis') {
                    total += parseFloat(this.invoices[i].total_ht)
                } 
            }

            return total.toFixed(2)
        },
        getNbCommand() {
            return this.invoices.length
        },
        getUnpaidNb() {
            return this.invoices.filter(invoice => !invoice.is_paid).length
        },
        getNbDevis() {
            return this.invoices.filter(invoice => invoice.invoice_type === 'Devis').length
        }
    },
    computed: {
        devisInvoices() {
            return this.invoices.filter(invoice => invoice.invoice_type === 'Devis')
        },
        factureInvoices() {
            return this.invoices.filter(invoice => invoice.invoice_type !== 'Devis')
        },
    }
}
</script>
