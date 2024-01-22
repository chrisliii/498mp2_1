from flask import Flask, redirect, url_for, request
import os
import subprocess
import socket
app = Flask(__name__)



@app.route('/',methods = ['POST'])
def post_seed():
   subprocess.Popen(["sudo", "python3", "stress_cpu.py"])
   return "true"

@app.route('/',methods = ['GET'])
def get_seed():
   return str(socket.gethostname())


if __name__ == '__main__':
   os.environ["SEED"] = "0"
   app.run(debug = True, port=80, host='0.0.0.0')