import os 
from flask import Flask, render_template, url_for
import json
app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('test2.html')
    #return "<p>Hello, World!</p>"

    
def showjson():
   filename = os.path.join(app.static_folder, 'real_data.json')
   with open(filename) as test_file:
    data = json.load(test_file)
   return render_template('showjson.jade', data=data)
    
if __name__ == "__main__":
    app.run(debug=True)