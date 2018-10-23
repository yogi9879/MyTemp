#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:02:30 2018

@author: yogesh
"""

from flask import Flask, render_template #, request,make_response
#from datetime import datetime
#from flask import render_template
#from FlaskWeb import app

pp = Flask(__name__)

 
@app.route("/")
def index():
    return render_template('upload.html')
 
#@app.route("https://lib12.azurewebsites.net/hello%20method%20=?nm=yogesh",methods = ['POST', 'GET'])
#def hello():
 #   return "Hello World!"
 
 
if __name__ == "__main__":
    app.run()
