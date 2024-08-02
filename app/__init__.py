from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {  # Apply CORS only to /api routes
        "origins": ["http://localhost:3000"],  # Allow only this origin
        "methods": ["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
        "allow_headers": ["Content-Type"],  # Allow specific headers
    }
})

from app import routes
