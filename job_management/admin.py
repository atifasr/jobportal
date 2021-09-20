from django.contrib import admin

from .models import *

# Register your models here.


class JobPostAdmin(admin.ModelAdmin):
    list_display = ('get_jobposters', 'title',
                    'cmpny_name', 'created_date', 'salary_start','salary_end')


class JobPostActivityAdmin(admin.ModelAdmin):
    list_display = ('job_post', 'user', 'apply_date','status')


class SkillsetAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)


class Job_SkillsetAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'job_post', 'skill_level')

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('job_type',)

class JobLocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state','job')

class SavedJobsAdmin(admin.ModelAdmin):
    list_display = ('user', 'job')



admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobLocation,JobLocationAdmin)
admin.site.register(JobType,JobTypeAdmin)
admin.site.register(JobPostActivity, JobPostActivityAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Job_Skillset, Job_SkillsetAdmin)
admin.site.register(SavedJobs, SavedJobsAdmin)
