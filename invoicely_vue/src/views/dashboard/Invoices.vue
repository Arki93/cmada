<template>
    <div class="page-invoices">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/dashboard/factures" aria-current="true">Factures</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-6">
                <h1 class="title">Factures</h1>
            </div>
            <div class="column is-6 is-flex is-justify-content-flex-end">
                <router-link to="/dashboard/factures/add" class="button is-light">Nouvelle Facture</router-link>
            </div>
            <div class="column is-12">
                <table class="table is-fullwidth is-striped">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Type</th>
                            <th>Client</th>
                            <th>Total H.T.</th>
                            <th>Echéance</th>
                            <th>Statut</th>    
                            <th></th>
                            <!-- <th>Date Emmission</th>  -->                     
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="invoice in invoices"
                            v-bind:key="invoice.id"
                        >
                            <td><router-link :to="{ name: 'Facture', params: { id: invoice.id }}">{{ invoice.invoice_number }}</router-link></td>
                            <td>{{ invoice.invoice_type }}</td> 
                            <td>{{ invoice.client_name}}</td>
                            <td>{{ invoice.total_ht }}€</td>
                            <td 
                                v-if="invoice.due_date"
                            >
                            {{ formatDate(invoice.due_date) }}
                            </td>
                            <td 
                                v-else
                            >
                            -
                            </td>
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
                           <!--  <td 
                                v-if="!invoice.is_paid"
                            >
                                <span :class="['icon-text', statusClass]">
                                <span class="icon">
                                    <i class="fas fa-exclamation-triangle"></i>
                                </span>
                                <span>{{ statusMessage }}</span>
                                </span>

                            </td> -->
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { format } from 'date-fns'

export default {
    name: 'Factures',
    data() {
        return {
            invoices: []
        }
    },
    mounted() {
        this.getInvoices()
    },
    /* computed: {
        statusClass() {
            return `has-text-${this.invoice.get_payment_check[0]}`;
        },
        statusMessage() {
            return this.invoice.get_payment_check[1]
        }
    }, */
    methods: {
        getInvoices() {
            axios
                .get('api/v1/factures')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.invoices.push(response.data[i])
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
        }
    }
}
</script>