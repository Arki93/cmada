<template>
    <div class="page-new-invoice">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/factures">Factures</router-link></li>
                <li class="is-active"><router-link to="/dashboard/factures/add" aria-current="true">Ajouter une facture</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Nouvelle Facture</h1>
            </div>

            <div class="column is-6">
                <h2 class="is-size-5 mb-4">Client</h2>

                <div class="select">
                    <select name="client" v-model="invoice.client">
                        <option value="">--Choisir un Client--</option>
                        <option
                            v-for="client in clients"
                            v-bind:key="client.id"
                            v-bind:value="client"
                        >
                            {{ client.company_name }}
                        </option>
                    </select>
                </div>

                <div class="box mt-4" v-if="invoice.client">
                    <p><strong>{{ invoice.client.company_name }}</strong></p>
                    <p>{{ invoice.client.address }}</p>
                    <p>{{ invoice.client.code_postal }} {{ invoice.client.ville }}</p>
                    <p>{{ invoice.client.pays }}</p>
                </div>
            </div>
            <div class="column is-2">
                <h2 class="is-size-5 mb-4">Echéance</h2>
                
                <div class="control">
                    <input type="date" class="input" v-model="invoice.due_date" required>
                </div>
            </div>

            <!-- <div class="column is-2">
                <h2 class="is-size-5 mb-4">Type</h2>

                <div class="select">
                    <select name="type" v-model="invoice.invoice_type">
                        <option value="">--Choisir Type--</option>
                        <option value="Facture">Facture</option>
                        <option value="Devis">Devis</option>
                    </select>
                </div>
            </div> -->

            <div class="column is-12">
                <h2 class="is-size-5 mb-4">Produits</h2>

                <ItemForm
                    v-for="(item, index) in invoice.items"
                    :key="item.item_num"
                    :initialItem="item"
                    :index="index"
                    @delete-item="removeItem"
                    v-on:updatePrice="updateTotals"
                >
                </ItemForm>

                <button class="button is-light" @click="addItem"><strong>+</strong></button>
            </div>
        </div>

        <div class="column is-12"
            v-if="invoice.total_ht != 0"
        >
            <h2 class="is-size-5 mb-4">Total</h2>

            <p><strong>Total H.T.:</strong> {{ invoice.total_ht }}€</p>
            <p v-if="invoice.invoice_reduction != 0">-Reduction: {{ invoice.invoice_reduction }}€</p>
            <p><strong>T.V.A:</strong> {{ invoice.total_tva }}€</p>
            <p v-if="invoice.tva_5 != 0 || invoice.tva_20 != 0">Dont:</p>
            <p v-if="invoice.tva_5 != 0">-T.V.A 5.5%: {{ invoice.tva_5 }}€</p>
            <p v-if="invoice.tva_20 != 0">-T.V.A 20%: {{ invoice.tva_20 }}€</p>
            <p><strong>Total T.T.C:</strong> {{ invoice.total_ttc }}€</p>
        </div>

        <div class="column is-12">
            <button class="button is-success" @click="submitForm">Enregister</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ItemForm from '@/components/ItemForm.vue'
import Invoice from './Invoice.vue'

export default {
   name: 'NewInvoice',
   components: {
       ItemForm,
        Invoice
   },
   data() {
       return {
           invoice: {
               client: '',
               /* invoice_type: '', */
               items: [
                   {
                       item_num: 0,
                       item_id: '',
                       item_name: '',
                       unit_price: '',
                       quantity: 1,
                       tva: 0,
                       total: 0,
                       item_reduction: 0,
                   }
               ],
               due_date: '',
               total_ht: 0,
               total_tva: 0,
               tva_5: 0,
               tva_20: 0,
               total_ttc: 0,
               invoice_reduction: 0
           },
           clients: []
       }
   },
   async mounted() {
       await this.getClients()
   },
   methods: {
        getClients() {
           axios
            .get('/api/v1/clients/')
            .then(response => {
                this.clients = response.data
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        },
        addItem() {
           this.invoice.items.push({
                item_num: this.invoice.items.length,
                item_name: '',
                item_id: '',
                unit_price: '',
                quantity: 1,
                tva: 0,
                total_ht: 0,
                item_reduction: 0,
           })
        },
        removeItem(index) {
           this.invoice.items.splice(index, 1)
        },
        updateTotals(changedItem) {
           let total_ht = 0
           let tva_20 = 0
           let tva_5 = 0
           let reduction = 0

           let item = this.invoice.items.filter(i => i.item_num === changedItem.item_num)

           item = changedItem
           for (let i = 0; i < this.invoice.items.length; i++) {
               const tx_tva = this.invoice.items[i].tva
               const tx_red = this.invoice.items[i].item_reduction

               if (tx_tva == 5.5) {
                   tva_5 += this.invoice.items[i].total * (tx_tva/100)
               }
               else{
                   tva_20 += this.invoice.items[i].total * (tx_tva/100)
               }
               
               if (tx_red != 0) {
                    reduction += this.invoice.items[i].quantity * this.invoice.items[i].unit_price * (tx_red/100)
               }
               total_ht += this.invoice.items[i].total
           }

           const tva = tva_5 + tva_20;

           this.invoice.total_ht = parseFloat(total_ht.toFixed(2))
           this.invoice.total_tva = parseFloat(tva.toFixed(2))
           this.invoice.tva_20 = parseFloat(tva_20.toFixed(2))
           this.invoice.tva_5 = parseFloat(tva_5.toFixed(2))
           this.invoice.total_ttc = parseFloat((total_ht + tva).toFixed(2))
           this.invoice.invoice_reduction = parseFloat(reduction.toFixed(2))
         },
        submitForm() {
           
           this.invoice.client_name = this.invoice.client.company_name
           this.invoice.client_email = this.invoice.client.email
           this.invoice.client_company = this.invoice.client.company
           this.invoice.client_address = this.invoice.client.address
           this.invoice.client_cp = this.invoice.client.code_postal
           this.invoice.client_ville = this.invoice.client.ville
           this.invoice.client_pays = this.invoice.client.pays
           this.invoice.client = this.invoice.client.id

           axios
            .post('/api/v1/factures/', this.invoice)
            .then(response => {
                toast({
                    message: 'La facture a été enregistrée',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'top-center'
                })

                this.$router.push('/dashboard/factures')
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
       }
   }
}
</script>

<style lang="scss">
    .select, .select select{
        width: 100%;
    }
</style>