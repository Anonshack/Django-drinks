from rest_framework import serializers
from .model import Drink


class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'dictionary']