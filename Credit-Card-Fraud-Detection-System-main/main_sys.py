# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 00:48:22 2023

@author: Neliswa Dlamini
"""
from flask import Flask , request
from flask import render_template
import webbrowser
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

url= 'http://127.0.0.1:5000/'  
webbrowser.open_new_tab(url)

#welcome page / root page
@app.route('/')
def index():
    return render_template('GUI.html')

@app.route('/', methods=['POST'])
def getvalue():
    distance_from_home = request.form['distance_from_home']
    distance_from_last_transaction = request.form['distance_from_last_transaction']
    ratio_to_median_purchase_price = request.form['ratio_to_median_purchase_price']
    repeat_retailer = request.form['repeat_retailer']
    used_chip = request.form['used_chip']
    used_pin_number = request.form['used_pin_number']
    online_order = request.form['online_order']
    
    x0 = [[distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order]]
        
    prediction = classifier.predict(x0)
    # probability = classifier.predict_proba(x0)
    if prediction == 0:
        prediction = 'Not Fraud'        
    else:
        prediction = 'Fraud'
    return render_template("outputGUI.html", pred=prediction)
    
    
    #return "The Credit Card is " + str(prediction


if __name__ == '__main__':
    app.run(port=5000)

    
    
