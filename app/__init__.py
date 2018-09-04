from flask import Flask
from config import Config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
    app = Flask(__name__)
    app.config.from_object(Config_options[config_name])
# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# Setting up configuration
    from .request import configure_request
    configure_request(app)

# Initializing Flask Extensions
    bootstrap.init_app(app)


    return app