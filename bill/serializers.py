from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'name', 'user_id', 'title', 'price', 'quantity', 'amount']
        depth=1

    def create(self, validated_data,*args, **kwargs):
        return Bill.objects.create(**validated_data)