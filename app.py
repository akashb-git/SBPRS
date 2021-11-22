
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
from model import Recommendation

recommend = Recommendation()
app = Flask(__name__)  # intitialize the flaks app  # common 

import os
from flask import send_from_directory

@app.route('/', methods = ['POST', 'GET'])
def home():
    flag = False 
    data = ""
    return render_template('index.html', data=data, flag=flag)

@app.route('/productList', methods = ['GET'])
def productList():
    user=request.args.get("userid")
    data=recommend.getTopProductsNew(user)
    return data

if __name__ == '__main__' :
    app.run(debug=True )  
    
    #,host="0.0.0.0")
