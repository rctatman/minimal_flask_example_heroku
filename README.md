
Here's a quick guide to each of the files and information whether you need to edit each:

## Files you'll put the code you wrote yesterday into 

[In yesterday's notebook](https://www.kaggle.com/rtatman/careercon-making-an-app-from-your-modeling-code), as the very last exercise we wrote two cells of code, each of which will be a single file. 

* **serve.py**: This is the file you should put the code from the first cell in; this is where you'll define the functions that will read in your trained models.
* **script.py**: This is where you'll put the code from your second notebook in. This is what will define the behaviour of our different endpoints.  

## Files you'll need to add

If you are going to use a pre-trained model, be sure to add it to your repo so that you can read it in. If you like, you can store your models in a new file, but if you do this be sure to update the file path of the code that you read them in. So if you have a model called "my_model.pkl" in a folder called "models", you'll need to update the code that reads it in from this:


```
pickle.load(open("my_model.pkl", "rb")
```

to this:

```
pickle.load(open("models/my_model.pkl", "rb")
```

## Files you'll need to edit

* **README**: This is the file you're currently reading. You'll probably want to update this to have information about your specific API and how to use it.
* **openapi.yaml**: This is the specification file that we wrote on day 1. ([The notebook's here if you need a refresher](https://www.kaggle.com/rtatman/careercon-intro-to-apis)). You'll want to replace this file with the OpenAPI specification file you wrote on day 1.
* **requirements.txt**: This file has information on what packages you use in your app. *You need to make sure that you list every package you import and also gunicorn*. If you remove the line with gunicorn or forget to include a package you import somewhere else, you'll get an error when you try to run your app. 
* **runtime.txt**: This file tells Heroku which version of Python to use to run your app. You'll only need to update this file if you pickled your model file using a different version of Python & that's causing your code to break. 


## File you don't need to edit

* **LICENSE**: This file is the license your code is released under. If you don't include a license, other folks won't be able to reuse your code. If you fork this repository for your own work, you'll need to keep the license. I've used Apache 2.0 here because that's the same license as public Kaggle Kernels. 
* **Procfile**: This file is required by Heroku. It tells Heroku how to run your application. You probably don't need to change this file. 
