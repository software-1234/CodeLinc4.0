import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify

from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib
import distance
import message_maker
# Your Account SID from twilio.com/console
account_sid = "AC08eb1bfb20fe3819d6fc89edd0519f6d"
# Your Auth Token from twilio.com/console
auth_token  = "8845298236d986236f8ea3ed68f4a1ba"

client = Client(account_sid, auth_token)

#import api_yelp
#import parse
import database
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


@app.route('/api/locations')
def get():
    response =  database.get_valid_locations()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/sms', methods=['POST'])
def text():
    response = MessagingResponse()
    replyText = message_maker.getReply(request.form['Body'])
    response.message(replyText)
    print('hi')
    return str(response)
@app.route('/lat')
def lat():
    response = distance.getDistance()
    return 'hi'
