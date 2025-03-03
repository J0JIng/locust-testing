from api import api
from typing import Any
from flask_restx import Resource, Api , fields , marshal
from werkzeug.exceptions import BadRequest, NotFound
from controllers.parser import header_parser

"""
namespcae module contains models and resources declarations
"""

# Define Namespace
ns = api.namespace('users', 
                   path='/v1/users', 
                   description='User-related operations')

# Define Models
userModel = ns.model('User', {
    'name': fields.String,
    'age': fields.Integer,  
    'married': fields.Boolean
})

# Define Resource - define route in namespace level as oppose to global level
@ns.route('')
@ns.expect(header_parser)
class UserList(Resource):
    def __init__(self, api: Api = None, *args: tuple, **kwargs: dict[str]):
        super().__init__(api)
    
    @ns.response(200, "OK", model = userModel)
    @ns.response(400, "Invalid Response")
    @ns.response(404, "User Not Found")
    # @ns.param()
    @ns.marshal_with(userModel)
    def get(self):
        # Sample logic for fetching user data - Query DB
        user_data = {'name': 'John Doe', 'age': 30, 'married': True}
        
        if not user_data:
            raise NotFound('User Not Found')
        return user_data
