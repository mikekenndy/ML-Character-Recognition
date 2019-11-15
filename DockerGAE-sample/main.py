import flask
from flask import Flask, render_template,request
import imageio as imgio
import numpy as np
import tensorflow.keras.models
import os
import jsonpickle
from werkzeug.utils import secure_filename

from loadmodel import * 

UPLOAD_FOLDER = '/'

app = Flask(__name__)
global model, graph
model, graph = init()

# image has 4 bytes data for each pixel? -> 4 * 28 * 28 = 3136?
# but each foramt has different way of compressing data
app.config['MAX_CONTENT_LENGTH'] =  10 * 1024  #to prevent large images come in
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template("index.html")

# shows the list of files saved in /user_inputs folder
@app.route('/dir/',methods=['GET','POST'])
def dir():
    out_str = ''
    for file in os.listdir("user_inputs"):
        out_str = out_str + str(file) + ' / '

    response = {'list': out_str}
    response_pickled = jsonpickle.encode(response)
    return flask.Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/test/',methods=['GET','POST'])
def test():
    with graph.as_default():
        img1 = imgio.imread('static/1.png',pilmode='L')
        img5 = imgio.imread('static/5.png',pilmode='L')
        img7 = imgio.imread('static/7.png',pilmode='L')
        img8 = imgio.imread('static/8.png',pilmode='L')

        flatten = get_flatten([img1, img5, img7, img8])
        np_flatten = np.array(flatten, np.float32)

        prediction = model.predict(np_flatten)
        out_str = ''
        for p in prediction:
            l = list(p)
            out_str = out_str + str(l.index(max(l))) + '  '

        return out_str

@app.route('/predict/',methods=['GET','POST'])
def predict():
    imagefile = request.files.get('file', '')
    #print(imagefile)
    #print('@@@@@@@@@@@@@@@@@@@@')
    #print(imagefile.__dict__)
    #print('@@@@@@@@@@@@@@@@@@@@')
    #import inspect
    #print(inspect.getmembers(imagefile))
    #print('@@@@@@@@@@@@@@@@@@@@')

    # converting directly into numpy array not working.. so
    # save the file and then read in the saved file
    filename = secure_filename(imagefile.filename)
    save_path = os.path.dirname(os.path.realpath(__file__))
    save_path = os.path.join(save_path, 'user_inputs') #concat the folder name
    save_path = os.path.join(save_path, filename)
    imagefile.save(save_path)

    # read in the saved file, and flatten
    img = imgio.imread('user_inputs/' + filename ,pilmode='L')
    flatten = get_flatten([img])
    np_flatten = np.array(flatten, np.float32)

    prediction = model.predict(np_flatten)
    out_str = ''
    for p in prediction:
        l = list(p)
        out_str = out_str + str(l.index(max(l))) + '  '
    
    # remove the saved image.
    os.remove(save_path)
    
    response = {'result': out_str}
    response_pickled = jsonpickle.encode(response)

    return flask.Response(response=response_pickled, status=200, mimetype="application/json")

# input == numpy array shape of 28x28
def get_flatten(img_list):
    flatten = []
    for img in img_list:
        temp = []
        for i in range(0,28):
            for j in range(0,28):
                temp.append(img[i][j])
        flatten.append(temp)
    return flatten

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8080))
	app.run(host='0.0.0.0', port=port)
