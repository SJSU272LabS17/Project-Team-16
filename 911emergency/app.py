from flask import Flask, render_template, request, make_response, url_for, flash, redirect, session, abort, jsonify,g
import json
from jsonschema import validate, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from functions import *
import  myexception

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

@app.route('/sign_up', methods = ['POST'])
def new_user():
    username = request.authorization.username
    password = request.authorization.password
    if username == '' or password == '':
        raise myexception.Unauthorized("Please enter username and password", 401)  # missing arguments
    elif User.query.filter_by(username = username).first() is not None:
        raise myexception.UserExists("User Already exists", 402)  # existing user
    else:
        user = User(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        raise myexception.AccessGranted("New user added and Logged in", 200)

@app.errorhandler(myexception.MyExceptions)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/login', methods=['POST'])
def authenticate():
    # if session['logged_in'] == False:
    username = request.authorization.username
    password = request.authorization.password
    if username is None or password is None:
        raise myexception.Unauthorized("Please enter username and password", 401)
        # abort(400)  # missing arguments
    elif User.query.filter_by(username=username).first() is not None:
        verify_password(username,password)

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        raise myexception.Unauthorized("Invalid username or password", 401)
    g.user = user
    session['logged_in'] = True
    raise myexception.Unauthorized("Access Granted and logged in", 200)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    return (200)

#home route
@app.route('/')
def index():
   return render_template('index.html')

#emergency type api
@app.route('/category', methods=['GET', 'POST'])
def type():
    result = category()
    return jsonify(result)

#emergency trend drop-down values api
@app.route('/sub_category', methods=['GET', 'POST'])
def trend_sub_dropdown():
    if not request.json or not 'emergency_type' in request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    result = sub_category(year,emergency_type)
    return jsonify(result)

schema = {
    "type" : "object",
    "properties" : {
    "year" : {"type" : "string"}
    },
}
#emergency overview api
@app.route('/emergency', methods=['GET', 'POST'])
# @auth.login_required
def emergency():
    input = request.json
    try:
        validate(input, schema)
        year = request.json['year']
        result = emergency_overview(year)
        return jsonify(result)
    except ValidationError as e:
        raise myexception.CheckPostData("year is integer, accepting string", 1)

#trend api
@app.route('/emergency_trend', methods=['GET', 'POST'])
# @auth.login_required
def trend():
    if not request.json:
        raise myexception.ImproperRequest ("Improper Clent request", )
    elif not 'year' in request.json:
        raise myexception.CheckPostData ("Year missing/Year not a string", 1)
    elif not 'emergency_type' in request.json:
        raise myexception.CheckPostData("Emergency type missing/Emergency type not a string", 2)
    elif not 'sub_emergency_type' in request.json:
        raise myexception.CheckPostData("Sub emergency type missing/Sub emergency type not a string", 3)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type = request.json['sub_emergency_type']
    result = emergency_trend(year, emergency_type, sub_emergency_type)
    return jsonify(result)

#comparison api
@app.route('/trend_comparison', methods=['GET', 'POST'])
def trend_comparison():
    if not request.json:
        raise myexception.ImproperRequest ("Improper Clent request", 403)
    elif not 'year' in request.json:
        raise myexception.CheckPostData ("Year missing/Year not a string", 403)
    elif not 'emergency_type' in request.json:
        raise myexception.CheckPostData("Emergency type missing/Emergency type not a string", 403)
    elif not 'sub_emergency_type1' in request.json:
        raise myexception.CheckPostData("Sub emergency type1 missing/Sub emergency type1 not a string", 403)
    elif not 'sub_emergency_type2' in request.json:
        raise myexception.CheckPostData("Sub emergency type2 missing/Sub emergency type2 not a string", 403)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type1 = request.json['sub_emergency_type1']
    sub_emergency_type2 = request.json['sub_emergency_type2']
    result = emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2)
    return jsonify(result)

#heat map api
@app.route('/heat_map', methods=['GET', 'POST'])
def heat_map_generator():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = heat_map(year)
    return jsonify(result)

#google_map api
@app.route('/google', methods=['GET', 'POST'])
def google():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = google_map(year)
    return jsonify(result)

#median income api
@app.route('/income', methods=['GET'])
def income():
    result = income_trend()
    return jsonify(result)

#home value api
@app.route('/h_value', methods=['GET'])
def h_value():
    result = home_value()
    return jsonify(result)

#small business api
@app.route('/small_b', methods=['GET'])
def small_b():
    result = small_business()
    return jsonify(result)

#emergency expenditure api
@app.route('/expenditure', methods=['GET'])
def expenditure():
    result = emergency_expenditure()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', threaded=True, port=80)

# host='0.0.0.0',
