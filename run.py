from flask import Flask, request, jsonify
from flask_cors import CORS
from app.model import get_response

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    @app.route('/api/chat', methods=['POST'])
    def chat():
        try:
            user_input = request.json.get('input')
            if not user_input:
                return jsonify({'error': 'No input provided'}), 400
            
            response = get_response(user_input)
            return jsonify({'response': response})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': 'Internal server error'}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
