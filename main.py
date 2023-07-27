import os
import sys
from google.cloud import logging
import subprocess
from flask import Flask
# Instantiates a client
client = logging.Client()
    
app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/dbt")
def launch_dbt():
    process = subprocess.run(["python3","-m","dbt","docs","generate"],stdout=subprocess.PIPE,text=True)
    process
    return process.stdout

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
