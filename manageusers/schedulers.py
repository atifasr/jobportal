 


from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from .helpers import push_data
 
jobstores = {
            'default': DjangoJobStore()
        }
executors = {
    'default': ThreadPoolExecutor(5),
    'processpool': ProcessPoolExecutor(5)
    }
job_defaults = {
    'coalesce': False,
    'max_instances': 3
    }
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors,job_defaults=job_defaults,timezone='utc')

scheduler.add_job(push_data, 'interval', hours = 2,replace_existing=True,id='this_job')