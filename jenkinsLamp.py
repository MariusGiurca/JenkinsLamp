#!/usr/bin/python

from flask import Flask, request, render_template 
from flask_api import FlaskAPI

status='green'

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
    print("TV - get")
    return {
           "led_url": request.url + "led/(green | red)/",
      		 "led_url_POST": {"state": "(0 | 1)"}
    			 }
  
@app.route('/led/<color>/', methods=["GET", "POST"])
def api_leds_control(color):
    print("TV- post")
    if request.method == "POST":
            status = color     
    return color

@app.route('/hello')
def hello():
    print('hello', status)
    return render_template('hello.html',statusHtml = status)

if __name__ == "__main__":
    app.run()
