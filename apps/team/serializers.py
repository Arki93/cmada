from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            'created_by',
        ),
        fields = (
            'id',
            'team_name',
            'address',
            'code_postal', 
            'ville',
            'pays', 
            'email',
            'RCS', 
            'SIRET', 
            'TVA',
            'bank',
            'IBAN',
            'BIC'
        )