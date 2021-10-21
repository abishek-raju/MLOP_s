from flask import Flask, jsonify, request,render_template,flash,redirect,url_for,send_from_directory
# from inference import classify_image
try:
    from .inference import classify_image     # "myapp" case
except:
    from inference import classify_image           # "__main__" case
import logging
from werkzeug.utils import secure_filename
import os
import shutil
from pathlib import Path
import cv2
import ntplib
from time import ctime
current_time_object = ntplib.NTPClient()
UPLOAD_FOLDER = os.path.join(Path(__file__).parent,'upload_folder')
STATIC_FOLDER = os.path.join(Path(__file__).parent,'static')

for dir_list in [UPLOAD_FOLDER,STATIC_FOLDER]:
    for root, dirs, files in os.walk(dir_list):
        for file in files:
            os.remove(os.path.join(root, file))



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
classified_json = {}

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
        files = request.files.getlist("file")
        uploaded_json = {}
        for file in files:
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_full_path_upload_folder = os.path.join(UPLOAD_FOLDER, filename)
                file_full_path_static_folder = os.path.join(STATIC_FOLDER, filename)
                file.save(file_full_path_upload_folder)
                shutil.copy(file_full_path_upload_folder, file_full_path_static_folder)
                # return redirect(url_for('download_file', name=filename))
                predicted_probs,predicted_class = None,None
                predicted_probs,predicted_class = classify_image(file_full_path_upload_folder,5)
                
                # return jsonify({'Predicted_Probability': predicted_probs,
                #                 'Predicted_Class' : predicted_class})
                response = current_time_object.request('asia.pool.ntp.org', version=3)

                classified_json.update({filename:{"predicted_probs" : predicted_probs,
                                                "predicted_class" : predicted_class,
                                                "timestamp" : ctime(response.tx_time)}})
                uploaded_json.update({filename:{"predicted_probs" : predicted_probs,
                                "predicted_class" : predicted_class,
                                "timestamp" : ctime(response.tx_time)}})

            else:
                return "file format does not match"
        return render_template('grid_image2.html', image_name=uploaded_json)
    else:
        return "check if File is passed with right format and Method is POST "

@app.route('/downloads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)


# https://www.youtube.com/watch?v=7pOXnc5kS54
@app.route("/shutdown")
def shutdown_server():
    print("Shutting down server")
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown is None:
        raise RuntimeError("Function not Available")
    else:
        shutdown()
        return "The server is shutting down!"

@app.route('/gallery')
def gallery():
    # image_names = os.listdir('/home/rampfire/Pictures')
    # image_names = [os.path.join('/home/rampfire/Pictures',path) for path in image_names]
    # print(image_names)
    return render_template('grid_image2.html', image_name=classified_json)

@app.route('/details/<name>')
def details(name):
    im = cv2.imread(os.path.join(UPLOAD_FOLDER,name))
    height_image, width_image, channel = im.shape
    return render_template('detail3.html',height = 400,width = 300,name = name,
                            conf_list = classified_json[name]["predicted_probs"],
                            class_list = classified_json[name]["predicted_class"],zip = zip,
                            height_image = height_image,width_image = width_image,channel = channel)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)
    # app.run(port = 5000)