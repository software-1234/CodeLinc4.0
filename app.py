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
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

#import api_yelp
#import parse
import database
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('home.html')

@app.route('/api/search')
def search():
    return render_template('form.html')

@app.route('/organization')
def searching():
    return render_template('organizations.html')

@app.route('/api/locations')
def get():
    response =  database.get_valid_locations()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/sms', methods=['POST'])
def text():
    response = MessagingResponse()
    replyText = message_maker.getReply(request.form['Body'], request.form['From'])
    response.message(replyText)
    return str(response)

@app.route('/api/test')
def test_distance():
    replyText = message_maker.getReply("food pantry near home", 19195251997)
    return replyText
