from flask import Blueprint
routes = Blueprint('routes', __name__)

from os import path

style_dir = path.abspath('../../front/styles')








from .admin import *
from .errors import *

from ._rules import *


