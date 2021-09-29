from django.contrib import admin

from .models import User, UserLog,Address,MessageThreads,Messages

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'user_type', 'gender','company')


class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_login_date', 'last_job_apply_date')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state','zip_code','street')


class MessageThreadsAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_date')



class MessagesAdmin(admin.ModelAdmin):
    list_display = ('message_thread', 'message', 'sent_date','sent_time','opened')





admin.site.register(User, UserAdmin)
admin.site.register(UserLog, UserLogAdmin)
admin.site.register(MessageThreads, MessageThreadsAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Messages, MessagesAdmin)


