from flask import Flask, request, render_template
from flask_api import FlaskAPI
from Naked.toolshed.shell import execute_js

status='green'

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
    print("TV - get")
    return {
           "led_url": request.url + "led/(green | red)/",
      		 "led_url_POST": {"state": "(0 | 1)"}
    			 }

@app.route('/<team>/<color>', methods=["GET"])
def hello(team, color):
    print('hello', color)
    if team == '3':
        result = execute_js('/home/mihaio/tuyapi/tuyapi-master/app.js ' + color)
        return render_template('hello.html',statusHtml = color)
    return render_template('hello.html',statusHtml = 'alive')

if __name__ == "__main__":
    app.run()
