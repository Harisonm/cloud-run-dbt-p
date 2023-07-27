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

def call_dbt_run_with_args(select_args, target=None, profiles_dir=None):
    try:
        cmd = ["dbt", "run", "--select", select_args]

        if target:
            cmd.extend(["--target", target])
        if profiles_dir:
            cmd.extend(["--profiles-dir", profiles_dir])

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

@app.route('/run_dbt', methods=['POST'])
def run_dbt():
    data = request.get_json()
    select_args = data.get('select_args')
    target = data.get('target')
    profiles_dir = data.get('profiles_dir')

    if not select_args:
        return jsonify({'error': 'Select arguments not provided'}), 400

    try:
        output = call_dbt_run_with_args(select_args, target, profiles_dir)
        return jsonify({'result': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/")
def welcome_to_dbt_platform():
    return f"Welcome to the dbt plateform on Cloud run"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
