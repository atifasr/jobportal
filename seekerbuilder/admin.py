from django.contrib import admin

from .models import SeekerProfile, ExperienceDetail, EducationDetail, Seekerskillset

# Register your models here.


class EducationDetailAdmin(admin.ModelAdmin):
    list_display = ('profile', 'certificate_degree_name', 'major',
                    'institute_university_name', 'starting_date', 'completion_date')


class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name',
                    'current_salary', 'currency', 'photo', 'resume')


class SeekerskillsetAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'skill_level')


admin.site.register(SeekerProfile, SeekerProfileAdmin)
admin.site.register(ExperienceDetail)
admin.site.register(EducationDetail, EducationDetailAdmin)
admin.site.register(Seekerskillset, SeekerskillsetAdmin)
