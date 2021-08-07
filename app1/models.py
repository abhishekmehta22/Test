from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    pwd = models.CharField(max_length=100)
    cpwd = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)

        
