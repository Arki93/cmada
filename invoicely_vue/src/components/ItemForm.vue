<template>
    <div class="columns">
        <div class="column is-1">
            <div class="field">
                <label>#</label>
                <div class="control">
                    <input type="text" class="input" v-model="item.item_id" disabled>
                </div>
            </div>
        </div>

        <div class="column is-3">
            <div class="field">
                <label>Produit</label>
                <div class="select">
                    <select name="product" v-model="selectedProductId">
                        <option value="">--Choisir un produit--</option>
                        <option
                            v-for="product in products"
                            v-bind:key="product.id"
                            v-bind:value="product.id"
                        >
                            {{ product.product_name }}
                        </option>
                    </select>
                </div>
            </div>
        </div>

        <div class="column is-2">
            <div class="field">
                <label>Prix Unitaire</label>
                <div class="control">
                    <input type="number" class="input" v-model="item.unit_price">
                </div>
            </div>
        </div>

        <div class="column is-2">
            <div class="field">
                <label>Quantité</label>
                <div class="control">
                    <input type="number" class="input" v-model="item.quantity">
                </div>
            </div>
        </div>

        <div class="column is-1">
            <div class="field">
                <label>TVA</label>
                <div class="control">
                    <input type="number" class="input" v-model="item.tva" disabled>
                </div>
            </div>
        </div>

        <div class="column is-2">
            <div class="field">
                <label>Total T.T.C.</label>
                <div class="control">
                    <input type="text" class="input" v-bind:value="total_ttc" disabled>
                </div>
            </div>
        </div>

        <div class="column is-1">
            <div class="field">
                <label>&nbsp;</label>
                <div class="control">
                    <button class="button is-danger" @click="deleteItem">X</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'ItemForm',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem,
            products: [],
            selectedProductId: ''
        }
    },
    async mounted() {
        await this.getProducts()
    },
    watch: {
        selectedProductId(newVal) {
            const selectedProduct = this.products.find(product => product.id === newVal)
            if (selectedProduct) {
                this.item.item_id = selectedProduct.product_id
                this.item.item_name = selectedProduct.product_name
                this.item.unit_price = selectedProduct.product_unit_price
                this.item.tva = selectedProduct.tva
            } else {
                this.item.unit_price = 0
                this.item.tva = 0
            }
        }
    },
    computed: {
        total_ttc() {
            const unit_price = this.item.unit_price;
            const quantity = this.item.quantity;
            const tva = this.item.tva;
            
            this.item.total = unit_price * quantity;

            this.$emit('updatePrice', this.item);

            const tot_ttc = this.item.total + (this.item.total * (tva / 100));

            return parseFloat(tot_ttc.toFixed(2));
        }
    },
    methods: {
        deleteItem() {
            this.$emit('delete-item', this.index)
        },
        getProducts() {
           axios
            .get('/api/v1/products/')
            .then(response => {
                this.products = response.data
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        },
    }
}
</script>
