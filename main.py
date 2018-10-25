#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:02:30 2018

@author: yogesh
"""

from flask import Flask, render_template,request, make_response
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
#from sklearn.preprocessing import StandardScaler
#from sklearn.svm import SVR
#import matplotlib.pyplot as plt
import sub
#import pandas as pd
#from flask import render_template
#from FlaskWeb import app

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def result():
  
      return render_template("upload1.html")


 
@app.route("/hello")
def index():
    return "gikgig" # render_template('upload1.html')
 
if __name__ == "__main__":
    app.run()
