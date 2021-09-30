import flask
import os
import json
from flask import request, jsonify
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/', methods=['GET'])
def home():
    return "This API is running."

    return response




app.run(host='0.0.0.0')
