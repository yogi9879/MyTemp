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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
from sklearn.cross_validation import cross_val_score

#from flask import render_template
#from FlaskWeb import app

app = Flask(__name__)

 
@app.route("/")
def index():
    return render_template('upload1.html')
 
@app.route("/hello",methods=['POST','GET'])
def hello():
 if request.method == 'POST':
    #X=request.form
    f = request.files['file']
    return "file uploaded"               #render_template('index.html',name=X)
 

 

 
 
 
if __name__ == "__main__":
    app.run()
