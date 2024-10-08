from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    client_reference = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    tel_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    siret = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255, null=True, blank=True)
    ''' created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE) '''
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('company_name',)

    def __str__(self) -> str:
        return f'{self.company_name} - {self.contact_name}'
    
    
        
        


