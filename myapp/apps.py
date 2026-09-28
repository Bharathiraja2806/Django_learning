from django.apps import AppConfig
from django.db.models.signals import post_migrate

class MyappConfig(AppConfig):
    name = 'myapp'
    def ready(self):
        
        from myapp.signals import create_auth_group
        post_migrate.connect(create_auth_group)
