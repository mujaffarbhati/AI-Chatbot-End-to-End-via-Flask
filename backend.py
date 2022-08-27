from time import sleep
from flask import Flask, render_template, request
from flask import session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename
import math
with open("config.json","r") as c:
    params=json.load(c)["params"]

app = Flask(__name__)
app.secret_key="super-secret-key"
app.config['UPLOAD_FOLDER'] = params['upload_location']

local_server=True
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
     app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)


class Contact(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Post(db.Model):
    '''
    sno,title,slug,content,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(35), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(12), nullable=True)

#this is for index page
@app.route("/")
def home():

    return render_template('index.html', params=params)

#for signup page aka dashboard
#inorder to get values from the html file adde the name thing in the form section so that value can be retrieved
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    #this is to check if the user is already pre loggined in the website
    if "user" in session and session['user']==params['admin_user']:
        posts = Post.query.all() #for fetching all the posts
        return render_template("dashboard.html", params=params, posts=posts)

    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if username==params['admin_user'] and userpass==params['admin_password']:
            # set the session variable
            session['user']=username
            posts = Post.query.all()
            return render_template("dashboard.html", params=params, posts=posts)
    else:
        return render_template("login.html", params=params)



#this is for having a logout out of the site
@app.route("/delete/<string:sno>" , methods=['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user']==params['admin_user']:
        post = Post.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")

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