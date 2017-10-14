import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify

from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

# Your Account SID from twilio.com/console
account_sid = "AC08eb1bfb20fe3819d6fc89edd0519f6d"
# Your Auth Token from twilio.com/console
auth_token  = "8845298236d986236f8ea3ed68f4a1ba"

client = Client(account_sid, auth_token)

#import api_yelp
#import parse
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/test')
def starting_test():
    return render_template('test.html')

@app.route('/home')
def starting():
    return render_template('home.html')
    
@app.route('/api/search')
def search():
    return render_template('form.html')

