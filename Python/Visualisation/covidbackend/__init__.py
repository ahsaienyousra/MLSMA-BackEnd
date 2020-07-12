from flask import Flask
from .extensions import mongo
from .main import main
def create_app(config_object='covidbackend.settings'):
    app = Flask(__name__)
    from flask_cors import CORS
    CORS(app)

    app.config.from_object(config_object)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app