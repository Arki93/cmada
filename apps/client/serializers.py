from rest_framework import serializers

from .models import Client
from apps.invoice.models import Invoice

class ClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'id',
            'invoice_number',
            'is_paid',
            'total_ht',
            'due_date',
            'invoice_type',
        )

class ClientSerializer(serializers.ModelSerializer):
    invoices = ClientInvoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        read_only_fields = (
            'created_at',
            'created_by',
        )
        fields = (
            'id',
            'contact_name', 
            'company_name', 
            'email',
            'siret', 
            'address',
            'code_postal', 
            'ville',
            'pays',
            'client_reference',
            'tel_number',
            'invoices',
        )