FROM tensorflow/tensorflow:1.14.0-py3

ADD static/ ./static
ADD templates/ ./templates
ADD user_inputs/ ./user_inputs
ADD 784model.h5 ./
ADD 784model.json ./
ADD requirements.txt ./
ADD main.py ./
ADD loadmodel.py ./
ADD app.yaml ./
ADD README.md ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]