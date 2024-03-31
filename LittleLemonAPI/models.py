from django.db import models

# Create your models here.  
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    # tablemo = models.IntegerField()
    # persons =  models.IntegerField()
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

class MenuItem(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'