# -*- coding: utf-8 -*-
from flask import render_template,request,session
from app import app

@app.route('/')  
def index():
    loginbean = None
    if 'loginbean' in session:
    	loginbean = session['loginbean']
    # return "Hello World" 
    return render_template('index.html',loginbean=loginbean)