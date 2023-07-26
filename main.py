from bigquery_public_data import app,db
import os
import sys
from google.cloud import logging
import subprocess

# Instantiates a client
client = logging.Client()

with app.app_context():
    db.create_all()

if __name__=='__main__':

    logging.info(sys.argv, len(sys.argv))
    client.setup_logging()
    process = subprocess.run(['dbt', sys.argv], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
    process
    
    app.run(debug=True,host="0.0.0.0",port=int(os.envion.get("PORT",8080)))
    
