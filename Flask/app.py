# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:42:52 2022

@author: HP
"""


import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph=tf.get_default_graph()
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer#no need these for ml models but only for deep leaning models

app=Flask(__name__)

model=load_model(r"C:\Users\HP\Desktop\AI project\Flask\bc.h5")

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['image']
        print("current path")
        basepath=os.path.dirname(__file__)
        print("current path",basepath)
        filepath=os.path.join(basepath,'uploads',f.filename)
        print("upload folder is",filepath)
        f.save(filepath)
        
        img=image.load_img(filepath,target_size=(64,64))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        
        with graph.as_default():
            pred=model.predict_classes(x)
        p=model.predict(x)
        
        if(p[0]==0):
            text1="The tumour is malignant"
        elif(p[0]==1):
            text1="The tumour is benign"
        
    return text1

if __name__=='__main__':
    app.run(debug=True,threaded=False)
