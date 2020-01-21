#!/bin/python

from flask import Flask
import os, json


app = Flask(__name__)

@app.route("/")
def hello():
    
    var = os.uname()

    uname = {
        "OS": var[0],
        "Hostname": var[1],
        "Kernel Version": var[2],
        "Kernel and Build Time": var[3],
        "Arch": var[4]
    }

    return {
        "status": 200,
        "body": var
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0",
    debug=True)