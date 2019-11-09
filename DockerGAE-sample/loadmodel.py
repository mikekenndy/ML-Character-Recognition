import numpy as np
import tensorflow.keras.models
from tensorflow.keras.models import model_from_json
import tensorflow as tf


def init(): 
	json_file = open('784model.json','r')
	model_json = json_file.read()
	json_file.close()

	model = tensorflow.keras.models.model_from_json(model_json)
	model.load_weights("784model.h5")

	model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	graph = tf.get_default_graph()

	return model, graph