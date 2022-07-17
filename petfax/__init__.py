from flask import Flask

# app factory


def create_app():
    app = Flask(__name__)
# index route

    @app.route('/')
    def index():
        return 'Hello, Petfax!'
# import pet file and register it with app
    from . import pet
    app.register_blueprint(pet.bp)
# register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app
