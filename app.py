import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify

#import api_yelp
#import parse
import database
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/test')
def starting():
    return render_template('test.html')
@app.route('/api/search')
def search():
    return render_template('form.html')
@app.route('/db')
def starter():
    return database.get_db()
