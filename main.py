from flask import Flask, request, send_from_directory

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