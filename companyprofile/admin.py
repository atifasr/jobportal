from django.contrib import admin

from .models import *

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'name',
                    'prof_description', 'estab_date', 'company_website')


class CompanyImageAdmin(admin.ModelAdmin):
    list_display = ('cover_image', 'images', 'company')


class BuisnessStreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'buisness_stream_name')


admin.site.register(CompanyImage, CompanyImageAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(BuisnessStream, BuisnessStreamAdmin)
