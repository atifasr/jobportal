from django.contrib import admin

from .models import User, UserLog,Address

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'user_type', 'gender','company')


class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_login_date', 'last_job_apply_date')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state','zip_code','street')


admin.site.register(User, UserAdmin)
admin.site.register(UserLog, UserLogAdmin)
admin.site.register(Address, AddressAdmin)
