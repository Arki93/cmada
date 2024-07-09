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

        <div class="column is-5">
            <div class="field">
                <label>Produit</label>
                <div class="control">
                    <v-select 
                    :options="formattedProducts"
                    :reduce="product => product.id"
                    label="product_label"
                    v-model="selectedProductId"
                    searchable
                    clearable
                    placeholder="--Choisir un produit--"
                    />
                </div>
            </div>
        </div>

        <div class="column is-1">
            <div class="field">
                <label>Prix Unitaire</label>
                <div class="control">
                    <input type="number" class="input" v-model="item.unit_price">
                </div>
            </div>
        </div>

        <div class="column is-1">
            <div class="field">
                <label>Remise</label>
                <div class="control">
                    <input type="number" class="input" v-model="item.item_reduction">
                </div>
            </div>
        </div>

        <div class="column is-1">
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

        <div class="column is-1">
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
import { defineComponent } from 'vue';
import VSelect from 'vue3-select';
import 'vue3-select/dist/vue3-select.css';

export default defineComponent({
    name: 'ItemForm',
    props: {
        initialItem: Object
    },
    components: {
    'v-select': VSelect,
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
                this.item.item_reduction = 0
            }
        }
    },
    computed: {
        formattedProducts() {
            return this.products.map(product => ({
            ...product,
            product_label: `${product.product_id}-${product.product_name}`
            }))
        },
        total_ttc() {
            const unit_price = this.item.unit_price;
            const quantity = this.item.quantity;
            const tva = this.item.tva;
            const reduction = this.item.item_reduction;
            
            if (reduction !== 0) {

                this.item.total = parseFloat(((unit_price *(1-reduction/100)) * quantity).toFixed(2));
                
                this.$emit('updatePrice', this.item);

                const tot_ttc = this.item.total + (this.item.total * (tva / 100));

                return parseFloat(tot_ttc.toFixed(2));
            } else {
                this.item.total = parseFloat((unit_price * quantity).toFixed(2));

                this.$emit('updatePrice', this.item);

                const tot_ttc = this.item.total + (this.item.total * (tva / 100));

                return parseFloat(tot_ttc.toFixed(2));
            }
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
})
</script>
