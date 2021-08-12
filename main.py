from flask import Flask
from flask import render_template
from flask import request
from flask.helpers import make_response

import os
import firebase

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service.json"

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/profile", methods=['POST'])
def render_profile():
    print ("REQUEST: ", request)
    user = {
        'email':  request.form['email'],
        'first_name':  request.form['fname'],
        'last_name': request.form['lname']
    }
    user = firebase.get_user(user)
    print ('firebase body: ', user)
    resp = make_response(render_template('profile.html'))
    resp.set_cookie('id', user['id'])
    resp.set_cookie('email', user['email'])
    resp.set_cookie('firstLast', user['first_name'] + " " + user['last_name'])
    return resp

@app.route("/manifest.json")
def render_manifest():
    return render_template('manifest.json')
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
