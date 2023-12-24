from rest_framework import serializers
from .models import fooddata

class FoodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = fooddata
        fields = '__all__'
class SingleFoodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = fooddata
        fields = '__all__'
class FoodDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = fooddata
        fields = '__all__'