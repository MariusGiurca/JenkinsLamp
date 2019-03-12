#!/usr/bin/python

from flask import Flask, request, render_template
from flask_api import FlaskAPI
from Naked.toolshed.shell import execute_js

import json
import sys
import urllib
import urllib2

status='green'

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
    print("TV - get")
    return {
           "led_url": request.url + "led/(green | red)/",
      		 "led_url_POST": {"state": "(0 | 1)"}
    			 }

@app.route('/<team>', methods=["GET"])
def hello(team):
    # print('hello', color)

    jenkinsUrl = "http://jenkinsURL.net/view/xxxx/job/jobName/lastBuild/api/json"

    try:
        jenkinsStream   = urllib2.urlopen( jenkinsUrl )
    except urllib2.HTTPError, e:
        print "URL Error: " + str(e.code)
        print "      (job name wrong)"
        sys.exit(2)

    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)

    if str(buildStatusJson["building"]) is 'True':
        color = "blue"
        print "BUILDING"

    elif buildStatusJson.has_key( "result" ):
        print buildStatusJson["result"]
        color = "green"
        if buildStatusJson["result"] != "SUCCESS" :
            color = "red"

    if team == '3':
        result = execute_js('/home/mihaio/tuyapi/tuyapi-master/app.js ' + color)
        return render_template('hello.html', statusHtml = color)
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()
