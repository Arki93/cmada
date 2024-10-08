from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from apps.client.models import Client
from apps.team.models import Team

from decimal import Decimal

class Invoice(models.Model):
    FACTURE = 'Facture'
    DEVIS = 'Devis'

    CHOISES_TYPE = (
        (FACTURE, 'Facture'),
        (DEVIS, 'Devis'),
    )

    invoice_number = models.CharField(max_length=20, unique=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_email = models.CharField(max_length=255, null=True, blank=True)
    client_siret = models.CharField(max_length=255, blank=True, null=True)
    client_address = models.CharField(max_length=255, blank=True, null=True)
    client_cp = models.CharField(max_length=255, blank=True, null=True)
    client_pays = models.CharField(max_length=255, blank=True, null=True)
    client_ville = models.CharField(max_length=255, blank=True, null=True)
    client_company = models.CharField(max_length=255, blank=True, null=True)
    invoice_type = models.CharField(max_length=20, choices=CHOISES_TYPE, default=FACTURE)
    due_date = models.DateField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    total_ht = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_tva = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tva_5 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tva_20 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_ttc = models.DecimalField(max_digits=6, decimal_places=2)
    invoice_reduction = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    team = models.ForeignKey(Team, related_name='factures', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, related_name='factures', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='creater_factures', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modifier_factures', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        
    def payment_check(self):
        pass

    def generate_invoice_number(self):
        # Define the base format for the invoice number
        date_str = now().strftime('%Y')
        last_d = now().strftime('%d%m')
        last_invoice = Invoice.objects.filter(invoice_number__startswith='F' + date_str).order_by('invoice_number').last()
        if last_invoice:
            last_number = last_invoice.invoice_number[5:8]
        else:
            last_number = 0
        new_number = int(last_number) + 1
        return f'F{date_str}{new_number:03d}-{last_d}'
    
    """ def get_payment_check(self):
        if not self.due_date:
            return ('info', 'No due date set')
            
        delta = (self.due_date - now()).days
        
        if not self.is_paid:
            if delta < 5:
                return ('warning', f'Delais de paiement J-{delta}')
            elif delta <= 0:
                return ('danger', 'Delais de paiement depassé')

        return ('success', 'Invoice is paid') """

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    item_num = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=1)  
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    tva = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    item_reduction = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    
    def get_total_ttc(self):
        tva = Decimal(self.tva) / 100
        if self.item_reduction != 0:
            subtotal = self.get_reduct_price() * self.quantity
        else:
            subtotal = self.unit_price * self.quantity
            
        return round(subtotal + (subtotal * tva), 2)

    def get_tva(self):
        tva = Decimal(self.tva) / 100
        return round(self.unit_price * tva, 2)

    def get_reduct_price(self):
        reduction = Decimal(self.item_reduction) / 100
        return round(self.unit_price * (1 - reduction), 2)

    def get_reduct_tva(self):
        reduction_price = self.get_reduct_price()
        tva = Decimal(self.tva) / 100
        return round(reduction_price * tva, 2)



