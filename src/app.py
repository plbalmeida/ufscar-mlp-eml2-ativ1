import joblib
from flask import Flask, request, jsonify


app = Flask(__name__)

model = joblib.load('iris_model.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        predictions = model.predict([data['features']])
        return jsonify({'prediction': int(predictions[0])})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
