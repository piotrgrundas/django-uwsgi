from django.core.management.base import BaseCommand
from django_uwsgi.uwsgi import UWSGIServer


class Command(BaseCommand):

    def handle(self, *args, **options):
        UWSGIServer().run()
