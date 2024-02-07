from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class MenuItem(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False)
   inventory = models.SmallIntegerField(default=10)

   def get_item(self):
    return f'{self.title} : {str(self.price)}'