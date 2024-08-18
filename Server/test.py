from flask import Flask, jsonify
from flask_cors import CORS
import Graph

app = Flask(__name__)
# connect Vite (frontend) with Flask (backend)
cors = CORS(app, origins="*")

@app.route("/", methods=['GET'])
def index():
    return "<h1>The Flask App Has Been Successfully Hosted</h1>"

@app.route("/graph", methods=['GET','POST'])
def graph():
    return jsonify (
        
    )
    
if __name__ == "__main__":
    app.run(debug=True)