import time

from celery import shared_task


@shared_task
def heavy_task(*args, **kwargs):
    print("-" * 30)
    print(args, kwargs)
    print("-" * 30)
    print("doing stuff ..., sending an email, computing largest prime number ...")
    time.sleep(2)
    return True


@shared_task
def periodic_task():
    print("-" * 30)
    print("running ...")
    time.sleep(2)
    print("-" * 30)
    print("completed")


@shared_task
def periodic_task_with_args(*args, **kwargs):
    print("-" * 30)
    print("running ...", args, kwargs)
    time.sleep(2)
    print("-" * 30)
    print("completed")

