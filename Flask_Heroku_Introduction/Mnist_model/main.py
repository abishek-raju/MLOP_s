from flask import Flask, jsonify, request,render_template,flash,redirect,url_for,send_from_directory
from mnist import predict_single_image
import logging
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = './upload_folder/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def welcome_and_upload():
    return render_template('welcome_upload.html')


@app.route('/uploader', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_full_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_full_path)
            # return redirect(url_for('download_file', name=filename))
            if os.path.exists("mnist_model.pt"):
                pass
            else:
                import gdown
                url = "https://drive.google.com/uc?id=1gVfFUEO28Lvu6pmRFAKUg7Wpgujwnif2"
                output = 'mnist_model.pt'
                gdown.download(url, output,quiet=False) 

            print("loaded trained model")
            predicted_probs,predicted_class = predict_single_image(file_full_path,"mnist_model.pt",1)
            return jsonify({'Predicted_Probability': predicted_probs.tolist(),
                            'Predicted_Class' : predicted_class.tolist()})
        else:
            return "file format does not match"
    else:
        return "check if File is passed with right format and Method is POST "

@app.route('/downloads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)



if __name__ == '__main__':
   app.run()