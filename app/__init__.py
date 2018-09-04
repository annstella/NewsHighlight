from flask import Flask
from .config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name)
# app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap.init_app(app)


return app