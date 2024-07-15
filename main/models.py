from django.db import models

# Create your models here.
class Product(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=FEMALE,
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='productimages/')
    price = models.IntegerField()
    
