"""
Routes and views for the flask application.
"""

from datetime import datetime
import sys
from flask import render_template
from flask import *
from FlaskWebshop import app
import json
from pprint import pprint
import mysql.connector


app.debug = True


#for (id, name, price, site, description) in executor:
#  print(id, name, price, site, description)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'a.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route("/login",methods=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route("/request.json")
def renderdata():
    try:
      db = mysql.connector.connect(user='root', password='wessel',host='127.0.0.1',database='projfive')
      print("Connection made")
    except:
      print("no connection")
    print('Hello world!')



    query = "SELECT * FROM products"
    executor = db.cursor()
    executor.execute(query)
    collectionString = "jsondata=[{\n"
    isfirst = True
    for (id, name, price, site, description) in executor:
      if isfirst:
        isfirst = False
      else:
        collectionString += ",{\n"
      print(name)
      collectionString += ("\t\"id\":\"" + str(id) + "\",\n" +
				"\t\"name\":\"" + str(name) + "\",\n" +
				"\t\"price\":\"" + str(price) + "\",\n" +
				"\t\"site\":\"" + str(site) + "\",\n" +
				"\t\"description\":\"" + str(description) + "\"\n}")

    collectionString += "]"
    db.close()
    return collectionString