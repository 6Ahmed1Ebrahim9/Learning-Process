from django.db import models

# Create your models here.
# we dont need to create a primary key because django will do it for us automatically
# or we can create our own primary key by adding id = models.anythingField(primary_key=True)
class Product(models.Model):
    title = models.CharField(max_length=255) # because it is limited
    description = models.TextField() # because it can be long
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True) # auto_now=True means it will update every time we save the model
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # email field will validate that it is a valid email and unique=True means it can only be used once
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True) # null=True means it can be empty