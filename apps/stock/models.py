from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class Stock(models.Model):
    
    stock_id = models.CharField(max_length=20, unique=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name='modifier_stock', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='creater_stock', on_delete=models.SET_NULL, null=True, blank=True)
        
class ProductStock(models.Model):
    
    product_id = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_unit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    on_going_command = models.IntegerField(default=0)
    minimun_stock = models.IntegerField(default=0)
    tva = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='create_product', on_delete=models.CASCADE, null=True, blank=True)
    modified_by = models.ForeignKey(User, related_name='modify_product', on_delete=models.CASCADE, null=True, blank=True)

    def set_tva(self):
        if self.product_name:
            if 'lait' in self.product_name.lower() or 'blanc' in self.product_name.lower():
                return 20
            else:
                return 5.5
            
    def custom_title_case(self, s):
        exceptions = {'de', 'au', 'et', 'à', 'la', 'aux'}
        return ' '.join(word.capitalize() if word not in exceptions else word for word in s.split())

  
    def __str__(self):
        return f'{self.product_id} {self.product_name}'

    def save(self, *args, **kwargs):
        if not self.tva:
            self.tva = self.set_tva()
        if self.product_name:
            self.product_name = self.custom_title_case(self.product_name)
        super().save(*args, **kwargs)

class ProductStockArchive(models.Model):
    
    SITE_CHOISES = (
        ('LIL', 'Lille'),
        ('VIO', 'Violet'),
        ('VIA', 'Viaduc'),
        ('LOU', 'Lourmel'),
    )
    
    stock = models.ForeignKey(Stock, related_name='stock',on_delete=models.CASCADE)
    product = models.ForeignKey(ProductStock, related_name='stock_product',on_delete=models.CASCADE)
    product_stock_id = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_qty = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_site = models.CharField(choices=SITE_CHOISES, max_length=10)    
    stock_DDM = models.DateField(null=True)
    entry_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    
    def ddm_check(self):
        if self.stock_DDM:        
            today = timezone.now().date()
            ddm_exp = (self.stock_DDM - today).days
            return ddm_exp < 90
        else:
            return False
    
    def __str__(self):
        return f'{self.product_id} {self.product_name}'




    

