from rest_framework import serializers
from .models import *

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DishOfOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesOfOrder
        fields = '__all__'