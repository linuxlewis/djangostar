from apistar import schema


class Star(schema.Object):

    properties = {
        'name': schema.String(max_length=255)
    }

