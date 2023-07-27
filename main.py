import os
import sys
from google.cloud import logging
import subprocess
from flask import Flask, request, jsonify
# Instantiates a client
client = logging.Client()
    
app = Flask(__name__)

def run_dbt_deps():
    try:
        cmd = ["dbt", "deps", "--profiles-dir", "profiles/big_query"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None
    
@app.route('/run_dbt_deps', methods=['GET'])
def run_dbt_docs_generate_api():
    try:
        output = run_dbt_deps()
        return jsonify({'result': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
