from dbhelpers import run_statement
from flask import Flask
import json

app = Flask(__name__)

# Create animals endpoint
@app.get("/animals")
def get_animals():
    # Call the run_statement function imported above from dbhelpers file
    results = run_statement('CALL return_animals()')
    if(type(results) == list):
        # If the returned value is a list, which means that the call worked, convert the data to json
        json_animals = json.dumps(results, default=str)
        return json_animals
    else:
        return "Sorry, something has gone wrong. Please try again"

# Create dogs endpoint
@app.get('/dogs')
def get_dogs():
    # Same logic but provide another DB procedure
    results = run_statement('CALL return_dogs()')
    if(type(results) == list):
        json_dogs = json.dumps(results, default=str)
        return json_dogs
    else:
        return "Sorry, something has gone wrong. Please try again"
    
@app.get('/cats')
def get_cats():
    # Another DB procedure
    results = run_statement('CALL return_cats()')
    if(type(results) == list):
        json_cats = json.dumps(results, default=str)
        return json_cats
    else:
        return "Sorry, something has gone wrong. Please try again"
    
app.run(debug=True)
