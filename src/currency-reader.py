import falcon


class HelloWorldResource(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = '{"hello": "world"}'


app = falcon.API()
hello = HelloWorldResource()
app.add_route('/', hello)
