from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Breed(models.Model):
    SIZE_CHOICES = [('tiny', 'Tiny'), ('small', 'Small'),
                    ('medium', 'medium'), ('large', 'large')]
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='tiny')
    friendliness = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])


class Dog(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    favoritefood = models.CharField(max_length=10)
    favoritetoy = models.CharField(max_length=10)
