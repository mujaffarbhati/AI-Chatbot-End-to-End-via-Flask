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


# class Contact(db.Model):
#     '''
#     sno, name phone_num, msg, date, email
#     '''
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)
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
        pass
    else:
        return render_template("login.html", params=params)



# #this is for having a logout out of the site
# @app.route("/delete/<string:sno>" , methods=['GET', 'POST'])
# def delete(sno):
#     if "user" in session and session['user']==params['admin_user']:
#         post = Post.query.filter_by(sno=sno).first()
#         db.session.delete(post)
#         db.session.commit()
#     return redirect("/dashboard")

#this is for deleteing the post 
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')



# #this is for about button on navibar
@app.route("/about")
def about():
    return render_template('about.html',params=params)

# #this is a code to run out a particular post as a slug
# @app.route("/post/<string:post_slug>",methods = ['GET'])
# def post_route(post_slug):
#     post=Post.query.filter_by(slug=post_slug).first()
#     return render_template('post.html',params=params,post=post)

# #This is for uploading files in the page
# @app.route("/uploader", methods=["GET","POST"])
# def uploader():
#     if ("user" in session and session['user']==params['admin_user']):
#         if request.method=="POST":
#             f = request.files['file1']
#             f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
#             return "Uploaded successfully!"
        

 #this is used for adding and updating of posts from the edit.html shit   
# @app.route("/edit/<string:sno>" , methods=['GET', 'POST'])
# def edit(sno):
#     if ("user" in session and session['user']==params['admin_user']):
#         if request.method=="POST":
#             box_title = request.form.get('title')
#             tline = request.form.get('tline')
#             slug = request.form.get('slug')
#             content = request.form.get('content')
#             date = datetime.now()
#             if sno=='0': #adding new post
#                 post = Post(title=box_title, slug=slug, content=content, tagline=tline, date=date)
#                 db.session.add(post)
#                 db.session.commit()
#             else: #editing a previously made post
#                 post = Post.query.filter_by(sno=sno).first()
#                 post.title = box_title
#                 post.tagline = tline
#                 post.slug = slug
#                 post.content = content
#                 post.date = date
#                 db.session.commit()
#                 return redirect('/edit/'+sno)
#         post = Post.query.filter_by(sno=sno).first()
#         return render_template('edit.html', params=params, post=post,sno=sno)

# #this is for sending values of contact field in the databse
# @app.route("/contact", methods = ['GET', 'POST'])
# def contact():
#     if(request.method=='POST'):
#         '''Add entry to the database'''
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         entry = Contact(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
#         db.session.add(entry)
#         db.session.commit()
#     return render_template('contact.html',params=params)


app.run(debug=True)