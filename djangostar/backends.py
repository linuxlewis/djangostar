from uuid import uuid4

from apistar.settings import Settings
from django import setup
from django.conf import settings as django_settings
from django.core.management import call_command


class DjangoBackend(object):

    preload = True

    @classmethod
    def build(cls, settings: Settings):
        django_settings.configure(SECRET_KEY=settings.get('SECRET_KEY'),
                                  INSTALLED_APPS=settings.get('INSTALLED_APPS'),
                                  DATABASES=settings.get('DATABASES'))
        setup()
        return cls()

    def create_tables(self):
        call_command('makemigrations')
        call_command('migrate')

    def drop_tables(self):
        pass