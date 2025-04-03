from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def mymodel_post_save_handler(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(10) 
    print("Signal handler finished")

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler executed in thread: {threading.current_thread().name}")
    print(f"User {instance.username} saved inside signal handler.")