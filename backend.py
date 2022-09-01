from time import sleep
from flask import Flask, render_template, request
from flask import session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename
import math
import main
with open("config.json","r") as c:
    params=json.load(c)["params"]

#this will read the data file and will save it as text
with open ("text.txt","r") as f:
    text=f.read()
# s=main.question_answer(a,text)
# print(s)

#this is just an extention since we were getting 1 input from the form in the files
def chatbot_response(usertext):
    s=main.question_answer(usertext,text)
    return s.capitalize()

app = Flask(__name__)
app.secret_key="super-secret-key"
app.config['UPLOAD_FOLDER'] = params['upload_location']

local_server=True
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
     app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)

#this is for index page
@app.route("/")
def home():
    return render_template('index.html', params=params)

#this is the flask for textchat aka chatbot 
@app.route("/textchat")
def textchat():
    return render_template('textchat.html', params=params)
#this is for getting the inputs from the chatbot and running the same through the model
@app.route("/textchat/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


#for signup page aka dashboard
#this is the route for the dashboard page for editing and customizing the data
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if request.method=="POST":
            if "content" in request.form:
                with open("text.txt","w")as f:
                    f.write(request.form["content"])
            else:
                username = request.form.get("uname")
                userpass = request.form.get("pass")
                if username==params['admin_user'] and userpass==params['admin_password']:
                    # set the session variable
                    session['user']=username
                    with open("text.txt","r") as f:
                        data=f.read()
                        params["dataset"]=data
                    return render_template("dashboard.html", params=params)
            # data = request.form.get();
    if "user" in session and session['user']==params['admin_user']:
        with open("text.txt","r") as f:
            data=f.read()
            params["dataset"]=data
        return render_template("dashboard.html", params=params)
    else:
        return render_template("login.html", params=params)


#this is for voicechat
@app.route("/voicechat")
def voice():
    return render_template("voicechat.html", params=params)
@app.route("/voicechat/get")
def get_bot_response2():
    userText = request.args.get('msg')
    return chatbot_response(userText)



#this is for logging out of the signin page 
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')



#this is for about button on navibar just for info purpose
@app.route("/about")
def about():
    return render_template('about.html',params=params)

app.run(debug=True)