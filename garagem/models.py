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
    category = models.ForeignKey(category, on_delete=models.PROTECT)
    brand = models.ForeignKey(brand, on_delete=models.PROTECT)
    name = models.CharField(max_length = 100) 

    def __str__(self):
        return f"{self.category} {self.brand} {self.name}"
    
class vehicle(models.Model):
    color = models.ForeignKey(color, on_delete=models.PROTECT)
    model = models.ForeignKey(model, on_delete=models.PROTECT)
    year = models.IntegerField(max_length=4)
    plate = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    accessories = models.ManyToManyField(acessory)

    def __str__(self):
        return f"{self.color} {self.model} {self.year} {self.plate} {self.price}"



