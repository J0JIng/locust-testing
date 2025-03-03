from flask import Flask
from api import api


app = Flask(__name__)
api.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080 , debug=True)