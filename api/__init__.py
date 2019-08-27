from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['JSONIFY_MIMETYPE'] = 'application/json'

from api import models, views
