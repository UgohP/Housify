from django.contrib import admin
from .models import *
# Register your models here.

class VendorApplicationAdmin(admin.ModelAdmin):
     list_display = ['user', 'phone_number1']
     model = VendorApplication
admin.site.register(VendorApplication, VendorApplicationAdmin)

admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(SecurityQuestion)
admin.site.register(VendorVerification)