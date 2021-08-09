from django.db import models

# Create your models here.
class Sign_up(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)

        
# class Validate(models.Model):
#     email = models.OneToOneField()


class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=12)
    msg = models.CharField(max_length=1000)


    def __str__(self):
        return str(self.email)
