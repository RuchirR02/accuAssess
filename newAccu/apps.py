from django.apps import AppConfig

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import models 


class NewaccuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newAccu'
