from django.db import models
from user.models import Vendor
from core.models import Categorie

# Create your models here.
class Product(models.Model):
    """A class model to feature all the products"""
    
    negotiate = [
        ('Negotiable', 'Negotiable'),
        ('Unnegotiable', 'Unnegotiable'),
    ]

    sex = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unisex', 'Unisex'),
    ]

    created_by = models.ForeignKey(Vendor, related_name = "fashion_vendors", on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='product', null=True)
    gender = models.CharField(max_length=10, choices=sex, default='Unisex', null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'image/', null=True) 
    image2 = models.ImageField(upload_to = 'image/', null=True, blank= True)    
    image3 = models.ImageField(upload_to = 'image/', null=True, blank= True)    
    image4 = models.ImageField(upload_to = 'image/', null=True, blank= True)    
    image5 = models.ImageField(upload_to = 'image/', null=True, blank= True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return str(self.created_by).capitalize()
        # return self.product_name

    class Meta:
        ordering = ('-created',)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def image4URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url
    @property
    def image5URL(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

