from flask import Flask, Blueprint, request, jsonify
import logging
from app.model import get_response  # Path import yang benar

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('input', '')  # Menggunakan 'input' sesuai dengan frontend
        logging.debug(f"Received input: {user_input}")
        response = get_response(user_input)
        logging.debug(f"Chatbot response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

# Register the blueprint in the main app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
