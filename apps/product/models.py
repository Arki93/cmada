from django.contrib.auth.models import User

from django.db import models

from django.utils import timezone
from django.db.models import Sum

class Product(models.Model):

    product_id = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_unit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    on_going_command = models.IntegerField(default=0)
    minimun_stock = models.IntegerField(default=0)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tva = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='creater_product', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modifier_product', on_delete=models.CASCADE)

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

