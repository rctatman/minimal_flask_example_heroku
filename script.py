from flask import Flask
from serve import useless_function  

app=Flask(__name__)

# Define our "ping" end point
@app.route('/ping')
def ping():
  output = useless_function()
  return output
