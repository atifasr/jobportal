from django.contrib import admin

from .models import *

# Register your models here.


class JobPostAdmin(admin.ModelAdmin):
    list_display = ('creater', 'title', 'job_type', 'job_loc',
                    'cmpny_name', 'created_date', 'salary')


class JobPostActivityAdmin(admin.ModelAdmin):
    list_display = ('job_post', 'user', 'apply_date','status')


class SkillsetAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)


class Job_SkillsetAdmin(admin.ModelAdmin):
    list_display = ('skill', 'job_post', 'skill_level')


admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobPostActivity, JobPostActivityAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Job_Skillset, Job_SkillsetAdmin)
