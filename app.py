import flask
import os
import json
from flask import request, jsonify
from datetime import datetime
from query import get_best_tle, get_ais, hits_and_misses, cheat, hits_and_misses_smarter, get_hits_and_misses, get_hits_and_misses_given_ais, get_hits_and_misses_smarter, get_hits_and_misses_mp, split, get_hits_and_misses_mp_alt, get_hits_and_misses_smarter_mp, get_sat_positions
from convert import getLonLatHits, getLonLatMisses
from create_czml import getCZML


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/', methods=['GET'])
def home():
    return "This API is running."

    return response




app.run(host='0.0.0.0')
