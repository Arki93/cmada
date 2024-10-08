from rest_framework import serializers

from .models import ProductStock, Stock, ProductStockArchive

class ProductStockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStock
        
        read_only_fields = (
            'created_at', 
            'modified_at',
            )
        
        fields = (
        'id',
            'product_id',
            'product_name',
            'product_unit_price',
            'product_type',
            'on_going_command',
            'minimun_stock',
            'tva',
        )
        
class ProductStockArchiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStockArchive
        
        read_only_fields = (
            'stock',
            'product',
            'created_at',
            'modified_at',
        )
        
        fields = (
            'id',
            'product_id',
            'product_name',
            'product_qty',
            'product_site',    
            'stock_DDM',
            'entry_status',
        )
        
class StockSerializer(serializers.ModelSerializer):
    products = ProductStockArchiveSerializer(many=True)

    class Meta:
        model = Stock
        
        read_only_fields = (
            'create_at',
            'modified_at',
            'created_by',
            'modified_by',
        )
        
        fields = (
            'id',
            'stock_id',
            'products',
        )
        
    def create(self, validated_data):
        products_data = validated_data.pop('products')
        stock = Stock.objects.create(**validated_data)

        for product_data in products_data:
            ProductStock.objects.create(stock=stock, **product_data)
            
        return stock
    
    def update(self, instance, validated_data):
        products_data = validated_data.pop('product', [])

        # Update the stock instance
        for attr, value in validated_data.products():
            setattr(instance, attr, value)
        instance.save()

        # Handle products
        current_product_ids = [product.id for product in instance.products.all()]
        new_product_ids = [product_data.get('id') for product_data in products_data]

        # Delete products that are no longer in the request
        for product_id in current_product_ids:
            if product_id not in new_product_ids:
                ProductStock.objects.filter(id=product_id).delete()

        # Update or create products
        for product_data in products_data:
            product_id = product_data.get('id')
            if product_id:
                product = ProductStock.objects.get(id=product_id)
                for attr, value in product_data.products():
                    setattr(product, attr, value)
                product.save()
            else:
                ProductStock.objects.create(stock=instance, **product_data)

        return instance
        