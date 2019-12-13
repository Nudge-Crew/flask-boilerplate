from app import app
from . import config


@app.route('/')
@app.route('/index')
def index():
    return str(config.PORT)
