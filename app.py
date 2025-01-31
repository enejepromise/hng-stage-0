'''
This a simple Flask API.
it returns the following data in JSON format
email, current datetime, and github url of the project codebase
It will also handle CORS which is a security feature 
that the browser use to prevent web pages from making different domain 
request than the one serving it.
'''

from flask import Flask, jsonify, redirect
from datetime import datetime
from flask_cors import CORS
from os import environ

'''initiazing flask'''
app = Flask(__name__)
'''handles Cross Origin Resouce Sharing'''
CORS(app) 

'''
This helps to disable flask from arranging the data alphabetically
but arranging it in the order we have created it
'''
app.json.sort_keys = False

#declaring variables
email = "enejepromise@gmail.com"
github_url = "https://github.com/enejepromise/hng-stage-0"


@app.route('/')
def index():
    '''
    Endpoint to retrieve basic information 

    Returns:
        JSON: A dictionary containing email, current_datetime and github

    '''
    data = {
        "email": email,
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        
        "github_url": github_url

    }
    return jsonify(data), 200
#Error handling
@app.errorhandler(404)
def page_not_found(e):
    '''
    Redirects to homepage
    when user tries to access an undefined route
    '''
    return redirect('/')

if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))  # Default to 5000 if not provided
    app.run(host="0.0.0.0", port=port) 
