import time
from celery import task

@task
def task1():
    print 'hello'
    time.sleep(5)
    print 'world'