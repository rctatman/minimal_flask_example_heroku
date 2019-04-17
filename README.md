This is a very simple Flask app that lets you identify & get the spans of text that are the names of popular Python packages.

The app is currently served on Heroku at https://kaggle-test.herokuapp.com/. 

To query it, you can use the following Python syntax:

```
import requests
input_text  = "Pandas is my favorite library. I don't like numpy as much as future."
requests.post('http://kaggle-test.herokuapp.com/extractpackages', json=input_text).json()
```
