import time
from celery import Celery


celery_app = Celery(name='worker', broker="redis://redis:6379/0")


@celery_app.task
def countWords(text):

    num_words = len(list(text.split()))
    time.sleep(num_words)
    return num_words
