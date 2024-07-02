<template>
    <div class="page-invoice">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/factures">Factures</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'Facture', params: { id:invoice.id } }" aria-current="true">{{ invoice.invoice_number }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Facture - {{ invoice.invoice_number }}</h1>
                <div class="buttons">
                    <button class="button is-dark" @click="getPdf()">Telecharger PDF</button>
                    <button class="button is-success" @click="setAsPaid()" v-if="!invoice.is_paid">Valider Paiement</button>
                </div>
            </div>

            <div class="column is-4 mb-4 box">
                <h1 class="title">{{ invoice.client_name }}</h1>

                <p><strong>{{ invoice.client_contact_name }}</strong></p>
                <p v-if="invoice.client_email">{{ invoice.client_email }}</p>
                <p v-if="invoice.client_tel_number">{{ invoice.client_tel_number }}</p>
                <p v-if="invoice.client_address">{{ invoice.client_address }}</p>
                <p v-if="invoice.client_ville || invoice.client_code_postal" >{{ invoice.client_code_postal }} {{ invoice.client_ville }}</p>
                <p v-if="invoice.client_pays">{{ invoice.client_pays }}</p>
            </div>

            <div class="column is-12">
                <h3 class="is-size-4">Produits</h3>

                <table class="table is-fullwidth">  
                    <thead>
                        <tr>    
                            <td>#</td>
                            <td>Produit</td>
                            <td>Quantité</td>
                            <td>Total H.T.</td>
                        </tr>
                    </thead> 

                    <tbody>
                        <tr 
                            v-for="item in invoice.items"
                            v-bind:key="item.id"
                        >   
                            <td>{{ item.item_id }}</td>
                            <td>{{ item.item_name }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ item.total }}</td>
                        </tr>
                    </tbody>
                </table>
            </div> 

            <div class="column is-12">
                <div class="box">
                    <div class="columns">
                        <div class="column is-6">
                            <p><strong>Emis le: </strong>{{ invoice.created_at }}</p>
                            <p><strong>Due au: </strong>{{ invoice.due_date }}</p>
                            <p><strong>Type: </strong>{{ getType() }}</p>
                            <p><strong>Statut: </strong>{{ getStatusLabel() }}</p>
                        </div>

                        <div class="column is-6 justify-flex">
                            <p><strong>Total H.T: </strong>{{ invoice.total_ht }}€</p>
                            <p><strong>T.V.A: </strong>{{ invoice.total_tva }}€</p>
                            <p>Dont:</p>
                            <p>-T.V.A 5: {{ invoice.tva_5 }}€</p>
                            <p>-T.V.A 20: {{ invoice.tva_20 }}€</p>
                            <p><strong>Total T.T.C: </strong>{{ invoice.total_ttc }}€</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

const fileDownload = require('js-file-download')

export default {
    name: 'facture',
    data() {
        return {
            invoice: {},
            items: []
        }
    },
    mounted() {
        this.getInvoice()
    },
    methods: {
        getInvoice() {
            const invoiceId = this.$route.params.id

            axios
                .get(`/api/v1/factures/${invoiceId}`)
                .then(response => {
                    this.invoice = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        getPdf() {
            const invoiceId = this.$route.params.id

            axios
                .get(`/api/v1/factures/${invoiceId}/generate_pdf/`, {
                    responseType: 'blob',
                }).then(res => {
                    fileDownload(res.data, `${this.invoice.invoice_number}-${this.invoice.client_name}.pdf`)
                }).catch(err => {
                    console.log(JSON.stringify(err))
                })
        },
        getStatusLabel() {
            if (this.invoice.is_paid) {
                return 'Payée'
            } else {
                return 'Non Payée'
            }
        },
        getType() {
            if (this.invoice.invoice_type === 'Devis') {
                return 'Devis'
            }   else {
                return 'Facture'
            }
        },
        async setAsPaid() {
            this.invoice.is_paid = true

            let items = this.invoice.items

            delete this.invoice['items']

            await axios
                .patch(`/api/v1/factures/${this.invoice.id}/`, this.invoice)
                .then(response => {
                    toast({
                        message: 'Changement Validé',
                        type: 'is-success',
                        dismissible: 'true',
                        pauseOnHover: 'true',
                        duration: 2000,
                        position: 'top-center',
                    })
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            
            this.invoice.items = items
        }
    }
}
</script>