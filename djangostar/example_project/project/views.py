from djangostar.backends import DjangoBackend

from project.models import Star


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def create_star(django: DjangoBackend):
    pass


def list_stars(django: DjangoBackend):
    return {'stars': list(Star.objects.values())}

