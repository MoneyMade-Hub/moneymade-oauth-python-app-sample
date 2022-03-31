import os

from dotenv import load_dotenv
from flask import Flask, request, send_from_directory

from moneymade_connect_python_sdk import moneymade_connect
  
load_dotenv()

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

moneymadeConnect = moneymade_connect.MoneyMadeConnect(private_key=PRIVATE_KEY,
                                                      public_key=PUBLIC_KEY,
                                                      env='development'
                                                    )

app = Flask(__name__)

@app.route('/moneymade/oauth', methods=['GET'])
def oauth():
  return send_from_directory('frontend', 'index.html')

@app.route('/moneymade/oauth', methods=['POST'])
def handle_oauth():
  signature = request.args.get('signature')
  payload = request.args.get('payload')
  
  if (signature is None):
    return { "error": 'Query sting parameter signature is required' }, 400
  
  if (payload is None):
    return { "error": 'Query sting parameter payload is required' }, 400
  
  return { "page": "index" }, 200