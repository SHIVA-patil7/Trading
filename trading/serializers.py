from rest_framework import serializers
from .models import MemeCoin

class MemeCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemeCoin
        fields = "__all__"
