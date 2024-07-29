from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register routes using a blueprint within the application context
    with app.app_context():
        from .routes import app as routes_blueprint
        app.register_blueprint(routes_blueprint)

    return app


