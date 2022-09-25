from fileinput import filename
from flask import Flask,request,redirect, url_for, send_from_directory,Response,jsonify,make_response, render_template
from functools import wraps
from utils.request_utils import get_file_request

secret_key = "abc"

"""
    REQUIRED TOKEN FOR EACH ROUTE ON SERVER
""" 

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        token = request.headers.get('x-access-tokens', None)

        if token is None:
            return make_response(jsonify({
                "status": "fail",
                "err": "a valid token is missing"
            }), 400)

        if token != app.config['SECRET_KEY']:
            return make_response(jsonify({
                "status": "fail",
                "err": "token is invalid"
            }), 400)

        return f(*args, **kwargs)

    return decorator

"""
    INITIALIZE APP
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


# TRY ON ROOT 

@app.route("/",methods = ["GET", "POST"])
@token_required
def sample():

    try: 
        return jsonify({
            "status": "1",
            "content": "hello world"
        })

    except:
        return jsonify({
            "status": "0",
            "content": "something wrong"
        })


#TRY ON REQUEST METHOD

@app.route("/request_file",methods = ["GET","POST"])
@token_required
def sample_request_file():
    
    try:

        if request.method == "GET":
            return jsonify({
                "status":"1",
                "content": "ping success"
            })

        else:
            parameter = ""
            filename = get_file_request(request,parameter)

            return jsonify({
                "status": "1",
                "content": "success request"
            })
    except:

        return jsonify({
            "status": "0",
            "content":"Something wrong"
        })
        

