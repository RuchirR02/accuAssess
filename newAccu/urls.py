from django.urls import path
from . import views

urlpatterns = [
    path("rrr",views.create_model, name="create_model"),
    path("qsecond", views.test_signal, name="test_signal"),
    path("qthird",views.test_signal_transaction, name="test_signal_transaction")
]