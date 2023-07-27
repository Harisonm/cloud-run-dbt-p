from bigquery_public_data import app,db
import os
import sys
from google.cloud import logging
import subprocess
from flask import Flask
# Instantiates a client
client = logging.Client()

with app.app_context():
    db.create_all()
    
app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
