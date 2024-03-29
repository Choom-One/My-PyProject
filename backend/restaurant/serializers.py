from .models import *
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
        
class OrderItemListSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
