from django.contrib.auth.models import User
from django.db import models
from rest_framework import viewsets


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    # tablemo = models.IntegerField()
    # persons =  models.IntegerField()
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name

class Menu(models.Model):
   item = models.CharField(max_length=100)
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='None')

   def __str__(self):
      return self.name
  #add the following method in Menu class
def __str__(self):
       return f'{self.title} : {str(self.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
#    def get_item(self):
#        return f'{self.title} : {str(self.price)}'

#class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated]