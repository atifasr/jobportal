from django.contrib import admin

from .models import User, UserLog

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'user_type', 'gender')


class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_login_date', 'last_job_apply_date')


admin.site.register(User, UserAdmin)
admin.site.register(UserLog, UserLogAdmin)
