from asyncore import file_dispatcher
from random import random
from flask import make_response, jsonify, request
import os

#get name domain of a file, input is a name, output is the name of the domain
def get_name(dir):

    if ("\\" in dir):
        tokens = dir.split("\\")
    elif ("/" in dir):
        tokens = dir.split("/")

    return tokens[-1].split(".")[0]

# Get file request from client
# input:
# - request input: input from flask request
# - parameter_name: name of parameter

def get_file_request(
    request_input, parameter_name
    ):

    try:
        file = request.files[parameter_name]
        file.save(file.filename)
        return file.filename
    except:
        raise Exception("Parameter Invalid")

## Delete file function
# Delete file by filename
# Input: filename    

def delete_file(filename):

    if not os.path.isdir(filename):
        raise Exception("No file found")
    else:
        os.remove(filename)
        print("remove file success")

# Get string request output
# input:
# - request input: input from flask request
# - parameter_name: name of parameter

def get_string_request(
    request_input, parameter_name
    ):

    try:
        out = request.form[parameter_name]
        return out
    except:
        raise Exception("Parameter Invalid")