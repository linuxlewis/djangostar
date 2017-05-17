from djangostar.backends import DjangoBackend
from project import schemas


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def create_star(models: DjangoBackend, star: schemas.Star):
    Star = models.Star
    star = Star(**star)
    star.save()
    return {'star': {'name': star.name, 'id': star.id}}


def list_stars(models: DjangoBackend):
    Star = models.Star
    return {'stars': list(Star.objects.values('name', 'id'))}

