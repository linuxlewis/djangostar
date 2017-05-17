from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, list_stars, create_star

routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes),
    Route('/api/stars/', 'GET', list_stars),
    Route('/api/stars/', 'POST', create_star)
]
