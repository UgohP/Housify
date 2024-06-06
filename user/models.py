from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 

# Create your models here.
class VendorApplication(models.Model):
    """class model for vendor application"""
    
    states = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Kastina', 'Kastina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
        ('FCT (Abuja)', 'FCT (Abuja)'),
    ]

    about_us = [
        ('WhatsApp', 'WhatsApp'),
        ('Instagram', 'Instagram'),
        ('X or Twitter', 'X or Twitter'),
        ('Someone', 'Someone'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=states, null=True)
    location = models.TextField(null=True)
    phone_number1 = models.BigIntegerField(null=True)
    phone_number2 = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    how_did_you_here_about_us = models.CharField(max_length=100, choices=about_us, null=True)


    def __str__(self) -> str:
        return str(self.user)
    


class Vendor(models.Model):
    """class model for the vendor"""

    states = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Kastina', 'Kastina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
        ('FCT (Abuja)', 'FCT (Abuja)'),
    ]
        
    vendor = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    state = models.CharField(max_length=100, choices=states, null=True)
    location = models.TextField(null=True)
    vendor_email = models.EmailField(blank=True)
    vendor_phone_number1 = models.BigIntegerField(null=True)
    vendor_phone_number2 = models.BigIntegerField(null=True, blank=True)
    business_whatsapp_number = models.BigIntegerField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)

class VendorVerification(models.Model):
    """"class model for vendorverification"""

    means_of_identification = [
        ("NIN", "NIN"),
        ("Driver's License", "Driver's License"),
        ("Voter's Card", "Voter's Card"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True)
    Means_of_Identification = models.CharField(max_length=100, choices=means_of_identification, null=True)
    front_view = models.ImageField(upload_to='image/', null=True)
    back_view = models.ImageField(upload_to='image/', null=True)
    
    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
    
    
class Customer(models.Model):
    """class model for customer"""
    
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.BigIntegerField(null=True)
    is_vendor = models.BooleanField(default=False, null=True, blank=True)
    in_process = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.customer).capitalize()

class SecurityQuestion(models.Model):
    """class model for security question to reset password"""
    
    username = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True)
    question1 = models.CharField(max_length=255, default="What is your username", blank=True)
    answer1 = models.CharField(max_length=255, default="", blank=True)
    question2 = models.CharField(max_length=255, default="What is your favourite colour?", blank=True)
    answer2 = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)
