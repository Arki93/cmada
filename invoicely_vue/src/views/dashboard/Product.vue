<template>
    <div class="page-product">
        <nav class="breadcrumb" aria-label="breadcrumb">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/dashboard/products">Produits</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'Product', params: { id:product.id } }" aria-current="true">{{ product.product_name }}</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="Title">{{ product.product_name }}</h1>

                <!-- <router-link :to="{ name: 'Updateproduct', params: { id: product.id }}" class="button is-light mt-4">Modifier</router-link> -->
            </div>

            <div class="column is-6">
                <p><strong>{{ product.product_name }}</strong></p>
                <p v-if="product.product_id">{{ product.product_id }}</p>
                <p v-if="product.product_unit_price">Prix: {{ product.product_unit_price }}</p>
                <p v-if="product.tva">{{ product.tva }}</p>
                <p v-if="product.product_quantity"> {{ product.product_quantity }}</p>
                <p v-if="product.on_going_command">{{ product.on_going_command }}</p>
            </div>

            <div class="column is-6">
                <p><strong>Quantité: </strong>{{  }}</p>
                <p><strong>Derniere MaJ: </strong>{{ stock.created_at }}</p>
            </div>

            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Produits</h2>

                    <table class="table is-fullwidth">
                        <thead>
                        <tr>
                            <th>Site</th>
                            <th>Quantité</th>
                            <th>DDM</th>
                            <th>Date de création</th>
                            <th>Derniere MaJ</th>
                            <th></th>
                        </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="item in stock"
                                v-bind:key="item.id"
                            >
                                <td>{{ item.product_site }}</td>
                                <td>{{ item.product_qty }}</td>
                                <td>{{ item.stock_DDM }}</td>
                                <td>{{ item.created_at }}</td>
                                <td>{{ item.modified_at }}</td>
                                <th></th>
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
    name: 'Product',
    data() {
        return {
            product: {},
            stock: []
        }
    },
    mounted() {
        this.getProduct(),
        this.getStock()
    },
    methods: {
        async getProduct() {
            const productId = this.$route.params.id

            await axios
                .get(`/api/v1/products/${productId}`)
                .then(response => {
                    this.product = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        formatDate(date) {
            return format(new Date(date), 'dd.MM.yy')
        },
        getStock() {
            axios
                .get('api/v1/stock')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        if (response.data[i].product === this.product.id){
                            this.stock.push(response.data[i])
                        }
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
