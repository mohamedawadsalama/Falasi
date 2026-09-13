from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email']
    
admin.site.register(CustomUser, CustomUserAdmin)



class CareerAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "position", "date")
  search_fields = ['position']
  
admin.site.register(Career, CareerAdmin)


class ContactAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "subject", "date")
  search_fields = ['subject']
  
admin.site.register(Contact, ContactAdmin)

class EnquiryAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "service", "phone", "date")
  search_fields = ['service']
  
admin.site.register(Enquiry, EnquiryAdmin)