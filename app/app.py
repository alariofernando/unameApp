#!/bin/python

from flask import Flask
import os, json


app = Flask(__name__)

@app.route("/")
def hello():
    
    var = os.uname()

    return {
        "status": 200,
        "body": var
    }

if __name__ == "__main__":
    app.run(debug=True)