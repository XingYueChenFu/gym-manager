from flask import Blueprint

base = Blueprint('base', __name__) # url_prefix='/'
staff_bp = Blueprint('staff', __name__, url_prefix='/staff')
super_bp = Blueprint('super', __name__, url_prefix='/superuser')
from ..routes import *
