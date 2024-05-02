from flask import Flask, request, jsonify
from src.model import get_model


app = Flask(__name__)

model = get_model()


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'features' not in data:
            return jsonify({'error': 'Missing features'}), 400
        predictions = model.predict([data['features']])
        return jsonify({'prediction': int(predictions[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
