from flask import Flask, jsonify, request
from mnist import predict_single_image
import logging

app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG)


@app.route('/predict/', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("loaded trained model")
        predicted_class = predict_single_image(None,"./Flask_Heroku_Introduction/Mnist_model/mnist_model.pt")
        return jsonify({'Prediction': predicted_class})

if __name__ == '__main__':
   app.run()