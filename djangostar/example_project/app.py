from apistar import App
from project.routes import routes

settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'project',
            'HOST': 'localhost',
            'USER': 'sam',
            'PASSWORD': 'password'
        }
    },
    'INSTALLED_APPS': ('project',)
}


app = App(routes=routes, settings=settings)
