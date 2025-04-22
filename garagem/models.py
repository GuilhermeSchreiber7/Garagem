from django.db import models

# Create your models here.

class acessory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"
    

class color(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"
    
class category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"
    
class brand(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"
        
class model(models.Model):
    category = models.ForeignKey(category, on_delete=models.PROTECT, related_name='models')
    brand = models.ForeignKey(brand, on_delete=models.PROTECT, related_name='models')
    name = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.category} {self.brand} {self.name}"
    
class vehicle(models.Model):
    color = models.ForeignKey(color, on_delete=models.PROTECT, related_name='vehicles')
    model = models.ForeignKey(model, on_delete=models.PROTECT, related_name='vehicles')
    year = models.IntegerField()
    plate = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    accessories = models.ManyToManyField(acessory, related_name='vehicles')

    def __str__(self):
        return f"{self.color} {self.model} {self.year} {self.plate} {self.price}"

class customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cars = models.ManyToManyField(vehicle, related_name='customers')

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.cars}"
