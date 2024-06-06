from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def createCustomerProfile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(customer=instance)
        print('profile created')

@receiver(post_save, sender=User)
def updateCustomerProfile(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        print('profile updated')

@receiver(post_save, sender=User)
def createVendorProfile(sender, instance, created, **kwargs):
    if created:
        Vendor.objects.create(vendor=instance)
        print('vendor created')

@receiver(post_save, sender=User)
def updateVendorProfile(sender, instance, created, **kwargs):
    if created == False:
        instance.vendor.save()

