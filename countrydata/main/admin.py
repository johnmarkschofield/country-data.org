from django.contrib import admin
from .models import Country
from .models import CIAWFBEntry
from .models import CIAWFBFieldInfo

admin.site.register(Country)
admin.site.register(CIAWFBEntry)
admin.site.register(CIAWFBFieldInfo)

# class CIAWFBFieldInfoAdmin(admin.ModelAdmin):
#     fields = ['field_name', 'field_group', 'field_order_number', 'field_description']
#     ordering = ['-field_group', 'field_order_number', 'field_name']
#     list_display = ['field_name', 'field_group', 'field_order_number']

# admin.site.register(CIAWFBFieldInfo, CIAWFBFieldInfoAdmin)
