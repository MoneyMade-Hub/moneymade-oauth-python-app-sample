import os

from dotenv import load_dotenv
from flask import Flask, request, send_from_directory

from moneymade_connect_python_sdk import moneymade_connect
  
load_dotenv()

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

moneymadeConnect = moneymade_connect.MoneyMadeConnect(private_key=PRIVATE_KEY,
                                                      public_key=PUBLIC_KEY,
                                                      env='development',
                                                      version='v2'
                                                    )

app = Flask(__name__)

@app.route('/moneymade/oauth', methods=['GET'])
def oauth():
  return send_from_directory('frontend', 'index.html')

@app.route('/moneymade/oauth', methods=['POST'])
def handle_oauth():
  oauth_signature = request.args.get('signature')
  payload = request.args.get('payload')
  
  if (oauth_signature is None):
    return { "error": 'Query sting parameter signature is required' }, 400
  
  if (payload is None):
    return { "error": 'Query sting parameter payload is required' }, 400
  
  decoded_payload = moneymadeConnect.base64_to_dict(payload)
  user_id = decoded_payload['userId']
  
  if oauth_signature != moneymadeConnect.generate_signature(decoded_payload):
    return { "error": "Oauth signature is not valid or expired" }, 400
  
  """
    Next step is handling user linking and finishing of oauth request.
    Depends on chosen data interchange strategy, you should do following:

    1. Authorize user on your side (check which user is sharing internal data)
    
    2.
      - For pulling strategy: generate access token which 
          allows moneymade backend to pull data for authorized user 
      - For pushing stategy:
          NOTE: pushing strategy requires to push data by cron for all user_id you stored
          a) store user_id variable to database and link it to your user's internal id
            (it should be used to push data to linked user by cron)
          b) collect current user accounts data according to your payload sample 
            into accounts variable
          
    3. Finish oauth request
      https://docs.moneymade.io/docs/interaction/connect-flow#oauth-page
  """
  
  # typically it's loaded from database or somewhere else for authorized user
  # dict keys are set by moneymade.io devs team according to your payload sample
  # so this dict is agnostic, fell free to use siutable data types 
  
  oauth_payload = {
    "userId": "2a7708cf-cdd7-463e-92f3-1cc07dc7074c",
    "accounts": [
        {"id": 2, "name": "Repaid", "amount": 1000.0},
    ]
  }
  
  try:
    moneymadeConnect.finish_oauth_request(oauth_signature, oauth_payload)
  except Exception as e:
    error = str(e)
    
    if error == 'Oauth signature is not valid or expired':
      return { "error": error }, 400

    return { "error": 'Internal Server Error' }, 500
  
  redirect_url = moneymadeConnect.get_finish_oauth_redirect_url(oauth_signature)
  
  return { "status": 'OK', "redirect_url": redirect_url }, 200