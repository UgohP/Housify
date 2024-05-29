from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# from user.models import *
# Create your models here.

class Categorie(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    category_image = models.ImageField(upload_to='image/', null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Categorie,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

class Carousel(models.Model):
    carousel = models.ImageField(upload_to = 'image/', null=True)

    def __str__(self):
        slides = "{}".format(self.carousel)
        return slides

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"
        
    def __str__(self) -> str:
        return str(self.user).capitalize()

    