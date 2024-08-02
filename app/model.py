import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import json
import pickle  # Tambahkan ini

# Load the model
model = tf.keras.models.load_model('export/model.h5')

# Load the TF-IDF Vectorizer
with open('export/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

# Load the label encoder
with open('export/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Load the responses
with open('export/responses.json', 'r') as f:
    responses = json.load(f)

def get_response(user_input):
    processed_input = tfidf_vectorizer.transform([user_input]).toarray()
    prediction = model.predict(processed_input)
    predicted_tag_index = np.argmax(prediction, axis=1)[0]
    predicted_tag = label_encoder.classes_[predicted_tag_index]
    return responses.get(predicted_tag, "Sorry, I don't understand your question.")
