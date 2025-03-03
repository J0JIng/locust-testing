from flask import Flask, Blueprint
from api import api  # Assuming api is a Flask-RESTX Api instance

class Webapp:
    def __init__(self, host="0.0.0.0", port=8080, debug=True):
        self.app = Flask(__name__)  # Define Flask app inside the class
        self.host = host
        self.port = port
        self.debug = debug
        self.init_app()  # Call method to initialize Blueprints

    def init_app(self):
        """Initialize API with Blueprint if not already registered"""
        if len(self.app.blueprints) > 0:
            return  # Avoid re-registering Blueprints

        # blueprint = Blueprint("api", __name__)  # Define a Blueprint
        # api.init_app(blueprint)  # Attach Flask-RESTX API to the Blueprint
        # self.app.register_blueprint(blueprint, url_prefix="/api")  # Register Blueprint

    def run(self):
        """Run the Flask application"""
        api.init_app(self.app)
        self.app.run(host=self.host, port=self.port, debug=self.debug)


if __name__ == "__main__":
    web_app = Webapp()  # Create an instance of Webapp
    web_app.run()  # Start the server
