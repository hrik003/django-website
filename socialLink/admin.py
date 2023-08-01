from django.contrib import admin
from socialLink.models import SocialLink

# Register your models here.
class socialLinkAdmin(admin.ModelAdmin):
    list_display= ('sl_name','sl_url','sl_icon','sl_slug')

admin.site.register(SocialLink,socialLinkAdmin)