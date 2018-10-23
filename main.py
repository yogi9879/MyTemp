#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:02:30 2018

@author: yogesh
"""

from flask import Flask, render_template #, request,make_response
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('upload.html')
 
@app.route("/hello",methods = ['POST', 'GET'])
def hello():
    return "Hello World!"
 
 
if __name__ == "__main__":
    app.run()
