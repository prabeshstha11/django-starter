from django.db import models

# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    time = models.IntegerField()
    level = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name