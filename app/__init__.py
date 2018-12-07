import logging
import dash

# Initializing logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(filename)s:%(lineno)s | %(funcName)s() | %(asctime)s | %(levelname)s] %(message)s')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from app.main_templates import *
from app.template_controller import *
