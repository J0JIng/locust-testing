# https://flask-restx.readthedocs.io/en/latest/parsing.html
from flask_restx.reqparse import RequestParser

header_parser = RequestParser()
header_parser.add_argument('Auth', 
                           type=str, 
                           required=True,
                           location='headers',
                           help='Auth is required')

