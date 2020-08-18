from django.db import models

# Create your models here.
class Type(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class icecream(models.Model):
    flavour1 = models.CharField(max_length=100)
    additionals = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)