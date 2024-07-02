from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from apps.client.models import Client
from apps.team.models import Team

import decimal

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
    reduction = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    team = models.ForeignKey(Team, related_name='factures', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, related_name='factures', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='creater_factures', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modifier_factures', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def generate_invoice_number(self):
        # Define the base format for the invoice number
        date_str = now().strftime('%Y%m%d')
        last_invoice = Invoice.objects.filter(invoice_number__startswith='F' + date_str).order_by('invoice_number').last()
        if last_invoice:
            last_number = last_invoice.invoice_number[-4:]
        else:
            last_number = 0
        new_number = int(last_number) + 1
        return f'F{date_str}-{new_number:04d}'
    
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
    item_id = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    tva = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    reduction = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def get_total_ttc(self):
        tva = decimal.Decimal(self.tva/100)
        return round(self.total + (self.total * tva),2)

    def get_tva(self):
        tva = decimal.Decimal(self.tva/100)
        return round(self.unit_price * tva,2)



