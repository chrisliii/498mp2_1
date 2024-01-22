from flask import Flask, redirect, url_for, request
import os
app = Flask(__name__)



@app.route('/',methods = ['POST'])
def post_seed():
   value = request.get_json().get('num')
   os.environ["SEED"] = str(value)
   return "true"

@app.route('/',methods = ['GET'])
def get_seed():
   return str(os.environ["SEED"])


if __name__ == '__main__':
   os.environ["SEED"] = "0"
   app.run(debug = True, port=80)