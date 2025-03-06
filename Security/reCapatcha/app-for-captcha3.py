from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import logging
import json
import dotenv 
import os 

dotenv.load_dotenv()


app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/verify-recaptcha', methods=['POST'])
def verify_recaptcha():
    # Get token from request body
    data = request.get_json()
    token = data.get('token')
    
    if not token:
        logger.error("No token provided")
        return jsonify({"error": "No token provided"}), 400
    
    # Your reCAPTCHA secret key
    secret_key = os.getenv('RECAPTCHA_v3_SECRET_KEY')
    print(secret_key)
    
    try:
        # Verify with Google using requests
        verify_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', 
            data={
                'secret': secret_key,
                'response': token
            }
        )
        
        # Log full response details
        logger.debug(f"Response Status: {verify_response.status_code}")
        logger.debug(f"Response Headers: {verify_response.headers}")
        logger.debug(f"Response Text: {verify_response.text}")
        
        # Attempt to parse JSON
        try:
            result = verify_response.json()
            logger.debug(f"Parsed JSON Result: {json.dumps(result, indent=2)}")
        except ValueError as json_error:
            logger.error(f"JSON Parsing Error: {json_error}")
            logger.error(f"Raw Response: {verify_response.text}")
            return jsonify({"error": "Invalid JSON response", "raw_response": verify_response.text}), 500
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f"Verification error: {str(e)}")
        return jsonify({"error": "Verification failed", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)