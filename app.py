# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 05:24:22 2020

@author: test
"""
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
import math as m

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


R0 = 6.9364*(10**8) ## Radius of Sun (m)
L0 = 3.828*(10**26) ## Luminosity of Sun (w/m2)
sigma = 5.67*(10**(-8)) ## Stefan Boltzman Constant
pi = m.pi
s1 = 1.1 ## Appropriate Solar Flux for inner boundary
s2 = 0.53 ## Appropriate Solar Flux for outer boundary 

    
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/table')
def table():
    return (render_template('table.html'))


def create_df(keys, values):
    df = pd.DataFrame(values).T
    df.columns = keys
    return df

@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    keys = [x for x in request.form.keys()]
    
    del int_features[3:5]
    del keys[3:5]
    
    
    for i in range(0, len(int_features)):
        int_features[i] = float(int_features[i])
    
    st_rad = int_features[6]*R0
    lum = 4*pi*sigma*(st_rad**2)*(int_features[5]**4)
    app_mag = lum/L0
    
    del int_features[-1]
    int_features.append(app_mag)

    # Inner Zone
    inner_radius = np.sqrt(int_features[-1]/1.1)
    int_features.append(inner_radius)

    outer_radius = np.sqrt(int_features[7]/0.53)
    int_features.append(outer_radius)
    
    # a is the value of bin
    temp = int_features[5]
    if (temp>574 and temp<=3500):
        a = 1
    elif (temp>3500 and temp<=5000):
        a = 2
    elif (temp>5000 and temp<=6000):
        a = 3
    elif (temp>6000 and temp<=7500):
        a = 4
    elif (temp>7500 and temp<=10000):
        a = 5
    elif (temp>10000 and temp<=25000):
        a = 6
    else:
        a = 7
    int_features.append(a)
    
    int_features[2] = np.log(int_features[2])
    int_features[3] = np.log(int_features[3])
    int_features[4] = np.log1p(int_features[4])
    int_features[5] = np.log(int_features[5])
    int_features[6] = np.log(int_features[6])
    int_features[7] = np.log(int_features[7])
    int_features[8] = np.log1p(int_features[8])
    int_features[9] = np.log1p(int_features[9])
    
    keys += ['Inner_radius', 'Outer_radius', 'st_class']
    
    dff = create_df(keys, int_features)
    
    y_output = model.predict(dff)
    
    if (y_output) == 1:
        val_print = "It is a Habitable Exoplanet"
    else:
        val_print = "It is not a Habitable Exoplanet"
    

    return render_template('index.html', prediction = val_print)


if __name__ == "__main__":
    app.run()
 



