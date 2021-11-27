from rest_framework import serializers
from .models import Ingredients, Products

class IngredientSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredients.objects.all(), many=True)
    class Meta:
        model = Ingredients
        fields = ('name', 'percentage')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'price', 'sellin_price', 'quantity', 'ingredients']
        depth=1

    def create(self, validated_data,*args, **kwargs):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.sellin_price = validated_data.get('sellin_price', instance.sellin_price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance