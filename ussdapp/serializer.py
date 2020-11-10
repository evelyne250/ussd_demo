from rest_framework import serializers
from .models import Ussd

class UssdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ussd
        fields = ('__all__')