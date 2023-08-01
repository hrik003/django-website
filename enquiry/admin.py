from django.contrib import admin
from enquiry.models import Enquiry

# Register your models here.
class enquiryAdmin(admin.ModelAdmin):
    list_display= ('en_name','en_email','en_phone','en_message')

admin.site.register(Enquiry,enquiryAdmin)