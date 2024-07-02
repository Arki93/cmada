<template>
    <div class="page-products">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/dashboard/products" aria-current="true">Produits</router-link></li>
            </ul>
        </nav>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Produits</h1>

                <router-link :to="{ name: 'AddProduct' }" class="button is-light mt-4">Ajouter un produit</router-link>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth is-striped">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Produit</th>
                            <th>Type</th>
                            <th>Quantité</th>
                            <th>Commande en cours</th>  
                            <!-- <th>Date Emmission</th>  -->                     
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="product in products"
                            v-bind:key="product.id"
                        >
                            <td><router-link :to="{ name: 'Product', params: { id: product.id }}">{{ product.product_id }}</router-link></td>
                            <td>{{ product.product_name }}</td> 
                            <td>{{ product.product_type}}</td>
                            <td>{{ product.quantity}}</td>
                            <td>{{ product.on_going_command}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Products',
    data() {
        return {
            products: [] 
        }
    },
    mounted() {
        this.getProduits()
    },
    methods: {
        getProduits() {
            axios
                .get('/api/v1/products/')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.products.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    } 
}
</script>