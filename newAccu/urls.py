from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("qfirst",views.create_model, name="qfirst"),
    path("qsecond", views.test_signal, name="qsecond"),
    path("qthird",views.test_signal_transaction, name="qthird")
]