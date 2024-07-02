from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    code_postal = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    pays = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    RCS = models.CharField(max_length=255, blank=True, null=True)
    SIRET = models.CharField(max_length=255, blank=True, null=True)
    TVA = models.CharField(max_length=255, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    IBAN = models.CharField(max_length=255, blank=True, null=True)
    BIC = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team_name}'




