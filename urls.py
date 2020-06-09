from api.routes import routes_api

def heartbeat():
    return 'Hello, World!'

def setup_routing(app):
    app.add_url_rule('/routes', 'routes_api', routes_api)
    app.add_url_rule('/', 'heartbeat', heartbeat)
