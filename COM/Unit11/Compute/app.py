from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("image_model.h5")
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    image = np.array(request.json['image']) / 255.0
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image)
    return jsonify({'class': int(np.argmax(prediction))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

