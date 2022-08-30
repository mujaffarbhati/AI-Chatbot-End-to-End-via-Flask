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


with open ("text.txt","r") as f:
    text=f.read()
# s=main.question_answer(a,text)
# print(s)
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

#to be removed 
# class Post(db.Model):
#     '''
#     sno,title,slug,content,date
#     '''
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     tagline = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(35), nullable=False)
#     content = db.Column(db.String(300), nullable=False)
#     date = db.Column(db.String(12), nullable=True)

#this is for index page
@app.route("/")
def home():

    return render_template('index.html', params=params)

@app.route("/textchat")
def textchat():
    return render_template('textchat.html', params=params)
@app.route("/textchat/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


#for signup page aka dashboard
#inorder to get values from the html file adde the name thing in the form section so that value can be retrieved
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if request.method=="POST":
            # if len(request.form["content"])>0:\
            print(type(request.form))
            if "content" in request.form:
                with open("text.txt","w")as f:
                    f.write(request.form["content"])
            else:
                print("INSIDE POST")
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
    return render_template("voicechat.htm", params=params)
@app.route("/voicechat/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)



#this is for deleteing the post 
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')



#this is for about button on navibar
@app.route("/about")
def about():
    return render_template('about.html',params=params)

app.run(debug=True)