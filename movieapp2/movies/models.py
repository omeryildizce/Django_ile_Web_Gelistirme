from pyexpat import model
from django.db import models
from django.core.validators import MinLengthValidator

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(20)])
    image_name = models.CharField(max_length=100)
    image_cover = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField(max_length=100)
class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()


class Person(models.Model):
    genders = (
        ("E", "Erkek"),
        ("K", "Kadın")
    )

    duty_types = (
        ("1", "Görevli"),
        ("2", "Oyuncu"),
        ("3", "Yönetmen"),
        ("4", "Senarist")
    )
    firstname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birth = models.FloatField()
    gender = models.CharField(max_length=1, choices=genders)
    duty_type = models.CharField(max_length=1, choices=duty_types)

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    