from flask import Flask, jsonify, request
from serve import get_keywords_api
import json

app=Flask(__name__)

# This will print some text at our app's URL
# so that we can check that it's working. If you 
# wanted a more complex UI you could put it here.
@app.route('/')
def index():
    return "Up and running!"

# load our pre-trained model & function to run it on
# new data. This design is based on one proposed by 
# Guillaume Genthial. More details: 
#https://guillaumegenthial.github.io/serving.html
keywords_api = get_keywords_api()

# Define a post method for our API. 
@app.route('/extractpackages', methods=['POST'])
# function that this method will run
def extractpackages():
    """Extract packages
    Pass in a single json file with a text span in it. It 
    will return any Python packages mentioned in that span,
    along with their index (in characters).
    """
    # get the json file with our text data in it
    input_data = request.get_json()
    
    # use our API function to extract the keywords
    output_data = keywords_api(input_data)

    # convert our dictionary output into a .json file
    response = json.dumps(output_data)
    
    # return our json file
    return response
