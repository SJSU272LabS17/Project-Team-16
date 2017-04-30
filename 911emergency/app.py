from flask import Flask, render_template, request, make_response, url_for, flash, redirect, session, abort, jsonify
from flask_oauth import OAuth
# from urllib2 import Request, urlopen, URLError
import json
from urllib.request import urlopen, URLError, Request
from functions import *

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
# GOOGLE_CLIENT_ID = '172252254677-2dkr49b0b736blrgbs6a5g5q7drpjqv4.apps.googleusercontent.com'
# GOOGLE_CLIENT_SECRET = 'bZLZjmpcZ_A_AgqtkUZFc7X2'
# REDIRECT_URI = '/authorized'  # one of the Redirect URIs from Google APIs console
#
# SECRET_KEY = 'development key'
# DEBUG = True
#
# app = Flask(__name__)
# app.debug = DEBUG
# app.secret_key = SECRET_KEY
# oauth = OAuth()
#
# google = oauth.remote_app('google',
#                           base_url='https://www.google.com/accounts/',
#                           authorize_url='https://accounts.google.com/o/oauth2/auth',
#                           request_token_url=None,
#                           request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
#                                                 'response_type': 'code'},
#                           access_token_url='https://accounts.google.com/o/oauth2/token',
#                           access_token_method='POST',
#                           access_token_params={'grant_type': 'authorization_code'},
#                           consumer_key=GOOGLE_CLIENT_ID,
#                           consumer_secret=GOOGLE_CLIENT_SECRET)

# @app.route('/')
# def index():
#     access_token = session.get('access_token')
#     if access_token is None:
#         return redirect(url_for('login'))
#
#     access_token = access_token[0]
#     headers = {'Authorization': 'OAuth '+access_token}
#     req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
#                   None, headers)
#     try:
#         res = urlopen(req)
#     except URLError as e:
#         if e.code == 401:
#             # Unauthorized - bad token
#             session.pop('access_token', None)
#             return redirect(url_for('login'))
#         return res.read()
#
#     # return res.read()
#     return render_template('new.html')
#
# @app.route('/login')
# def login():
#     callback = url_for('authorized', _external=True)
#     return google.authorize(callback = callback)
#
# @app.route(REDIRECT_URI)
# @google.authorized_handler
# def authorized(resp):
#     access_token = resp['access_token']
#     session['access_token'] = access_token, ''
#     return redirect(url_for('index'))
#
# @google.tokengetter
# def get_access_token():
#     return session.get('access_token')
#
# def main():
#     app.run()
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('new.html')

# @app.route('/bar')
# def bar():
#    return render_template('bar.html')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = emergency_overview(year)
    return jsonify(result)

@app.route('/emergency_trend', methods=['GET', 'POST'])
def trend():
    if not request.json or not 'year' in request.json or not 'emergency_type' in request.json or not 'sub_emergency_type' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type = request.json['sub_emergency_type']
    result = emergency_trend(year, emergency_type, sub_emergency_type)
    return jsonify(result)

@app.route('/trend_comparison', methods=['GET', 'POST'])
def trend_comparison():
    if not request.json or not 'year' in request.json or not 'emergency_type' in request.json or not 'sub_emergency_type1' in request.json or not 'sub_emergency_type2' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type1 = request.json['sub_emergency_type1']
    sub_emergency_type2 = request.json['sub_emergency_type2']
    result = emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)
