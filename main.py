#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:02:30 2018

@author: yogesh
"""

from flask import Flask, render_template, request, make_response
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
#import flask
#import matplotlib.pyplot as plt
#import numpy 
#from sklearn.svm import SVR
#from sklearn.cross_validation import cross_val_score
#import sub

#from flask import render_template
#from FlaskWeb import app

app = Flask(__name__)

 
@app.route("/")
def index():
    return  "3dddddgg"     #render_template('upload1.html')
 
@app.route("/hello",methods=['POST','GET'])
def hello():
 if request.method == 'POST':
    #X=request.form
    f = request.files['file']
 #   dataset=pd.read_csv(f)
    #results=sub.Model(dataset)
    return "HI"             #render_template('index.html',name=X)
 

 

 
 
 
if __name__ == "__main__":
    app.run()
