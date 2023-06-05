from dbhelpers import run_statement
from flask import Flask
import json

app = Flask(__name__)

@app.get("/animals")
def get_animals():
    results = run_statement('CALL return_animals()')
    if(type(results) == list):
        json_animals = json.dumps(results, default=str)
        return json_animals
    else:
        return "Sorry, something has gone wrong. Please try again"
    
app.run(debug=True)
