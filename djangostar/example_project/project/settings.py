from apistar import environment, schema

class Env(environment.Environment):
    pass

env = Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project',
        'HOST': 'localhost'

    }
}

INSTALLED_APPS = [
    'project'
]

SECRET_KEY = env['SECRET_KEY']