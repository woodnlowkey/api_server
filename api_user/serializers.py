from rest_framework import serializers
from .models import Bread, Topping, Cheese, Sauce, Sandwich
 
class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = '__all__'

class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = '__all__'

class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = '__all__'