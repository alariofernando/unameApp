#!/bin/python

from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def hello():
    
    var = os.uname()

    return var

if __name__ == "__main__":
    app.run(debug=True)