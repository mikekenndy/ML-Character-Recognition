from flask import Flask, render_template,request
import imageio as imgio
import skimage.transform
import numpy as np
import tensorflow.keras.models
import os
from loadmodel import * 


app = Flask(__name__)
global model, graph
model, graph = init()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/test/',methods=['GET','POST'])
def test():
	with graph.as_default():
		img1 = imgio.imread('static/1.png',pilmode='L')
		img5 = imgio.imread('static/5.png',pilmode='L')
		img7 = imgio.imread('static/7.png',pilmode='L')
		img8 = imgio.imread('static/8.png',pilmode='L')

		flatten = []
		for img in [img1, img5, img7, img8]:
		    temp = []
		    for i in range(0,28):
		        for j in range(0,28):
		            temp.append(img[i][j])
		    flatten.append(temp)

		np_flatten = np.array(flatten, np.float32)

		print("##################################3")
		print(model)

		prediction = model.predict(np_flatten)
		out_str = ''
		for p in prediction:
		    l = list(p)
		    out_str = out_str + str(l.index(max(l))) + '  '

		return out_str
	
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8080))
	app.run(host='0.0.0.0', port=port)
