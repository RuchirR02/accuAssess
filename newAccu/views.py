from django.shortcuts import render
from .models import MyModel
from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth.models import User
import threading

def home(request):
    return render(request, 'index.html')

def create_model(request):
    MyModel.objects.create(name="Test")
    return HttpResponse("Question 1 Done")


def test_signal(request):
    print(f"Main thread: {threading.current_thread().name}")
    user = User.objects.create(username="testuser1")  
    threading.Timer(0.5, lambda: user.delete()).start()
    return HttpResponse("Signal test completed!<br>Question 2 Done")


def test_signal_transaction(request):
    print(f"Main thread: {threading.current_thread().name}")
    
    try:
        with transaction.atomic():  
            user = User.objects.create(username="testuser2")  
            threading.Timer(0.5, lambda: user.delete()).start()
            raise Exception("Rolling back transaction!")  

    except Exception as e:
        print(f"Transaction rolled back: {e}")

    return HttpResponse("Signal transaction test completed!<br>Question 3 Done")
