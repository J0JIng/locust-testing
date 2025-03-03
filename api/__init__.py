"""
Documentation:
- https://flask-restx.readthedocs.io/en/latest/api.html
- https://flask-restx.readthedocs.io/en/latest/scaling.html
"""
from flask_restx import Api


api = Api(
    version="1.0", 
    title="Simple RESTAPI", 
    description="RESTFUL API Project"
    )

from api.v1.entity.user import ns as namespace1 
api.add_namespace(namespace1)




