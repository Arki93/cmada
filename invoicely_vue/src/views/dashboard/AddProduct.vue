<template>
    <div class="page-add-product">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/products">Produits</router-link></li>
                <li class="is-active"><router-link to="/dashboard/products/add" aria-current="true">Ajouter un product</router-link></li>
            </ul>
        </nav>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Ajouter un product</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Reference product</label>

                    <div class="control">
                        <input type="text" name="product_id" class="input" v-model="product.product_id">
                    </div>
                </div>

                <div class="field">
                    <label>Nom du product</label>

                    <div class="control">
                        <input type="text" name="product_name" class="input" v-model="product.product_name">
                    </div>
                </div>

                <div class="field">
                    <label>Type de produit</label>

                    <div class="select">
                        <select name="type" v-model="product.product_type">
                            <option value="">--Choisir Type--</option>
                            <option value="Couverture">Couverture</option>
                            <option value="Tablette">Tablette</option>
                            <option value="Napoolitain">Napolitain</option>
                            <option value="Divers">Divers</option>
                        </select>
                    </div>
                </div>
                <div class="field" v-if="product.product_type">
                    <label>Section</label>
                </div>

                <div class="field">
                    <label>Prix unitaire</label>

                    <div class="control">
                        <input type="number" name="unit_price" class="input" v-model="product.product_unit_price">
                    </div>
                </div>
            </div>

            <div class="column is-6">

                <div class="field">
                    <label>Minimun en stock</label>

                    <div class="control">
                        <input type="number" name="minimun_stock" class="input" v-model="product.minimun_stock">
                    </div>
                </div>

                <div class="field">
                    <label>Commande en cours</label>

                    <div class="control">
                        <input type="number" name="on_going_command" class="input" v-model="product.on_going_command">
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
    name: 'Addproduct',
    data() {
        return {
            product: {
                product_type: ''
            }
        }
    },
    methods: {
        submitForm() {
            axios
                .post('/api/v1/products/', this.product)
                .then(response => {

                    toast({
                        message: 'product Enregisté',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-center',
                    })
                    this.$router.push('/dashboard/products')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
