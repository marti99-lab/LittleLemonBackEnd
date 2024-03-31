from rest_framework import serializers
from .models import MenuItem
from .models import Booking


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class bookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'