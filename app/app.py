#!/bin/python

from flask import Flask, jsonify
import os, json


app = Flask(__name__)

@app.route("/")
def hello():
    
    var = os.uname()

    return jsonify({
        "status": 200,
        "body": f"{var}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",
    debug=True)
